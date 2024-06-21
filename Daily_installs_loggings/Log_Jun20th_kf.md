Logs on June 20th:
==============================

* Installed NVIDIA parabricks:
```bash
apptainer pull docker://nvcr.io/nvidia/clara/clara-parabricks:4.1.0-1
```
* Installed Openmpi with the following commands:
```bash
sudo apt-get update
sudo apt install build-essential
sudo apt-get install openmpi-bin openmpi-doc libopenmpi-dev
```
Sources: https://webpages.charlotte.edu/abw/coit-grid01.uncc.edu/ParallelProgSoftware/Software/OpenMPIInstall.pdf; https://cgold.readthedocs.io/en/latest/first-step/installation.html
Note: I did get --> A kernel mismatch. Apparently the kernel version running is running behind the kernel version for openmpi-bin and it asked me to restart the system. I will load the screenshot of the error message.

* Installed cmake with the following commands:
```bash
sudo apt-get -y install cmake-qt-gui
```

* Created a Horovod Pytorch GPU ENV:
```bash
eval "$(/opt/miniconda3/bin/conda shell.bash hook)"
conda create --name Horovod_pytorch_gpu python=3.10
conda activate Horovod_pytorch_gpu
conda install pytorch torchvision pytorch-cuda=11.8 -c pytorch -c nvidia
```
Note: --> torchaudio was not available with aarch64 I got the following below when including torchaudio into the list of packages to install:

```bash
Channels:
 - pytorch
 - nvidia
 - defaults
Platform: linux-aarch64
Collecting package metadata (repodata.json): done
Solving environment: failed

PackagesNotFoundError: The following packages are not available from current channels:

  - torchaudio

Current channels:

  - https://conda.anaconda.org/pytorch
  - https://conda.anaconda.org/nvidia
  - defaults

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.
```
* Installing CUDNN:
  
```bash
conda install -c conda-forge cudnn
```

* Installing Cudatoolkit:

```bash
conda install -c "nvidia/label/cuda-11.8.0" cuda-toolkit 
```

* Installed gxx:
```bash
 conda install conda-forge::gxx_linux-64
```

* Downloaded NCCL from https://developer.nvidia.com/nccl:
```bash
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/sbsa/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt-get update
sudo apt install libnccl2=2.16.2-1+cuda11.8 libnccl-dev=2.16.2-1+cuda11.8 
```

* Gave the path to libnccl

```bash
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/aarch64-linux-gnu
```

* Tried to build Horovod with:

```bash
CC=mpicc CXX=mpicxx  CMAKE=1 HOROVOD_WITH_MPI=1 HOROVOD_WITH_PYTORCH=1 HOROVOD_GPU_ALLREDUCE=MPI HOROVOD_GPU_OPERATIONS=NCCL   pip install --no-cache-dir  horovod[pytorch]

```

But failed 
```bash E
Assembler messages:
      Error: unknown architecture `nocona'

      Error: unrecognized option -march=nocona
      cc1plus: error: unknown value ‘nocona’ for ‘-march’
      cc1plus: note: valid arguments are: armv8-a armv8.1-a armv8.2-a armv8.3-a armv8.4-a armv8.5-a armv8.6-a armv8-r native
      cc1plus: error: unknown value ‘haswell’ for ‘-mtune’
```
I tried
`apt-get install -y g++-aarch64-linux-gnu```

I also tried to build Horovod without HOROVOD_GPU_ALLREDUCE=MPI and/or CC=mpicc CXX=mpicxx  but it did not work. I might be better off using Pytorch lightning.

* Installed spack with the following commands:

```bash
sudo apt update
sudo apt install build-essential ca-certificates coreutils curl environment-modules gfortran git gpg lsb-release python3 python3-distutils python3-venv unzip zip
git clone -c feature.manyFiles=true https://github.com/spack/spack.git
. spack/share/spack/setup-env.sh
```

However installs of even simple packages like zlib seem to not work. Got the following error
```bash
==> gmake: Executing phase: 'install'
==> [2024-06-21-04:02:05.362046] '/tmp/a10-kfotso/spack-stage/spack-stage-gmake-4.4.1-tiqzp6vofv6jm7zktwnv3ibu6n2sr24t/spack-src/configure' '--prefix=/home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-12.3.0/gmake-4.4.1-tiqzp6vofv6jm7zktwnv3ibu6n2sr24t' '--without-guile' '--disable-nls' '--disable-dependency-tracking'
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a race-free mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking whether make supports the include directive... yes (GNU style)
checking for gcc... /home/a10-kfotso/spack/spack/lib/spack/env/c++
checking whether the C compiler works... no
configure: error: in `/tmp/a10-kfotso/spack-stage/spack-stage-gmake-4.4.1-tiqzp6vofv6jm7zktwnv3ibu6n2sr24t/spack-src/spack-build':
configure: error: C compiler cannot create executables
See `config.log' for more details
```

* I installed lua with the following as shown [here](https://lmod.readthedocs.io/en/latest/030_installing.html):

```bash
wget https://sourceforge.net/projects/lmod/files/lua-5.1.4.9.tar.bz2
tar xf lua-5.1.4.9.tar.bz2
cd lua-5.1.4.9/
sudo make;sudo make install
cd /opt/apps/lua; 
sudo ln -s 5.1.4.9 lua
sudo mkdir /usr/local/bin; sudo ln -s /opt/apps/lua/lua/bin/lua /usr/local/bin
```




