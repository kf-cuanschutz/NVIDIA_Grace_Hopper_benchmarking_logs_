Documentation:
================

* Let's measure GPU write to CPU DRAM as shown [here](https://docs.nvidia.com/grace-performance-tuning-guide.pdf)

  ```bash
  ink_c2c1_pmu_0^Cd_bytes_loc/,nvidia_nvlink_c2c1_pmu_0/wr_bytes_loc/}' ./nvbandwidth -t 1
a10-kfotso@a10-cuanschutz01:~/nvbandwidth/nvbandwidth$ sudo perf stat -a -e '{nvidia_nvlink_c2c0_pmu_0/total_bytes_loc/,nvidia_nvlink_c2c0_pmu_0/rd_bytes_loc/,nvidia_nvlink_c2c0_pmu_0/wr_bytes_loc/}','{nvidia_nvlink_c2c1_pmu_0/total_bytes_loc/,nvidia_nvlink_c2c1_pmu_0/rd_bytes_loc/,nvidia_nvlink_c2c1_pmu_0/wr_bytes_loc/}' ./nvbandwidth -t 1 
nvbandwidth Version: v0.5
Built from Git version: v0.5-1-g4da7d7e

NOTE: This tool reports current measured bandwidth on your system.
Additional system-specific tuning may be required to achieve maximal peak bandwidth.

CUDA Runtime Version: 12040
CUDA Driver Version: 12040
Driver Version: 550.54.15

Device 0: NVIDIA GH200 480GB

Running device_to_host_memcpy_ce.
memcpy CE CPU(row) <- GPU(column) bandwidth (GB/s)
           0
 0    272.94

SUM device_to_host_memcpy_ce 272.94


 Performance counter stats for 'system wide':

     4,234,722,816      nvidia_nvlink_c2c0_pmu_0/total_bytes_loc/                                      
       208,190,976      nvidia_nvlink_c2c0_pmu_0/rd_bytes_loc/                                      
     4,026,531,840      nvidia_nvlink_c2c0_pmu_0/wr_bytes_loc/                                      
        23,901,696      nvidia_nvlink_c2c1_pmu_0/total_bytes_loc/                                      
         6,145,280      nvidia_nvlink_c2c1_pmu_0/rd_bytes_loc/                                      
        17,756,416      nvidia_nvlink_c2c1_pmu_0/wr_bytes_loc/                                      

       0.631442915 seconds time elapsed
  ```

* Let's then measure GPU read from CPU DRAM:
```bash
a10-kfotso@a10-cuanschutz01:~/nvbandwidth/nvbandwidth$ sudo perf stat -a -e '{nvidia_nvlink_c2c0_pmu_0/total_bytes_loc/,nvidia_nvlink_c2c0_pmu_0/rd_bytes_loc/,nvidia_nvlink_c2c0_pmu_0/wr_bytes_loc/}','{nvidia_nvlink_c2c1_pmu_0/total_bytes_loc/,nvidia_nvlink_c2c1_pmu_0/rd_bytes_loc/,nvidia_nvlink_c2c1_pmu_0/wr_bytes_loc/}' ./nvbandwidth -t 0
nvbandwidth Version: v0.5
Built from Git version: v0.5-1-g4da7d7e

NOTE: This tool reports current measured bandwidth on your system.
Additional system-specific tuning may be required to achieve maximal peak bandwidth.

CUDA Runtime Version: 12040
CUDA Driver Version: 12040
Driver Version: 550.54.15

Device 0: NVIDIA GH200 480GB

Running host_to_device_memcpy_ce.
memcpy CE CPU(row) -> GPU(column) bandwidth (GB/s)
           0
 0    299.51

SUM host_to_device_memcpy_ce 299.51


 Performance counter stats for 'system wide':

     4,436,049,920      nvidia_nvlink_c2c0_pmu_0/total_bytes_loc/                                      
     4,234,723,328      nvidia_nvlink_c2c0_pmu_0/rd_bytes_loc/                                      
       201,326,592      nvidia_nvlink_c2c0_pmu_0/wr_bytes_loc/                                      
        23,938,048      nvidia_nvlink_c2c1_pmu_0/total_bytes_loc/                                      
         6,166,528      nvidia_nvlink_c2c1_pmu_0/rd_bytes_loc/                                      
        17,771,520      nvidia_nvlink_c2c1_pmu_0/wr_bytes_loc/                                      

       0.620030717 seconds time elapsed

```
