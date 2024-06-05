Logs on May 30th and Jun 4th:
==============================

* Installed apptainer
```bash
sudo add-apt-repository -y ppa:apptainer/ppa
sudo apt update
sudo apt install -y apptainer
```
  
* Installed nvtop 3.1.0 from Maxime Schmitt (razortealeaf)

```bash
sudo snap install nvtop
```
* Installed tensorflow:
```bash
apptainer pull nvcr_tf.sif docker://nvcr.io/nvidia/tensorflow:24.05-tf2-py3-igpu
```
* Installed screen"
```bash
sudo apt install screen
```

* Installed pytorch
```bash
apptainer pull pytorch.sif docker://nvcr.io/nvidia/pytorch:24.05-py3
```

* Installing NVIDIA Rapids:

```bash
apptainer pull nvidia_rapids_.sif docker://nvcr.io/nvidia/rapidsai/base:24.04-cuda12.2-py3.11
```

* Installing cupy:
```bash
 apptainer pull cupy_.sif docker://cupy/cupy
```

* Installing miniconda3. Fetched it [here](https://docs.anaconda.com/free/miniconda/)
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh
chmod +x Miniconda3-latest-Linux-aarch64.sh
sudo bash Miniconda3-latest-Linux-aarch64.sh
```

Path is "/opt/miniconda3"

Got the following log:


```bash
Do you wish to update your shell profile to automatically initialize conda?
This will activate conda on startup and change the command prompt when activated.
If you'd prefer that conda's base environment not be activated on startup,
   run the following command when conda is activated:

conda config --set auto_activate_base false

You can undo this by running `conda init --reverse $SHELL`? [yes|no]
[no] >>> 

You have chosen to not have conda modify your shell scripts at all.
To activate conda's base environment in your current shell session:

eval "$(/opt/miniconda3/bin/conda shell.YOUR_SHELL_NAME hook)" 

To install conda's shell functions for easier access, first activate, then:

conda init
```

* Installing of mamba cuda, nvprof and nsight toolkit:

```bash
eval "$(/opt/miniconda3/bin/conda shell.bash hook)"
conda create -n cuda_env python=3.9
onda activate cuda_env
conda install -c "nvidia/label/cuda-11.8.0" cuda-toolkit
conda install nvidia::cuda-nvprof -y
conda install nvidia::nsight-compute -y
conda install numba -y
```

* Containers images were copied to
```bash
/opt/containers_img
```
