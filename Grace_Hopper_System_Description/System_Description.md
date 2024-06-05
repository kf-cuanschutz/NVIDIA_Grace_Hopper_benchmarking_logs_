## Description:
----------------

The Grace Hopper system is made of an ARM CPU part and a Hopper architechture part.

* CPU part, NUMA architechture with 1 socket and 72 cores per socket. The system is split into 8 NUMA nodes, but we only have access to NUMA0 which enables a connection to the Hopper GPU part.
* CPU max Frequency is 3,483 MHz and 81 MHz min Frequency.
* The system has about 480G CPU RAM
* Here is a link to the CPU [model](https://www.arm.com/products/silicon-ip-cpu/neoverse/neoverse-v2)
* According to nvidia-smi, the GPU chip is  NVIDIA GH200 with global memory 480GB.


[1] Further links to nvidia-smi: https://developer.download.nvidia.com/compute/DCGM/docs/nvidia-smi-367.38.pdf

[2] More information on Grace-Hopper: https://extremecomputingtraining.anl.gov/wp-content/uploads/sites/96/2023/08/ATPESC-2023-Track-1-Talk-4-Giri-Nvidia-Grace-Hopper-1.pdf
