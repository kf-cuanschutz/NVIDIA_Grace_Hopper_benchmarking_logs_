NVIDIA Rapids:
==============

```bash
 export CONTAIN_DIR=${PWD}
 export FUNC_DIR=/home/a10-kfotso/containers_img_
 apptainer run -H $CONTAIN_DIR --bind=$FUNC_DIR --nv nvidia_rapids_.sif python3 dbscan_gpu.py 
```

Got in return:

```bash
NameError: name 'cuml' is not defined
```

Let's see what is inside the container:
```bash
apptainer shell -H $CONTAIN_DIR --bind=$FUNC_DIR --nv nvidia_rapids_.sif
pip list | grep cuml
```
And I get
```bash
cuml                      24.4.0
```
Then I run:

```bash
Apptainer> python
Python 3.11.9 | packaged by conda-forge | (main, Apr 19 2024, 18:25:01) [GCC 12.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import cuml
>>> exit()
```

Looks like I forgot to add the following in my python scripts based on the reference [here](https://docs.rapids.ai/api/cuml/stable/estimator_intro/):

```bash
import cuml
from cupy import asnumpy
from joblib import dump, load
```

After running both the dbscan script I get the following:

```bash
a10-kfotso@a10-cuanschutz01:~/benchmarking_/NVIDIA_Rapids$ apptainer run -H $CONTAIN_DIR --bind=$FUNC_DIR --nv $FUNC_DIR/nvidia_rapids_.sif python dbscan_gpu.py 
This container image and its contents are governed by the NVIDIA Deep Learning Container License.
By pulling and using the container, you accept the terms and conditions of this license:
https://developer.download.nvidia.com/licenses/NVIDIA_Deep_Learning_Container_License.pdf

 cuml's adjusted random index score :  1.0
 sklearn's adjusted random index score :  1.0
```

After running the umap script I get the following:

```bash
a10-kfotso@a10-cuanschutz01:~/benchmarking_/NVIDIA_Rapids$ apptainer run -H $CONTAIN_DIR --bind=$FUNC_DIR --nv $FUNC_DIR/nvidia_rapids_.sif python umap_clustering_gpu.py 
This container image and its contents are governed by the NVIDIA Deep Learning Container License.
By pulling and using the container, you accept the terms and conditions of this license:
https://developer.download.nvidia.com/licenses/NVIDIA_Deep_Learning_Container_License.pdf

 cuml's trustworthiness score :  0.8524086693548387
 sklearn's trustworthiness score :  0.8524084677419355
```

Time for some profiling.

* For profiling I had to reinstall NVIDIA Rapids through the Pytorch sif container. Please refer to this[issue](https://github.com/kf-cuanschutz/NVIDIA_Grace_Hopper_benchmarking_logs_/issues/9) for more information.

I ran the following:

```bash
export CONTAIN_DIR=${PWD}
apptainer overlay create --fakeroot --sparse --size 100000 rapids_pytorch_img_
export FUNC_DIR=/home/a10-kfotso/containers_img_
apptainer shell -H $CONTAIN_DIR --bind=$FUNC_DIR --fakeroot --nv --containall --overlay rapids_pytorch_img_ pytorch.sif
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh
chmod +x Miniconda3-latest-Linux-aarch64.sh
bash Miniconda3-latest-Linux-aarch64.sh
conda create -n rapids-24.06 -c rapidsai -c conda-forge -c nvidia  \
    rapids=24.06 python=3.11 cuda-version=11.2
```

Now running it with the rapids ENV

```bash
cd /home/a10-kfotso/benchmarking_/NVIDIA_Rapids                                                                                                                                       export CONTAIN_DIR=${PWD}
export FUNC_DIR=/home/a10-kfotso/containers_img_
apptainer shell -H $CONTAIN_DIR --bind=$FUNC_DIR --fakeroot --nv --containall --overlay $FUNC_DIR/rapids_pytorch_img_ $FUNC_DIR/pytorch.sif
eval "$(/home/a10-kfotso/containers_img_/miniconda3/bin/conda shell.bash hook)"
conda activate rapids-24.06;nsys profile --stats=true python umap_clustering_gpu.py 
```

I did get the following:

```bash
Generating '/tmp/nsys-report-2726.qdstrm'
[1/8] [========================100%] report1.nsys-rep
[2/8] [========================100%] report1.sqlite
[3/8] Executing 'nvtx_sum' stats report

 Time (%)  Total Time (ns)  Instances    Avg (ns)      Med (ns)     Min (ns)    Max (ns)   StdDev (ns)   Style                Range             
 --------  ---------------  ---------  ------------  ------------  ----------  ----------  -----------  -------  -------------------------------
     82.2       8492014432          1  8492014432.0  8492014432.0  8492014432  8492014432          0.0  PushPop  cuml_python:datasets.make_blobs
     17.8       1838923872          1  1838923872.0  1838923872.0  1838923872  1838923872          0.0  PushPop  librmm:allocate_async          
      0.0            56640          1       56640.0       56640.0       56640       56640          0.0  PushPop  librmm:deallocate_async        

[4/8] Executing 'osrt_sum' stats report

 Time (%)  Total Time (ns)  Num Calls   Avg (ns)    Med (ns)    Min (ns)  Max (ns)   StdDev (ns)           Name         
 --------  ---------------  ---------  ----------  -----------  --------  ---------  -----------  ----------------------
     89.3       8290892128         97  85473114.7  100103168.0      1120  303983808   40591424.3  poll                  
      9.5        879895040       2593    339334.8      30912.0      1024   42067584    1140807.9  ioctl                 
      0.4         33216704       4011      8281.4       6912.0      1024    3569952      56759.8  read                  
      0.3         31350656       9817      3193.5       2752.0      1472     306144       4626.5  munmap                
      0.2         17705696       3463      5112.8       4800.0      1024      54592       2225.9  open64                
      0.2         17164448       8573      2002.2       1440.0      1024     445216       5081.7  mmap64                
      0.0          3633504        182     19964.3      16736.0      1728     152064      18055.7  mmap                  
      0.0          2191008          3    730336.0      38080.0     31328    2121600    1204874.7  waitpid               
      0.0          1114112        208      5356.3       3216.0      1024     271040      19053.7  fopen                 
      0.0           536288         53     10118.6       1344.0      1120     313472      43072.2  write                 
      0.0           270368         13     20797.5      10976.0      1344     107616      29789.3  fgets                 
      0.0           262048        130      2015.8       1408.0      1024       5760       1208.6  fclose                
      0.0           228960         10     22896.0      14576.0     11136      95168      25618.7  sem_timedwait         
      0.0           180256          3     60085.3      62784.0     52416      65056       6738.3  pthread_create        
      0.0           163008          2     81504.0      81504.0     73472      89536      11359.0  pthread_cond_wait     
      0.0           114656         24      4777.3       3232.0      1792      10240       2847.6  open                  
      0.0            78944         15      5262.9       2752.0      1696      12704       3876.3  fopen64               
      0.0            73472         13      5651.7       3488.0      2080      11008       3359.6  pipe2                 
      0.0            58304          4     14576.0      12240.0      8160      25664       7700.7  socket                
      0.0            34240          2     17120.0      17120.0     16416      17824        995.6  connect               
      0.0            15840          3      5280.0       3456.0      1152      11232       5281.7  signal                
      0.0            10880          2      5440.0       5440.0      4832       6048        859.8  pthread_cond_broadcast
      0.0            10368          3      3456.0       3040.0      3008       4320        748.4  fwrite                
      0.0            10304          2      5152.0       5152.0      3712       6592       2036.5  stat                  
      0.0             8704          6      1450.7       1328.0      1152       1888        300.6  sigaction             
      0.0             8640          3      2880.0       1344.0      1024       6272       2941.9  fputs                 
      0.0             6144          2      3072.0       3072.0      2624       3520        633.6  bind                  
      0.0             5952          5      1190.4       1216.0      1024       1344        122.7  fcntl                 
      0.0             4288          2      2144.0       2144.0      2080       2208         90.5  mprotect              
      0.0             3424          2      1712.0       1712.0      1120       2304        837.2  dup2                  
      0.0             2816          1      2816.0       2816.0      2816       2816          0.0  fread                 
      0.0             2080          1      2080.0       2080.0      2080       2080          0.0  listen                

[5/8] Executing 'cuda_api_sum' stats report

 Time (%)  Total Time (ns)  Num Calls    Avg (ns)      Med (ns)    Min (ns)   Max (ns)   StdDev (ns)               Name            
 --------  ---------------  ---------  ------------  ------------  --------  ----------  ------------  ----------------------------
     75.2       5572407808          2  2786203904.0  2786203904.0     52480  5572355328  3940213130.6  cudaFree                    
     24.8       1838933920          2   919466960.0   919466960.0     15744  1838918176  1300300379.6  cudaMalloc                  
      0.0           400224          1      400224.0      400224.0    400224      400224           0.0  cudaStreamIsCapturing_v10000
      0.0           121568          1      121568.0      121568.0    121568      121568           0.0  cudaDeviceSynchronize       
      0.0            61664        385         160.2          96.0        32        1824         172.9  cuGetProcAddress            
      0.0            54752          1       54752.0       54752.0     54752       54752           0.0  cudaMemGetInfo              
      0.0            43872          2       21936.0       21936.0      8512       35360       18984.4  cudaLaunchKernel            
      0.0            26880          1       26880.0       26880.0     26880       26880           0.0  cuModuleLoadData            
      0.0             8384          4        2096.0        2096.0      1792        2400         264.5  cuInit                      
      0.0              384          1         384.0         384.0       384         384           0.0  cuModuleGetLoadingMode      

[6/8] Executing 'cuda_gpu_kern_sum' stats report

 Time (%)  Total Time (ns)  Instances  Avg (ns)  Med (ns)  Min (ns)  Max (ns)  StdDev (ns)                                                  Name                                                
 --------  ---------------  ---------  --------  --------  --------  --------  -----------  ----------------------------------------------------------------------------------------------------
     98.5           118272          1  118272.0  118272.0    118272    118272          0.0  void generate_seed_pseudo<rng_config<curandStateXORWOW, (curandOrdering)101>>(unsigned long long, u…
      1.5             1824          1    1824.0    1824.0      1824      1824          0.0  void gen_sequenced<curandStateXORWOW, float, int, &curand_uniform_noargs<curandStateXORWOW>, rng_co…

[7/8] Executing 'cuda_gpu_mem_time_sum' stats report
SKIPPED: /home/a10-kfotso/benchmarking_/NVIDIA_Rapids/report1.sqlite does not contain GPU memory data.
[8/8] Executing 'cuda_gpu_mem_size_sum' stats report
SKIPPED: /home/a10-kfotso/benchmarking_/NVIDIA_Rapids/report1.sqlite does not contain GPU memory data.
Generated:
    /home/a10-kfotso/benchmarking_/NVIDIA_Rapids/report1.nsys-rep
    /home/a10-kfotso/benchmarking_/NVIDIA_Rapids/report1.sqlite
(rapids-24.06) Apptainer> Generating '/tmp/nsys-report-2726.qdstrm'
[1/8] [========================100%] report1.nsys-rep
[2/8] [========================100%] report1.sqlite
[3/8] Executing 'nvtx_sum' stats report

 Time (%)  Total Time (ns)  Instances    Avg (ns)      Med (ns)     Min (ns)    Max (ns)   StdDev (ns)   Style                Range             
 --------  ---------------  ---------  ------------  ------------  ----------  ----------  -----------  -------  -------------------------------
     82.2       8492014432          1  8492014432.0  8492014432.0  8492014432  8492014432          0.0  PushPop  cuml_python:datasets.make_blobs
     17.8       1838923872          1  1838923872.0  1838923872.0  1838923872  1838923872          0.0  PushPop  librmm:allocate_async          
      0.0            56640          1       56640.0       56640.0       56640       56640          0.0  PushPop  librmm:deallocate_async        

[4/8] Executing 'osrt_sum' stats report

 Time (%)  Total Time (ns)  Num Calls   Avg (ns)    Med (ns)    Min (ns)  Max (ns)   StdDev (ns)           Name         
 --------  ---------------  ---------  ----------  -----------  --------  ---------  -----------  ----------------------
     89.3       8290892128         97  85473114.7  100103168.0      1120  303983808   40591424.3  poll                  
      9.5        879895040       2593    339334.8      30912.0      1024   42067584    1140807.9  ioctl                 
      0.4         33216704       4011      8281.4       6912.0      1024    3569952      56759.8  read                  
      0.3         31350656       9817      3193.5       2752.0      1472     306144       4626.5  munmap                
      0.2         17705696       3463      5112.8       4800.0      1024      54592       2225.9  open64                
      0.2         17164448       8573      2002.2       1440.0      1024     445216       5081.7  mmap64                
      0.0          3633504        182     19964.3      16736.0      1728     152064      18055.7  mmap                  
      0.0          2191008          3    730336.0      38080.0     31328    2121600    1204874.7  waitpid               
      0.0          1114112        208      5356.3       3216.0      1024     271040      19053.7  fopen                 
      0.0           536288         53     10118.6       1344.0      1120     313472      43072.2  write                 
      0.0           270368         13     20797.5      10976.0      1344     107616      29789.3  fgets                 
      0.0           262048        130      2015.8       1408.0      1024       5760       1208.6  fclose                
      0.0           228960         10     22896.0      14576.0     11136      95168      25618.7  sem_timedwait         
      0.0           180256          3     60085.3      62784.0     52416      65056       6738.3  pthread_create        
      0.0           163008          2     81504.0      81504.0     73472      89536      11359.0  pthread_cond_wait     
      0.0           114656         24      4777.3       3232.0      1792      10240       2847.6  open                  
      0.0            78944         15      5262.9       2752.0      1696      12704       3876.3  fopen64               
      0.0            73472         13      5651.7       3488.0      2080      11008       3359.6  pipe2                 
      0.0            58304          4     14576.0      12240.0      8160      25664       7700.7  socket                
      0.0            34240          2     17120.0      17120.0     16416      17824        995.6  connect               
      0.0            15840          3      5280.0       3456.0      1152      11232       5281.7  signal                
      0.0            10880          2      5440.0       5440.0      4832       6048        859.8  pthread_cond_broadcast
      0.0            10368          3      3456.0       3040.0      3008       4320        748.4  fwrite                
      0.0            10304          2      5152.0       5152.0      3712       6592       2036.5  stat                  
      0.0             8704          6      1450.7       1328.0      1152       1888        300.6  sigaction             
      0.0             8640          3      2880.0       1344.0      1024       6272       2941.9  fputs                 
      0.0             6144          2      3072.0       3072.0      2624       3520        633.6  bind                  
      0.0             5952          5      1190.4       1216.0      1024       1344        122.7  fcntl                 
      0.0             4288          2      2144.0       2144.0      2080       2208         90.5  mprotect              
      0.0             3424          2      1712.0       1712.0      1120       2304        837.2  dup2                  
      0.0             2816          1      2816.0       2816.0      2816       2816          0.0  fread                 
      0.0             2080          1      2080.0       2080.0      2080       2080          0.0  listen                

[5/8] Executing 'cuda_api_sum' stats report

 Time (%)  Total Time (ns)  Num Calls    Avg (ns)      Med (ns)    Min (ns)   Max (ns)   StdDev (ns)               Name            
 --------  ---------------  ---------  ------------  ------------  --------  ----------  ------------  ----------------------------
     75.2       5572407808          2  2786203904.0  2786203904.0     52480  5572355328  3940213130.6  cudaFree                    
     24.8       1838933920          2   919466960.0   919466960.0     15744  1838918176  1300300379.6  cudaMalloc                  
      0.0           400224          1      400224.0      400224.0    400224      400224           0.0  cudaStreamIsCapturing_v10000
      0.0           121568          1      121568.0      121568.0    121568      121568           0.0  cudaDeviceSynchronize       
      0.0            61664        385         160.2          96.0        32        1824         172.9  cuGetProcAddress            
      0.0            54752          1       54752.0       54752.0     54752       54752           0.0  cudaMemGetInfo              

```

I did get an error right before from Rapids. I believe it is related to the ENV:

```bash
Traceback (most recent call last):
  File "/home/a10-kfotso/benchmarking_/NVIDIA_Rapids/umap_clustering_gpu.py", line 14, in <module>
    X_blobs, y_blobs = make_blobs( n_samples = n_samples,
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/a10-kfotso/containers_img_/miniconda3/envs/rapids-24.06/lib/python3.11/site-packages/nvtx/nvtx.py", line 116, in inner
    result = func(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^
  File "/home/a10-kfotso/containers_img_/miniconda3/envs/rapids-24.06/lib/python3.11/site-packages/cuml/internals/api_decorators.py", line 188, in wrapper
    ret = func(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^
  File "/home/a10-kfotso/containers_img_/miniconda3/envs/rapids-24.06/lib/python3.11/site-packages/cuml/datasets/blobs.py", line 180, in make_blobs
    centers, n_centers = _get_centers(
                         ^^^^^^^^^^^^^
  File "/home/a10-kfotso/containers_img_/miniconda3/envs/rapids-24.06/lib/python3.11/site-packages/cuml/datasets/blobs.py", line 43, in _get_centers
    centers = rs.uniform(
              ^^^^^^^^^^^
  File "/home/a10-kfotso/containers_img_/miniconda3/envs/rapids-24.06/lib/python3.11/site-packages/cupy/random/_generator.py", line 983, in uniform
    rand = self.random_sample(size=size, dtype=dtype)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/a10-kfotso/containers_img_/miniconda3/envs/rapids-24.06/lib/python3.11/site-packages/cupy/random/_generator.py", line 630, in random_sample
    RandomState._mod1_kernel(out)
  File "cupy/_core/_kernel.pyx", line 920, in cupy._core._kernel.ElementwiseKernel.__call__
  File "cupy/_core/_kernel.pyx", line 945, in cupy._core._kernel.ElementwiseKernel._get_elementwise_kernel
  File "cupy/_util.pyx", line 64, in cupy._util.memoize.decorator.ret
  File "cupy/_core/_kernel.pyx", line 728, in cupy._core._kernel._get_elementwise_kernel
  File "cupy/_core/_kernel.pyx", line 82, in cupy._core._kernel._get_simple_elementwise_kernel_from_code
  File "cupy/_core/core.pyx", line 2258, in cupy._core.core.compile_with_cache
  File "/home/a10-kfotso/containers_img_/miniconda3/envs/rapids-24.06/lib/python3.11/site-packages/cupy/cuda/compiler.py", line 484, in _compile_module_with_cache
    return _compile_with_cache_cuda(
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/a10-kfotso/containers_img_/miniconda3/envs/rapids-24.06/lib/python3.11/site-packages/cupy/cuda/compiler.py", line 606, in _compile_with_cache_cuda
    mod.load(cubin)
  File "cupy/cuda/function.pyx", line 263, in cupy.cuda.function.Module.load
  File "cupy/cuda/function.pyx", line 265, in cupy.cuda.function.Module.load
  File "cupy_backends/cuda/api/driver.pyx", line 226, in cupy_backends.cuda.api.driver.moduleLoadData
  File "cupy_backends/cuda/api/driver.pyx", line 63, in cupy_backends.cuda.api.driver.check_status
cupy_backends.cuda.api.driver.CUDADriverError: CUDA_ERROR_INVALID_SOURCE: device kernel image is invalid
```


