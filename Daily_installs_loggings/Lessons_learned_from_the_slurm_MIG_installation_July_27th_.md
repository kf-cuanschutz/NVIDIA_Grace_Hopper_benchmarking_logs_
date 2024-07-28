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

* We had to clone the mig discovery github repo.
```bash
a10-kfotso@a10-cuanschutz01:~/mig_discovery$ git clone https://gitlab.com/nvidia/hpc/slurm-mig-discovery.git
Cloning into 'slurm-mig-discovery'...
remote: Enumerating objects: 7, done.
remote: Total 7 (delta 0), reused 0 (delta 0), pack-reused 7 (from 1)
Receiving objects: 100% (7/7), 8.07 KiB | 8.07 MiB/s, done.
Resolving deltas: 100% (1/1), done.
a10-kfotso@a10-cuanschutz01:~/mig_discovery$ cd slurm-mig-discovery
a10-kfotso@a10-cuanschutz01:~/mig_discovery/slurm-mig-discovery$ sudo gcc -g -o mig -I/usr/local/cuda/include -I/usr/cuda/include mig.c -lnvidia-ml
a10-kfotso@a10-cuanschutz01:~/mig_discovery/slurm-mig-discovery$ sudo ./mig
GPU count 1
Success
```

* We did not have to install ```slurm-slurmd```. We could not locate it with apt anyway.

* We had to make sure to chown all the .conf files to ```slurm:slurm```. It was really an important step

* We had to enable munge.

```bash
root@a10-cuanschutz01:~# cp /etc/munge/munge.key /sched/
root@a10-cuanschutz01:~# chown munge:munge /sched/munge.key
root@a10-cuanschutz01:~# chmod 400 /sched/munge.key
root@a10-cuanschutz01:~# cp /sched/munge.key /etc/slurm/
root@a10-cuanschutz01:~# cp /sched/munge.key /etc/slurm-llnl/
root@a10-cuanschutz01:~# systemctl restart munge
root@a10-cuanschutz01:~# systemctl enable munge
Synchronizing state of munge.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable munge
```
  
* We created a directory ``` /sched/```. We created the file ```/sched/cgroup.conf```. We also created the files accounting.conf, gres.conf, partition.conf, cgroup.conf and cgroup_allowed_devices_file.conf. 

* We made sure to copy them to /etc/slurm and /etc/slurm-llnl.  For more information please refer to all the configuration files that we uploaded [here](https://github.com/kf-cuanschutz/NVIDIA_Grace_Hopper_benchmarking_logs_/tree/main/Daily_installs_loggings/all_final_slurm_mig_config_files_)

* A lot of trial and error were necessary and the commands below were alwauys very useful:

```bash
systemctl restart slurmctld;systemctl enable slurmctld;systemctl restart slurmd;systemctl enable slurmd
```

```bash
slurmctld -D
```

```bash
scontrol update nodename=localhost state=idle
```

* We had to create a mount point for the cgroup.

```bash
root@a10-cuanschutz01:/sched# 

echo CgroupMountpoint=/sys/fs/cgroup >> /etc/slurm-llnl/cgroup.conf
root@a10-cuanschutz01:/sched# 

echo CgroupMountpoint=/sys/fs/cgroup >> /etc/slurm/cgroup.conf
root@a10-cuanschutz01:/sched# ls /sys/fs/cgroup^C
root@a10-cuanschutz01:/sched# 

echo CgroupMountpoint=/sys/fs/cgroup >> /sched/cgroup.conf
root@a10-cuanschutz01:/sched# cat cgroup.conf 
CgroupAutomount=yes
ConstrainCores=no
ConstrainRamSpace=no
ConstrainDevices=yes
CgroupMountpoint=/sys/fs/cgroup
root@a10-cuanschutz01:/sched# systemctl restart slurmctld;systemctl enable slurmctld;systemctl restart slurmd;systemctl enable slurmd
Synchronizing state of slurmctld.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable slurmctld
Synchronizing state of slurmd.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable slurmd

```

```bash
apt install cgroupfs-mount
cgroupfs-mount
```

* Finally, the following slurm commands are very useful for debugging purposes:

```bash
slurmd -C
slurmctld -D
sudo tail var/log/slurm/slurmd.log
scontrol update nodename=localhost state=resume
```

* [This](https://gitlab.com/nvidia/hpc/slurm-mig-discovery) was a helpful link as well.

