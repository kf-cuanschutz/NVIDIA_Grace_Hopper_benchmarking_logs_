### Install logs:
------------------

* The goal is to install HPL-cuda from (https://github.com/avidday/hpl-cuda)[here] so that we can do benchmarking.

* Installed mpich with the following:

```bash
 sudo apt install mpich
```

* Installed Go2blas with the following:

```bash
sudo apt-get install libopenblas-dev
```

* I activate my cuda environment which already has all the installed cublas related libraries:
  ```bash
  eval "$(/opt/miniconda3/bin/conda shell.bash hook)"
  conda activate cuda_env
  find /home/a10-kfotso/.conda/envs/cuda_env | grep -i cublas
  /home/a10-kfotso/.conda/envs/cuda_env/conda-meta/libcublas-dev-11.11.3.6-0.json
  /home/a10-kfotso/.conda/envs/cuda_env/conda-meta/libcublas-11.11.3.6-0.json
  /home/a10-kfotso/.conda/envs/cuda_env/include/cublasXt.h
  /home/a10-kfotso/.conda/envs/cuda_env/include/cublas_api.h
  /home/a10-kfotso/.conda/envs/cuda_env/include/cublasLt.h
  /home/a10-kfotso/.conda/envs/cuda_env/include/cublas.h
  /home/a10-kfotso/.conda/envs/cuda_env/include/cublas_v2.h
  /home/a10-kfotso/.conda/envs/cuda_env/lib/libcublasLt.so.11
  /home/a10-kfotso/.conda/envs/cuda_env/lib/libcublasLt_static.a
  /home/a10-kfotso/.conda/envs/cuda_env/lib/libcublas_static.a
  /home/a10-kfotso/.conda/envs/cuda_env/lib/libcublas.so
  /home/a10-kfotso/.conda/envs/cuda_env/lib/libcublas.so.11.11.3.6
  /home/a10-kfotso/.conda/envs/cuda_env/lib/stubs/libcublas.so
  /home/a10-kfotso/.conda/envs/cuda_env/lib/stubs/libcublasLt.so
  /home/a10-kfotso/.conda/envs/cuda_env/lib/libcublas.so.11
  /home/a10-kfotso/.conda/envs/cuda_env/lib/libcublasLt.so
  /home/a10-kfotso/.conda/envs/cuda_env/lib/libcublasLt.so.11.11.3.6
  ```

  * Installing cmkae with snap does not work ```sudo snap install cmake```. However the following worked
    ```bash
    sudo apt  install cmake-curses-gui
    ```

 * It looks like I can get an HPL container here: https://catalog.ngc.nvidia.com/orgs/nvidia/containers/hpc-benchmarks
   Currently building it with the following below:

   ```bash
   apptainer build  hpc-benchmarks:24.06.sif  docker://nvcr.io/nvidia/hpc-benchmarks:24.06
   ```
 * I installed slurm following this [guide](https://drtailor.medium.com/how-to-setup-slurm-on-ubuntu-20-04-for-single-node-work-scheduling-6cc909574365). For the slurm.conf file, I entered 72 CPUs and 480G memory. Also, the slurm.conf file had to be created under "/etc/slurm/" in lieu of "/etc/slurm-llnl" for it to work. I applied the permission "755" on /etc/slurm/ as well.

* I had to follow this [guide](https://nekodaemon.com/2022/09/02/Slurm-Quick-Installation-for-Cluster-on-Ubuntu-20-04/) as well. But I was still getting issues when trying to start slurmctld. Running the following below allowed me to see that I had to create the "/var/lib/slurm-llnl" and "/var/lib/slurm-llnl/slurmctld" directories. I also changed the owner of "/var/lib/slurm-llnl" directories and change permissions.

```bash
 sudo slurmctld -D
sudo mkdir -vp /var/lib/slurm-llnl/slurmctld
sudo mkdir -pv /var/lib/slurm-llnl/slurmd
sudo chown slurm:slurm /var/lib/slurm-llnl
sudo chown slurm:slurm /var/lib/slurm-llnl/slurmctld
sudo chmod 755 /var/lib/slurm-llnl
sudo chmod 755 /var/lib/slurm-llnl/slurmctld
sudo chmod 755 /var/lib/slurm-llnl/slurmd
```

Current output after making all of those edits for slurm:

```bash
(cuda_env) a10-kfotso@a10-cuanschutz01:~/slurm$ sudo slurmctld -D
slurmctld: error: Configured MailProg is invalid
slurmctld: slurmctld version 21.08.5 started on cluster localcluster
slurmctld: No memory enforcing mechanism configured.
slurmctld: Recovered state of 1 nodes
slurmctld: Recovered information about 0 jobs
slurmctld: select/cons_tres: part_data_create_array: select/cons_tres: preparing for 1 partitions
slurmctld: Recovered state of 0 reservations
slurmctld: read_slurm_conf: backup_controller not specified
slurmctld: select/cons_tres: select_p_reconfigure: select/cons_tres: reconfigure
slurmctld: select/cons_tres: part_data_create_array: select/cons_tres: preparing for 1 partitions
slurmctld: Running as primary controller
slurmctld: No parameter for mcs plugin, default values set
slurmctld: mcs: MCSParameters = (null). ondemand set.
slurmctld: SchedulerParameters=default_queue_depth=100,max_rpc_cnt=0,max_sched_time=2,partition_job_depth=0,sched_max_job_start=0,sched_min_interval=2
slurmctld: error: Nodes localhost not responding
slurmctld: error: Nodes localhost not responding
^Cslurmctld: Terminate signal (SIGINT or SIGTERM) received
slurmctld: Saving all slurm state
(cuda_env) a10-kfotso@a10-cuanschutz01:~/slurm$ ^C
(cuda_env) a10-kfotso@a10-cuanschutz01:~/slurm$ sudo systemctl stop slurmctld
(cuda_env) a10-kfotso@a10-cuanschutz01:~/slurm$ sudo systemctl start slurmctld
(cuda_env) a10-kfotso@a10-cuanschutz01:~/slurm$  systemctl status slurmctld
● slurmctld.service - Slurm controller daemon
     Loaded: loaded (/lib/systemd/system/slurmctld.service; enabled; vendor preset: enabled)
     Active: active (running) since Sun 2024-07-21 00:29:53 UTC; 5s ago
       Docs: man:slurmctld(8)
   Main PID: 194544 (slurmctld)
      Tasks: 14
     Memory: 35.3M
        CPU: 11ms
     CGroup: /system.slice/slurmctld.service
             ├─194544 /usr/sbin/slurmctld -D -s
             └─194545 "slurmctld: slurmscriptd" "" ""
(cuda_env) a10-kfotso@a10-cuanschutz01:~/slurm$ sinfo -a
PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
LocalQ*      up   infinite      1    unk localhost

```


