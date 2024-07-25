Installed numactl:
==================

```bash
sudo apt install numactl
```
Installed nvbandwitdth with the following below:
```bash
git clone https://github.com/NVIDIA/nvbandwidth.git
spack load cuda
sudo apt update
sudo apt install libboost-program-options-dev
./debian_install.sh 
```

[ccc](https://github.com/greenelab/ccc) seems to port quite well on Grace:
```bash
eval "$(/opt/miniconda3/bin/conda shell.bash hook)"
conda create -y -n ccc-env python=3.9 ipython pandas
conda activate ccc-env
 pip install ccc-coef
ipython
```
