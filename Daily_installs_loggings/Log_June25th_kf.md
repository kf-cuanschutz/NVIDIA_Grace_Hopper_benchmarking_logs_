Logs Jun 25th:
==============

* In the NVIDIA rapids container, I cannot profile my experiments so I had to install the necessary packages witht the command below inside the container.

```bash
export CONTAIN_DIR=${PWD}
export FUNC_DIR=/home/a10-kfotso/containers_img_
apptainer shell -H $CONTAIN_DIR --bind=$FUNC_DIR --fakeroot --nv
conda install nvidia::cuda-nvprof -y
conda install nvidia::nsight-compute -y
```

But then I got the following error:

```bash
## Package Plan ##

  environment location: /opt/conda

  added / updated specs:
    - nvidia::nsight-compute


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    nsight-compute-2024.1.1.4  |                0       282.9 MB  nvidia
    ------------------------------------------------------------
                                           Total:       282.9 MB

The following NEW packages will be INSTALLED:

  nsight-compute     nvidia/linux-aarch64::nsight-compute-2024.1.1.4-0 

The following packages will be UPDATED:

  ca-certificates                       2024.2.2-hcefe29a_0 --> 2024.6.2-hcefe29a_0 
  certifi                             2024.2.2-pyhd8ed1ab_0 --> 2024.6.2-pyhd8ed1ab_0 
  openssl                                  3.3.0-h31becfc_0 --> 3.3.1-h68df207_0 



Downloading and Extracting Packages:
                                                                                                                                                                                                                  
Preparing transaction: done
Verifying transaction: failed

EnvironmentNotWritableError: The current user does not have write permissions to the target environment.
  environment location: /opt/conda
  uid: 1001
  gid: 1001


```

* I then created the an overlay and but got the following error:

```bash

a10-kfotso@a10-cuanschutz01:~/benchmarking_/NVIDIA_Rapids$ apptainer overlay create --fakeroot --sparse --size 100000 nvidia_rapids_.img
a10-kfotso@a10-cuanschutz01:~/benchmarking_/NVIDIA_Rapids$ apptainer shell -H $CONTAIN_DIR --bind=$FUNC_DIR --fakeroot --nv --containall --overlay nvidia_rapids_.img $FUNC_DIR/nvidia_rapids_.sif 

The following NEW packages will be INSTALLED:

  cuda-nvprof        nvidia/linux-aarch64::cuda-nvprof-11.7.101-0 

The following packages will be UPDATED:

  ca-certificates                       2024.2.2-hcefe29a_0 --> 2024.6.2-hcefe29a_0 
  certifi                             2024.2.2-pyhd8ed1ab_0 --> 2024.6.2-pyhd8ed1ab_0 
  openssl                                  3.3.0-h31becfc_0 --> 3.3.1-h68df207_0 



Downloading and Extracting Packages:

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
ERROR conda.core.link:_execute(949): An error occurred while installing package 'conda-forge::ca-certificates-2024.6.2-hcefe29a_0'.
Rolling back transaction: done
```

So I finally ran conda update all:

```bash
apptainer shell -H $CONTAIN_DIR --bind=$FUNC_DIR --fakeroot --nv --containall --overlay nvidia_rapids_.img $FUNC_DIR/nvidia_rapids_.sif
 conda update --all
```

Didn't work, please see issue [here](https://github.com/kf-cuanschutz/NVIDIA_Grace_Hopper_benchmarking_logs_/issues/8) 

I instead built a conda ENV with nvidia rapids and installed nvprof that way

Seems like it works when creating a new CONDA ENV. See below:

```bash
conda create -n rapids_ml_2 -c rapidsai -c conda-forge -c nvidia  \
    rapids=24.06 python=3.11 cuda-version=11.2

 conda activate rapids_ml_2     

conda install nvidia::cuda-nvprof -y  
conda install nvidia::nsight-compute -y                                                                                                                                                                           
Channels:                                                                                                                                                                                                         
 - defaults                                                                                                                                                                                                       
 - nvidia                                                                                                                                                                                                         
 - conda-forge                                                                                                                                                                                                    
 - rapidsai                                                                                                                                                                                                       
Platform: linux-aarch64                                                                                                                                                                                           
Collecting package metadata (repodata.json): done                                                                                                                                                                 
Solving environment: done                                                                                                                                                                                         
                                                                                                                                                                                                                  
## Package Plan ##                                                                                                                                                                                                
                                                                                                                                                                                                                  
  environment location: /home/a10-kfotso/.conda/envs/rapids_ml_2                                                                                                                                                  
                                                                                                                                                                                                                  
  added / updated specs:                                                                                                                                                                                          
    - nvidia::cuda-nvprof                                                                                                                                                                                         
                                                                                                                                                                                                                  
                                                                                                                                                                                                                  
The following packages will be downloaded:                                                                                                                                                                        
                                                                                                                                                                                                                  
    package                    |            build                                                                                                                                                                 
    ---------------------------|-----------------                                                                                                                                                                 
    certifi-2024.6.2           |  py311hd43f75c_0         161 KB                                                                                                                                                  
    ------------------------------------------------------------                                                                                                                                                  
                                           Total:         161 KB                                                                                                                                                  
                                                                                                                                                                                                                  
The following NEW packages will be INSTALLED:                                                                                                                                                                     
                                                                                                                                                                                                                  
  cuda-nvprof        nvidia/linux-aarch64::cuda-nvprof-11.7.101-0                                                                                                                                                 
                                                                                                                                                                                                                  
The following packages will be SUPERSEDED by a higher-priority channel:                                                                                                                                           
                                                                                                                                                                                                                  
  certifi            conda-forge/noarch::certifi-2024.6.2-~ --> pkgs/main/linux-aarch64::certifi-2024.6.2-py311hd43f75c_0                                                                                         
                                                                                                                                                                                                                  
                                                                                                                                                                                                                  
                                                                                                                                                                                                                  
Downloading and Extracting Packages:                                                                                                                                                                              
                                                                                                                                                                                                                  
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
Channels:
 - defaults
 - nvidia
 - conda-forge
 - rapidsai
Platform: linux-aarch64
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: /home/a10-kfotso/.conda/envs/rapids_ml_2

  added / updated specs:
    - nvidia::nsight-compute


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    nsight-compute-2024.1.1.4  |                0       282.9 MB  nvidia
    ------------------------------------------------------------
                                           Total:       282.9 MB

The following NEW packages will be INSTALLED:

  nsight-compute     nvidia/linux-aarch64::nsight-compute-2024.1.1.4-0 



Downloading and Extracting Packages:
                                                                                                                                                                                                                  
Preparing transaction: done
Verifying transaction: done
Executing transaction: done

```
