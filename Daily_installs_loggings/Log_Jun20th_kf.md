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




