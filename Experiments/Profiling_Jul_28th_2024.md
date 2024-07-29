


I was getting this error when trying to use ncu

```bash
(cuda_env) root@a10-cuanschutz01:/home/a10-kfotso/benchmarking_/Pi_numba_cuda_project_/gpu_programming_December_2023# srun -p gpu --gres=gpu:1 /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/nvhpc-24.5-lwy544yxfvbzqufhsdp5mubg2swkt74j/Linux_aarch64/2024/profilers/Nsight_Compute/ncu --set detailed -o out_filename_ncu python calculate_pi_gpu_opt_clean_float64.py 1000
==PROF== Connected to process 2119298 (/home/a10-kfotso/.conda/envs/cuda_env/bin/python3.9)
==WARNING== Unable to access the following 8 metrics: pcie__read_bytes.avg.per_second, pcie__read_bytes.max.per_second, pcie__read_bytes.min.per_second, pcie__read_bytes.sum.per_second, pcie__write_bytes.avg.per_second, pcie__write_bytes.max.per_second, pcie__write_bytes.min.per_second, pcie__write_bytes.sum.per_second. If profiling on a MIG instance, it is not possible to collect metrics from GPU units that are shared with other MIG instances.

==PROF== Profiling "v1,cw51cXTLSUwv1sCUt9Ww1FEw0N..." - 0: 0%
==ERROR== An error was reported by the driver

==ERROR== Cannot lock GPU clock frequencies on MIG! Try locking the clocks externally (e.g. using 'nvidia-smi --lock-gpu-clocks=tdp,tdp') or profile without fixed frequencies (see '--clock-control').
==ERROR== Failed to profile "v1,cw51cXTLSUwv1sCUt9Ww1FEw0N..." in process 2119298
==PROF== Trying to shutdown target application
==ERROR== The application returned an error code (9).
==ERROR== An error occurred while trying to profile.
==WARNING== No kernels were profiled.
srun: error: localhost: task 0: Exited with exit code 9
```

Thus, I did the following below:

```bash
nvidia-smi --lock-gpu-clocks=tdp,tdp
(cuda_env) root@a10-cuanschutz01:/home/a10-kfotso/benchmarking_/Pi_numba_cuda_project_/gpu_programming_December_2023# nvidia-smi --lock-gpu-clocks=tdp,tdp
GPU clocks set to "(gpuClkMin tdp, gpuClkMax tdp)" for GPU 00000009:01:00.0

Warning: persistence mode is disabled on device 00000009:01:00.0. See the Known Issues section of the nvidia-smi(1) man page for more information. Run with [--help | -h] switch to get more information on how to enable persistence mode.
All done.
````

I decided to reset the clocks:

```bash
(cuda_env) root@a10-cuanschutz01:/home/a10-kfotso/benchmarking_/Pi_numba_cuda_project_/gpu_programming_December_2023# nvidia-smi --reset-gpu-clocks
All done.
```

I am not able to use ncu when the MIG is activate I tried different ways but it is not working. I might have to rever the MIG for now:

```bash
(cuda_env) root@a10-cuanschutz01:/home/a10-kfotso/benchmarking_/Pi_numba_cuda_project_/gpu_programming_December_2023# nvidia-smi -mig 0
Unable to disable MIG Mode for GPU 00000009:01:00.0: In use by another client
Terminating early due to previous errors.
```

This is strange because when I try to see all of the processes that are running I see none:

```bash
(cuda_env) root@a10-cuanschutz01:/home/a10-kfotso/benchmarking_/Pi_numba_cuda_project_/gpu_programming_December_2023# fuser -v /dev/nvidia*
```

I saw this issue as well that seems to confirm [it](https://github.com/NVIDIA/gpu-operator/issues/118)

Let's try to kill process 2263460?

```bash
(cuda_env) root@a10-cuanschutz01:/home/a10-kfotso/benchmarking_/Pi_numba_cuda_project_/gpu_programming_December_2023# ls /proc/*/fd/* -l | grep /dev/nvidi
ls: cannot access '/proc/2263460/fd/255': No such file or directory
ls: cannot access '/proc/2263460/fd/3': No such file or directory
ls: cannot access '/proc/self/fd/255': No such file or directory
ls: cannot access '/proc/self/fd/3': No such file or directory
ls: cannot access '/proc/thread-self/fd/255': No such file or directory
ls: cannot access '/proc/thread-self/fd/3': No such file or directory
```
It looks like it did not work.
