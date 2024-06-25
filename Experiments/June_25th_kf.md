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
