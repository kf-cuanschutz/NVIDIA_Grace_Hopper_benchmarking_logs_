## Description:
----------------

The Grace Hopper system is made of an ARM CPU part and a Hopper architechture part.

* CPU part, NUMA architechture with 1 socket and 72 cores per socket. The system is split into 8 NUMA nodes, but we only have access to NUMA0 which enables a connection to the Hopper GPU part.
* CPU max Frequency is 3,483 MHz and 81 MHz min Frequency.
* The system has about 480G CPU RAM
* Here is a link to the CPU [model](https://www.arm.com/products/silicon-ip-cpu/neoverse/neoverse-v2)
* According to nvidia-smi, the GPU chip is  NVIDIA GH200 with global memory 574.5GB.
* The OS distribution is Ubuntu 22.04.4 and the kernel is 6.5.0-1019-nvidia-64k, suitable for the arm64 architecture.

Link to Hopper CUDA gencode --> [90](https://arnon.dk/matching-sm-architectures-arch-and-gencode-for-various-nvidia-cards/)

A technical description of the Hopper architechture --> [here](https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/)


[1] Further links to nvidia-smi: https://developer.download.nvidia.com/compute/DCGM/docs/nvidia-smi-367.38.pdf

[2] More information on Grace-Hopper here [1](https://extremecomputingtraining.anl.gov/wp-content/uploads/sites/96/2023/08/ATPESC-2023-Track-1-Talk-4-Giri-Nvidia-Grace-Hopper-1.pdf) , [2](https://developer.nvidia.com/grace-cpu), [3](https://www.nvidia.com/en-us/on-demand/session/gtcspring22-s41788/)  

