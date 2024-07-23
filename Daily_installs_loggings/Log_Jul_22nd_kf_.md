Install logs:
=============

* To run the [AC-DC](https://code.google.com/archive/p/ac-dc/downloads) software I had to install gsl

```bash
wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/ac-dc/paper_experiment.zip
unzip paper_experiment.zip
a10-kfotso@a10-cuanschutz01:~/ac-dc_/paper_experiment$ sudo apt-get install libgsl-dev
[sudo] password for a10-kfotso: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  cuda-cuobjdump-12-5 cuda-cuxxfilt-12-5 cuda-documentation-12-5 cuda-gdb-12-5 cuda-nvdisasm-12-5 cuda-nvprune-12-5 cuda-nvtx-12-5 cuda-nvvm-12-5 cuda-sanitizer-12-5 cuda-toolkit-12-5-config-common
  cuda-toolkit-12-config-common cuda-toolkit-config-common gds-tools-12-5 libcudla-12-5 libcufft-12-5 libcufile-12-5 libcufile-dev-12-5 libcurand-12-5 libcusolver-12-5 libcusparse-12-5 libnpp-12-5
  libnvfatbin-12-5 libnvjitlink-12-5
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  libgsl27 libgslcblas0
Suggested packages:
  gsl-ref-psdoc | gsl-doc-pdf | gsl-doc-info | gsl-ref-html
The following NEW packages will be installed:
  libgsl-dev libgsl27 libgslcblas0
0 upgraded, 3 newly installed, 0 to remove and 60 not upgraded.
Need to get 2,169 kB of archives.
After this operation, 10.2 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://ports.ubuntu.com/ubuntu-ports jammy/universe arm64 libgslcblas0 arm64 2.7.1+dfsg-3 [72.4 kB]
Get:2 http://ports.ubuntu.com/ubuntu-ports jammy/universe arm64 libgsl27 arm64 2.7.1+dfsg-3 [919 kB]
Get:3 http://ports.ubuntu.com/ubuntu-ports jammy/universe arm64 libgsl-dev arm64 2.7.1+dfsg-3 [1,178 kB]
Fetched 2,169 kB in 4s (508 kB/s)       
Selecting previously unselected package libgslcblas0:arm64.
(Reading database ... 197230 files and directories currently installed.)
Preparing to unpack .../libgslcblas0_2.7.1+dfsg-3_arm64.deb ...
Unpacking libgslcblas0:arm64 (2.7.1+dfsg-3) ...
Selecting previously unselected package libgsl27:arm64.
Preparing to unpack .../libgsl27_2.7.1+dfsg-3_arm64.deb ...
Unpacking libgsl27:arm64 (2.7.1+dfsg-3) ...
Selecting previously unselected package libgsl-dev.
Preparing to unpack .../libgsl-dev_2.7.1+dfsg-3_arm64.deb ...
Unpacking libgsl-dev (2.7.1+dfsg-3) ...
Setting up libgslcblas0:arm64 (2.7.1+dfsg-3) ...
Setting up libgsl27:arm64 (2.7.1+dfsg-3) ...
Setting up libgsl-dev (2.7.1+dfsg-3) ...
Processing triggers for man-db (2.10.2-1) ...
Processing triggers for libc-bin (2.35-0ubuntu3.8) ...
Scanning processes...                                                                                                                                                                                             
Scanning candidates...                                                                                                                                                                                            
Scanning processor microcode...                                                                                                                                                                                   
Scanning linux images...                                                                                                                                                                                          

Failed to check for processor microcode upgrades.

Restarting services...
Service restarts being deferred:
 systemctl restart networkd-dispatcher.service
 systemctl restart packagekit.service
 systemctl restart systemd-journald.service
 systemctl restart systemd-logind.service
 /etc/needrestart/restart.d/systemd-manager
 systemctl restart systemd-networkd.service
 systemctl restart systemd-resolved.service
 systemctl restart systemd-timesyncd.service
 systemctl restart systemd-udevd.service
 systemctl restart udisks2.service
 systemctl restart unattended-upgrades.service
 systemctl restart user@1001.service

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.

a10-kfotso@a10-cuanschutz01:~/ac-dc_/paper_experiment$ make >> exp_.log


```

* I need the profiler in a conda ENV:

```bash
eval "$(/opt/miniconda3/bin/conda shell.bash hook)"
conda activate cuda_env
 conda install nvidia::cuda-nvprof
```
