### Install logs:
------------------

* The goal is to install HPL-cuda from (https://github.com/avidday/hpl-cuda)[here] so that we can do benchmarking.

* Installed mpich with the following:

```bash
 sudo apt install mpich
```

* Installed Go2blas with the following:

```bash
sudo apt-get install libopenblas-dev
```

* I activate my cuda environment which already has all the installed cublas related libraries:
  ```bash
  eval "$(/opt/miniconda3/bin/conda shell.bash hook)"
  conda activate cuda_env
  find /home/a10-kfotso/.conda/envs/cuda_env | grep -i cublas
  /home/a10-kfotso/.conda/envs/cuda_env/conda-meta/libcublas-dev-11.11.3.6-0.json
  /home/a10-kfotso/.conda/envs/cuda_env/conda-meta/libcublas-11.11.3.6-0.json
  /home/a10-kfotso/.conda/envs/cuda_env/include/cublasXt.h
  /home/a10-kfotso/.conda/envs/cuda_env/include/cublas_api.h
  /home/a10-kfotso/.conda/envs/cuda_env/include/cublasLt.h
  /home/a10-kfotso/.conda/envs/cuda_env/include/cublas.h
  /home/a10-kfotso/.conda/envs/cuda_env/include/cublas_v2.h
  /home/a10-kfotso/.conda/envs/cuda_env/lib/libcublasLt.so.11
  /home/a10-kfotso/.conda/envs/cuda_env/lib/libcublasLt_static.a
  /home/a10-kfotso/.conda/envs/cuda_env/lib/libcublas_static.a
  /home/a10-kfotso/.conda/envs/cuda_env/lib/libcublas.so
  /home/a10-kfotso/.conda/envs/cuda_env/lib/libcublas.so.11.11.3.6
  /home/a10-kfotso/.conda/envs/cuda_env/lib/stubs/libcublas.so
  /home/a10-kfotso/.conda/envs/cuda_env/lib/stubs/libcublasLt.so
  /home/a10-kfotso/.conda/envs/cuda_env/lib/libcublas.so.11
  /home/a10-kfotso/.conda/envs/cuda_env/lib/libcublasLt.so
  /home/a10-kfotso/.conda/envs/cuda_env/lib/libcublasLt.so.11.11.3.6
  ```

  * Installing cmkae with snap does not work ```sudo snap install cmake```. However the following worked
    ```bash
    sudo apt  install cmake-curses-gui
    ```

 * It looks like I can get an HPL container here: https://catalog.ngc.nvidia.com/orgs/nvidia/containers/hpc-benchmarks
   Currently building it with the following below:

   ```bash
   apptainer build  hpc-benchmarks:24.06.sif  docker://nvcr.io/nvidia/hpc-benchmarks:24.06
   ```
 * I installed slurm following this [guide](https://drtailor.medium.com/how-to-setup-slurm-on-ubuntu-20-04-for-single-node-work-scheduling-6cc909574365). For the slurm.conf file, I entered 72 CPUs and 480G memory. Also, the slurm.conf file had to be created under "/etc/slurm/" in lieu of "/etc/slurm-llnl" for it to work. I applied the permission "755" on /etc/slurm/ as well.

