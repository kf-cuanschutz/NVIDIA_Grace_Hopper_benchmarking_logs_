# Installation logs:
---------------------

```bash
conda create --name ccc_gpu_env conda-forge::python=3.9 -y
conda activate ccc_gpu_env
conda install numba -y
conda install -c conda-forge cuda-nvcc cuda-nvrtc "cuda-version>=12.0"
conda install  conda-forge::ipython -y
conda install  conda-forge::pandas -y
pip install ccc-coef
```
Packages installed in the ENV:
```bash
(ccc_gpu_env) a10-kfotso@a10-cuanschutz01:~$ conda list
# packages in environment at /home/a10-kfotso/.conda/envs/ccc_gpu_env:
#
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                        main  
_openmp_mutex             5.1                      51_gnu  
_sysroot_linux-aarch64_curr_repodata_hack 4                   h57d6b7b_16    conda-forge
asttokens                 2.0.5              pyhd3eb1b0_0  
binutils_impl_linux-aarch64 2.38                 h0c9fd12_1  
binutils_linux-aarch64    2.38.0               h0c7b1b4_0  
blas                      1.0                    openblas  
bzip2                     1.0.8                h998d150_6  
ca-certificates           2024.8.30            hcefe29a_0    conda-forge
ccc-coef                  0.1.7                    pypi_0    pypi
cuda-cccl_linux-aarch64   12.6.37              h579c4fd_0    conda-forge
cuda-crt-dev_linux-aarch64 12.6.68              h579c4fd_0    conda-forge
cuda-crt-tools            12.6.68              h579c4fd_0    conda-forge
cuda-cudart               12.6.68              h3ae8b8a_0    conda-forge
cuda-cudart-dev           12.6.68              h3ae8b8a_0    conda-forge
cuda-cudart-dev_linux-aarch64 12.6.68              h3ae8b8a_0    conda-forge
cuda-cudart-static        12.6.68              h3ae8b8a_0    conda-forge
cuda-cudart-static_linux-aarch64 12.6.68              h3ae8b8a_0    conda-forge
cuda-cudart_linux-aarch64 12.6.68              h3ae8b8a_0    conda-forge
cuda-driver-dev_linux-aarch64 12.6.68              h3ae8b8a_0    conda-forge
cuda-nvcc                 12.6.68              ha346c71_0    conda-forge
cuda-nvcc-dev_linux-aarch64 12.6.68              h4310d6a_0    conda-forge
cuda-nvcc-impl            12.6.68              h614329b_0    conda-forge
cuda-nvcc-tools           12.6.68              h614329b_0    conda-forge
cuda-nvcc_linux-aarch64   12.6.68              h028b88b_0    conda-forge
cuda-nvrtc                12.6.68              h3ae8b8a_0    conda-forge
cuda-nvvm-dev_linux-aarch64 12.6.68              h579c4fd_0    conda-forge
cuda-nvvm-impl            12.6.68              h614329b_0    conda-forge
cuda-nvvm-tools           12.6.68              h614329b_0    conda-forge
cuda-version              12.6                 h7480c83_3    conda-forge
decorator                 5.1.1              pyhd3eb1b0_0  
exceptiongroup            1.2.0            py39hd43f75c_0  
executing                 0.8.3              pyhd3eb1b0_0  
gcc_impl_linux-aarch64    11.2.0               h1234567_1  
gcc_linux-aarch64         11.2.0               h3fc98b3_0  
gxx_impl_linux-aarch64    11.2.0               h1234567_1  
gxx_linux-aarch64         11.2.0               h0c7b1b4_0  
ipython                   8.18.1             pyh707e725_3    conda-forge
jedi                      0.19.1           py39hd43f75c_0  
kernel-headers_linux-aarch64 4.18.0              h5b4a56d_16    conda-forge
ld_impl_linux-aarch64     2.38                 h8131f2d_1  
libffi                    3.4.4                h419075a_1  
libgcc                    14.1.0               he277a41_1    conda-forge
libgcc-devel_linux-aarch64 11.2.0               h1234567_1  
libgcc-ng                 14.1.0               he9431aa_1    conda-forge
libgfortran-ng            11.2.0               h6e398d7_1  
libgfortran5              11.2.0               h1234567_1  
libgomp                   14.1.0               he277a41_1    conda-forge
libllvm14                 14.0.6               hb8fdbf2_3  
libnsl                    2.0.1                h31becfc_0    conda-forge
libopenblas               0.3.21               hc2e42e2_0  
libsqlite                 3.46.0               hf51ef55_0    conda-forge
libstdcxx                 14.1.0               h3f4de04_1    conda-forge
libstdcxx-devel_linux-aarch64 11.2.0               h1234567_1  
libstdcxx-ng              14.1.0               hf1166c9_1    conda-forge
libuuid                   2.38.1               hb4cce97_0    conda-forge
libxcrypt                 4.4.36               h31becfc_1    conda-forge
libzlib                   1.2.13               h68df207_6    conda-forge
llvmlite                  0.43.0           py39h419075a_0  
matplotlib-inline         0.1.6            py39hd43f75c_0  
ncurses                   6.5                  hcccb83c_1    conda-forge
numba                     0.60.0           py39h419075a_0  
numpy                     1.26.4           py39he45c16d_0  
numpy-base                1.26.4           py39h15d264d_0  
openssl                   3.3.2                h86ecc28_0    conda-forge
pandas                    2.2.2            py39h60c7704_1    conda-forge
parso                     0.8.3              pyhd3eb1b0_0  
pexpect                   4.8.0              pyhd3eb1b0_3  
pickleshare               0.7.5           pyhd3eb1b0_1003  
pip                       24.2             py39hd43f75c_0  
prompt-toolkit            3.0.43           py39hd43f75c_0  
ptyprocess                0.7.0              pyhd3eb1b0_2  
pure_eval                 0.2.2              pyhd3eb1b0_0  
pygments                  2.15.1           py39hd43f75c_1  
python                    3.9.19          h4ac3b42_0_cpython    conda-forge
python-dateutil           2.9.0post0       py39hd43f75c_2  
python-tzdata             2023.3             pyhd3eb1b0_0  
python_abi                3.9                      5_cp39    conda-forge
pytz                      2024.1           py39hd43f75c_0  
readline                  8.2                  h998d150_0  
scipy                     1.13.1                   pypi_0    pypi
setuptools                72.1.0           py39hd43f75c_0  
six                       1.16.0             pyhd3eb1b0_1  
stack_data                0.2.0              pyhd3eb1b0_0  
sysroot_linux-aarch64     2.17                h5b4a56d_16    conda-forge
tbb                       2021.8.0             hb8fdbf2_0  
tk                        8.6.14               h987d8db_0  
traitlets                 5.14.3           py39hd43f75c_0  
typing_extensions         4.11.0           py39hd43f75c_0  
tzdata                    2024a                h04d1e81_0  
wcwidth                   0.2.5              pyhd3eb1b0_0  
wheel                     0.43.0           py39hd43f75c_0  
xz                        5.4.6                h998d150_1  
zlib                      1.2.13               h68df207_6    conda-forge

```

Installing cupy:
---------------

```bash
python -m pip install -U setuptools pip
conda install -c conda-forge cupy

```
