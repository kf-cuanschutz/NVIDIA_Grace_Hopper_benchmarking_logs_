Compiling the lessons learned from the Slurm MIG Installation:
--------------------------------------------------------------

* The main guide that was used to achieve this was [here](https://techcommunity.microsoft.com/t5/azure-high-performance-computing/creating-a-slurm-cluster-for-scheduling-nvidia-mig-based-gpu/ba-p/4183835). 
Because we are working only on a single node, some steps had to be skipped. We will go over that a little later.

* We first followed the NVIDIA guide on MIG to assess the gpu partitioning with nvidia-smi. Partitioning here means the action of creating seperate GPU instances composed of their own unique paths to the DRAM, the L2 cache, memory controllers etc ...
  The full guide can be found [here](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html).

* We first enabled the MIG mode

```bash
a10-kfotso@a10-cuanschutz01:~/spack$ sudo nvidia-smi -mig 1
Enabled MIG Mode for GPU 00000009:01:00.0

Warning: persistence mode is disabled on device 00000009:01:00.0. See the Known Issues section of the nvidia-smi(1) man page for more information. Run with [--help | -h] switch to get more information on how to enable persistence mode.
All done.
```

* We enabled the persistent mode then disabled it. Refer to the helpful thread [here](https://forums.developer.nvidia.com/t/nvidia-persistenced-failed-to-initialize-check-syslog-for-more-details/74052/4)

```bash
root@a10-cuanschutz01:~# nvidia-smi -pm 1
Persistence mode is already Enabled for GPU 00000009:01:00.0.
All done.
```

Note that to disable the persistent mode, one may run ```nvidia-smi -pm 0``` . You may refer to this [guide](https://docs.nvidia.com/deploy/driver-persistence/index.html#persistence-daemon) from NVIDIA.
We did disable the persistent mode in the end.

```bash
root@a10-cuanschutz01:~# nvidia-smi -pm 0
Disabled persistence mode for GPU 00000009:01:00.0.
All done.
```

* We listed all the instances profiles. Please see below.

```bash
a10-kfotso@a10-cuanschutz01:~$ nvidia-smi mig -lgip
+-----------------------------------------------------------------------------+
| GPU instance profiles:                                                      |
| GPU   Name             ID    Instances   Memory     P2P    SM    DEC   ENC  |
|                              Free/Total   GiB              CE    JPEG  OFA  |
|=============================================================================|
|   0  MIG 1g.12gb       19     7/7        11.00      No     16     1     0   |
|                                                             1     1     0   |
+-----------------------------------------------------------------------------+
|   0  MIG 1g.12gb+me    20     1/1        11.00      No     16     1     0   |
|                                                             1     1     1   |
+-----------------------------------------------------------------------------+
|   0  MIG 1g.24gb       15     4/4        23.00      No     26     1     0   |
|                                                             1     1     0   |
+-----------------------------------------------------------------------------+
|   0  MIG 2g.24gb       14     3/3        23.00      No     32     2     0   |
|                                                             2     2     0   |
+-----------------------------------------------------------------------------+
|   0  MIG 3g.48gb        9     2/2        46.50      No     60     3     0   |
|                                                             3     3     0   |
+-----------------------------------------------------------------------------+
|   0  MIG 4g.48gb        5     1/1        46.50      No     64     4     0   |
|                                                             4     4     0   |
+-----------------------------------------------------------------------------+
|   0  MIG 7g.96gb        0     1/1        93.00      No     132    7     0   |
|                                                             8     7     1   |
+-----------------------------------------------------------------------------+

```

* Before creating all the instances, we had to kill all the profiles PID

```bash
root@a10-cuanschutz01:~# sudo fuser -v /dev/nvidia*
                     USER        PID ACCESS COMMAND
/dev/nvidia0:        root      1484778 F...m nsys
/dev/nvidiactl:      root      1484778 F.... nsys
/dev/nvidia-uvm:     root      1484778 F.... nsys
root@a10-cuanschutz01:~# nvidia-smi mig -cgi 20,20,20,20,20,20,20,20 -C
Unable to create a GPU instance on GPU  0 using profile 20: In use by another client
Failed to create GPU instances: In use by another client
root@a10-cuanschutz01:~# kill 1484778
```

* From the instance profiles, we created the actual instances. Be careful to make sure that you have enough resources and that you are not using saturated profiles !!! See below.
  In that case, profile 20 was saturated.

```bash
root@a10-cuanschutz01:~# nvidia-smi mig -cgi 20,20,20 -C
Unable to create a GPU instance on GPU  0 using profile 20: Insufficient Resources
Failed to create GPU instances: Insufficient Resources
```

* We therefore decided to use profile 15 instead.
```bash
root@a10-cuanschutz01:~# nvidia-smi mig -cgi 15,15,15 -C
Successfully created GPU instance ID  5 on GPU  0 using profile MIG 1g.24gb (ID 15)
Successfully created compute instance ID  0 on GPU  0 GPU instance ID  5 using profile MIG 1g.24gb (ID  7)
Successfully created GPU instance ID  3 on GPU  0 using profile MIG 1g.24gb (ID 15)
Successfully created compute instance ID  0 on GPU  0 GPU instance ID  3 using profile MIG 1g.24gb (ID  7)
Successfully created GPU instance ID  4 on GPU  0 using profile MIG 1g.24gb (ID 15)
Successfully created compute instance ID  0 on GPU  0 GPU instance ID  4 using profile MIG 1g.24gb (ID  7)

```
  
* We created a directory ``` /sched/```. We created the file ```/sched/cgroup.conf```. We also created the files accounting.conf, gres.conf, partition.conf, cgroup.conf and cgroup_allowed_devices_file.conf. 

* We made sure to copy them to /etc/slurm and /etc/slurm-llnl.  For more information please refer to all the configuration files that we uploaded [here](https://github.com/kf-cuanschutz/NVIDIA_Grace_Hopper_benchmarking_logs_/tree/main/Daily_installs_loggings/all_final_slurm_mig_config_files_)




