Usage of NCU:
------------

* I am getting a "The user does not have permission to access NVIDIA GPU Performance Counters on the target device 0." when running ncu. Please see below:

```bash
(cuda_env) a10-kfotso@a10-cuanschutz01:~/benchmarking_/Pi_numba_cuda_project_/gpu_programming_December_2023$ ncu python calculate_pi_gpu_opt_clean_float64.py 10000000
==PROF== Connected to process 1314148 (/home/a10-kfotso/.conda/envs/cuda_env/bin/python3.9)
==ERROR== ERR_NVGPUCTRPERM - The user does not have permission to access NVIDIA GPU Performance Counters on the target device 0. For instructions on enabling permissions and to get more information see https://developer.nvidia.com/ERR_NVGPUCTRPERM
/home/a10-kfotso/benchmarking_/Pi_numba_cuda_project_/gpu_programming_December_2023/calculate_pi_gpu_opt_clean_float64.py:76: DeprecationWarning: Conversion of an array with ndim > 0 to a scalar is deprecated, and will error in future. Ensure you extract a single element from your array before performing this operation. (Deprecated NumPy 1.25.)
  print("Pi = %.20f, (Diff=%.20f) (calculated in %f secs with %d steps)" %(pi, pi-np.pi, end-start, step_vec.shape[0]))
Pi = 3.14159265358979045146, (Diff=-0.00000000000000266454) (calculated in 0.413071 secs with 10000000 steps)
==PROF== Disconnected from process 1314148
==WARNING== No kernels were profiled.
```

I went to this [link](https://developer.nvidia.com/ERR_NVGPUCTRPERM). Below is what I tried:

```bash
(cuda_env) a10-kfotso@a10-cuanschutz01:~/benchmarking_/Pi_numba_cuda_project_/gpu_programming_December_2023$ sudo modprobe nvidia NVreg_RestrictProfilingToAdminUsers=1
(cuda_env) a10-kfotso@a10-cuanschutz01:~/benchmarking_/Pi_numba_cuda_project_/gpu_programming_December_2023$ sudo systemctl isolate multi-user
(cuda_env) a10-kfotso@a10-cuanschutz01:~/benchmarking_/Pi_numba_cuda_project_/gpu_programming_December_2023$ sudo modprobe -rf nvidia_uvm nvidia_drm nvidia_modeset nvidia-vgpu-vfio nvidia
modprobe: FATAL: Module nvidia-vgpu-vfio not found.
(cuda_env) a10-kfotso@a10-cuanschutz01:~/benchmarking_/Pi_numba_cuda_project_/gpu_programming_December_2023$ sudo modprobe nvidia NVreg_RestrictProfilingToAdminUsers=1
(cuda_env) a10-kfotso@a10-cuanschutz01:~/benchmarking_/Pi_numba_cuda_project_/gpu_programming_December_2023$ sudo systemctl isolate graphical
(cuda_env) a10-kfotso@a10-cuanschutz01:~/benchmarking_/Pi_numba_cuda_project_/gpu_programming_December_2023$ ncu python calculate_pi_gpu_opt_clean_float64.py 10000000
==PROF== Connected to process 1314148 (/home/a10-kfotso/.conda/envs/cuda_env/bin/python3.9)
==ERROR== ERR_NVGPUCTRPERM - The user does not have permission to access NVIDIA GPU Performance Counters on the target device 0. For instructions on enabling permissions and to get more information see https://developer.nvidia.com/ERR_NVGPUCTRPERM
/home/a10-kfotso/benchmarking_/Pi_numba_cuda_project_/gpu_programming_December_2023/calculate_pi_gpu_opt_clean_float64.py:76: DeprecationWarning: Conversion of an array with ndim > 0 to a scalar is deprecated, and will error in future. Ensure you extract a single element from your array before performing this operation. (Deprecated NumPy 1.25.)
  print("Pi = %.20f, (Diff=%.20f) (calculated in %f secs with %d steps)" %(pi, pi-np.pi, end-start, step_vec.shape[0]))
Pi = 3.14159265358979045146, (Diff=-0.00000000000000266454) (calculated in 0.413071 secs with 10000000 steps)
==PROF== Disconnected from process 1314148
==WARNING== No kernels were profiled.
```

No success yet.

I tried to log into the system as root and created a file ```/etc/modprobe.d/nvidia-prof-access.conf``` with the following inside ```options nvidia NVreg_RestrictProfilingToAdminUsers=0```. Then I ran the following below:

```bash
(cuda_env) a10-kfotso@a10-cuanschutz01:~/benchmarking_/Pi_numba_cuda_project_/gpu_programming_December_2023$ sudo update-initramfs -u -k all
update-initramfs: Generating /boot/initrd.img-6.5.0-1023-nvidia-64k
W: Possible missing firmware /lib/firmware/ast_dp501_fw.bin for module ast
update-initramfs: Generating /boot/initrd.img-6.5.0-1019-nvidia-64k
W: Possible missing firmware /lib/firmware/ast_dp501_fw.bin for module ast
update-initramfs: Generating /boot/initrd.img-6.5.0-44-generic
W: Possible missing firmware /lib/firmware/ast_dp501_fw.bin for module ast

```

A restart might be necessary  unfortunately.


