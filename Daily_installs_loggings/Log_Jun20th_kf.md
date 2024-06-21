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

