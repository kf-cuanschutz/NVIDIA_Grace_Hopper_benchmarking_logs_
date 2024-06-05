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
 
