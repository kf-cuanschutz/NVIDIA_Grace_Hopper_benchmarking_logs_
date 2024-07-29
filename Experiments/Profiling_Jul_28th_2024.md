


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

Looks like I found the culprit?

```bash
(cuda_env) root@a10-cuanschutz01:/home/a10-kfotso/benchmarking_/Pi_numba_cuda_project_/gpu_programming_December_2023# lsof | grep -i nvidia
systemd-u    1119                               root  mem       REG              252,0    23209   41812296 /usr/lib/modules/6.5.0-1019-nvidia-64k/modules.builtin.bin
systemd-u    1119                               root  mem       REG              252,0   909157   41812286 /usr/lib/modules/6.5.0-1019-nvidia-64k/modules.symbols.bin
systemd-u    1119                               root  mem       REG              252,0  1927237   41812283 /usr/lib/modules/6.5.0-1019-nvidia-64k/modules.alias.bin
systemd-u    1119                               root  mem       REG              252,0  1169980   41812282 /usr/lib/modules/6.5.0-1019-nvidia-64k/modules.dep.bin
systemd-u    1119                               root  mem       REG              252,0    49215   41812297 /usr/lib/modules/6.5.0-1019-nvidia-64k/modules.builtin.alias.bin
nvidia-mo 1484769                               root  cwd       DIR              252,0     4096          2 /
nvidia-mo 1484769                               root  rtd       DIR              252,0     4096          2 /
nvidia-mo 1484769                               root  txt   unknown                                        /proc/1484769/exe
nvidia-mo 1484770                               root  cwd       DIR              252,0     4096          2 /
nvidia-mo 1484770                               root  rtd       DIR              252,0     4096          2 /
nvidia-mo 1484770                               root  txt   unknown                                        /proc/1484770/exe
nvidia-pe 1984422                               root  cwd       DIR              252,0     4096          2 /
nvidia-pe 1984422                               root  rtd       DIR              252,0     4096          2 /
nvidia-pe 1984422                               root  txt       REG              252,0   195976   41718137 /usr/bin/nvidia-persistenced
nvidia-pe 1984422                               root  mem       REG              252,0     6240   41681700 /usr/lib/aarch64-linux-gnu/librt.so.1
nvidia-pe 1984422                               root  mem       REG              252,0   390808   41718167 /usr/lib/aarch64-linux-gnu/libnvidia-cfg.so.550.54.15
nvidia-pe 1984422                               root  mem       REG              252,0  1637400   41681454 /usr/lib/aarch64-linux-gnu/libc.so.6
nvidia-pe 1984422                               root  mem       REG              252,0    13752   41681697 /usr/lib/aarch64-linux-gnu/libpthread.so.0
nvidia-pe 1984422                               root  mem       REG              252,0     6152   41681529 /usr/lib/aarch64-linux-gnu/libdl.so.2
nvidia-pe 1984422                               root  mem       REG              252,0   187776   41680960 /usr/lib/aarch64-linux-gnu/ld-linux-aarch64.so.1
nvidia-pe 1984422                               root    0u     unix 0xffff005a73b65d80      0t0    3448369 type=DGRAM
nvidia-pe 1984422                               root    1uW     REG               0,26        8     251658 /run/nvidia-persistenced/nvidia-persistenced.pid
nvidia-pe 1984422                               root    2r      DIR               0,23        0    1633844 /sys/bus/pci/drivers/nvidia
nvidia-pe 1984422                               root    9u     unix 0xffff005a73b60880      0t0    3448370 /var/run/nvidia-persistenced/socket type=STREAM
```
