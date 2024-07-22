HPL benchmarking:
==============

* Generated the HPL.dat files using this [link](https://www.advancedclustering.com/act_kb/tune-hpl-dat-file/)
* This HPL NVIDIA [documentation](https://docs.nvidia.com/nvidia-hpc-benchmarks/overview.html#using-custom-libraries) is useful.
* And of course the [documentation](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/hpc-benchmarks) on the container page is very useful as well.

```bash
python  calculate_pi_gpu_opt_clean_float64.py 1000000000
```
Results in --> ```Pi = 3.14159265358980155369, (Diff=0.00000000000000843769) (calculated in 27.445787 secs with 1000000000 steps)```

* Running the HPL container as below. Note that the amount of cores sent with mpirun needs to be identical with what is written on the .dat file.

```bash
apptainer shell -H $CONTAIN_DIR --nv hpc-benchmarks\:24.06.sif
 mpirun -n 72 /workspace/hpl.sh --dat mysample.dat
================================================================================
HPL-NVIDIA 24.6.0  -- NVIDIA accelerated HPL benchmark -- NVIDIA
================================================================================
HPLinpack 2.1  --  High-Performance Linpack benchmark  --   October 26, 2012
Written by A. Petitet and R. Clint Whaley,  Innovative Computing Laboratory, UTK
Modified by Piotr Luszczek, Innovative Computing Laboratory, UTK
Modified by Julien Langou, University of Colorado Denver
================================================================================

An explanation of the input/output parameters follows:
T/V    : Wall time / encoded variant.
N      : The order of the coefficient matrix A.
NB     : The partitioning blocking factor.
P      : The number of process rows.
Q      : The number of process columns.
Time   : Time in seconds to solve the linear system.
Gflops : Rate of execution for solving the linear system.

The following parameter values will be used:

N      :    6912 
NB     :     192 
PMAP   : Row-major process mapping
P      :       8 
Q      :       9 
PFACT  :   Right 
NBMIN  :       4 
NDIV   :       2 
RFACT  :   Crout 
BCAST  :  1ringM 
DEPTH  :       1 
SWAP   : Mix (threshold = 64)
L1     : transposed form
U      : transposed form
EQUIL  : yes
ALIGN  : 8 double precision words

--------------------------------------------------------------------------------

- The matrix A is randomly generated for each test.
- The following scaled residual check will be computed:
      ||Ax-b||_oo / ( eps * ( || x ||_oo * || A ||_oo + || b ||_oo ) * N )
- The relative machine precision (eps) is taken to be               1.110223e-16
- Computational tests pass if scaled residuals are less than                16.0


HPL-NVIDIA ignores the following parameters from input file:
	* Broadcast parameters
	* Panel factorization parameters
	* Look-ahead value
	* L1 layout
	* U layout
	* Equilibration parameter
	* Memory alignment parameter

HPL-NVIDIA settings from environment variables:
[WARNING]: HPL_FCT_COMM_POLICY=1 (host MPI) will be used with row-major process mapping
--- DEVICE INFO ---
  Peak clock frequency: 1980 MHz
  SM version          : 90
  Number of SMs       : 132
-------------------
[HPL TRACE] cuda_nvshmem_init: max=15.9546 (1) min=15.7468 (59)
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:205060] *** Process received signal ***
[a10-cuanschutz01:205060] Signal: Aborted (6)
[a10-cuanschutz01:205060] Signal code:  (-6)
[a10-cuanschutz01:205060] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xe2df88c209d0]
[a10-cuanschutz01:205060] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xe2df5298f200]
[a10-cuanschutz01:205060] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xe2df5294a67c]
[a10-cuanschutz01:205060] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xe2df52937130]
[a10-cuanschutz01:205060] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xe2df52983308]
[a10-cuanschutz01:205060] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xe2df5299957c]
[a10-cuanschutz01:205060] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xe2df52999ed8]
[a10-cuanschutz01:205060] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xe2df5299b558]
[a10-cuanschutz01:205060] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xe2df5299dc84]
[a10-cuanschutz01:205060] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xe2df5294cecc]
[a10-cuanschutz01:205060] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xe2df5294cf0c]
[a10-cuanschutz01:205060] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb1b623d9128c]
[a10-cuanschutz01:205060] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb1b623d6817c]
[a10-cuanschutz01:205060] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xe2df529373fc]
[a10-cuanschutz01:205060] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xe2df529374cc]
[a10-cuanschutz01:205060] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb1b623d69070]
[a10-cuanschutz01:205060] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204895] *** Process received signal ***
[a10-cuanschutz01:204895] Signal: Aborted (6)
[a10-cuanschutz01:204895] Signal code:  (-6)
[a10-cuanschutz01:204895] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xecf8097b09d0]
[a10-cuanschutz01:204895] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xecf7d351f200]
[a10-cuanschutz01:204895] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xecf7d34da67c]
[a10-cuanschutz01:204895] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xecf7d34c7130]
[a10-cuanschutz01:204895] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xecf7d3513308]
[a10-cuanschutz01:204895] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xecf7d352957c]
[a10-cuanschutz01:204895] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xecf7d3529ed8]
[a10-cuanschutz01:204895] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xecf7d352b558]
[a10-cuanschutz01:204895] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xecf7d352dc84]
[a10-cuanschutz01:204895] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xecf7d34dcecc]
[a10-cuanschutz01:204895] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xecf7d34dcf0c]
[a10-cuanschutz01:204895] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xbef9269f128c]
[a10-cuanschutz01:204895] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xbef9269c817c]
[a10-cuanschutz01:204895] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xecf7d34c73fc]
[a10-cuanschutz01:204895] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xecf7d34c74cc]
[a10-cuanschutz01:204895] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xbef9269c9070]
[a10-cuanschutz01:204895] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204511] *** Process received signal ***
[a10-cuanschutz01:204511] Signal: Aborted (6)
[a10-cuanschutz01:204511] Signal code:  (-6)
[a10-cuanschutz01:204511] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xfbf0ca4109d0]
[a10-cuanschutz01:204511] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xfbf09417f200]
[a10-cuanschutz01:204511] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xfbf09413a67c]
[a10-cuanschutz01:204511] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xfbf094127130]
[a10-cuanschutz01:204511] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xfbf094173308]
[a10-cuanschutz01:204511] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xfbf09418957c]
[a10-cuanschutz01:204511] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xfbf094189ed8]
[a10-cuanschutz01:204511] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xfbf09418b558]
[a10-cuanschutz01:204511] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xfbf09418dc84]
[a10-cuanschutz01:204511] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xfbf09413cecc]
[a10-cuanschutz01:204511] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xfbf09413cf0c]
[a10-cuanschutz01:204511] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xac46db89128c]
[a10-cuanschutz01:204511] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xac46db86817c]
[a10-cuanschutz01:204511] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xfbf0941273fc]
[a10-cuanschutz01:204511] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xfbf0941274cc]
[a10-cuanschutz01:204511] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xac46db869070]
[a10-cuanschutz01:204511] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204961] *** Process received signal ***
[a10-cuanschutz01:204961] Signal: Aborted (6)
[a10-cuanschutz01:204961] Signal code:  (-6)
[a10-cuanschutz01:204961] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf981af6d09d0]
[a10-cuanschutz01:204961] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf9817943f200]
[a10-cuanschutz01:204961] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf981793fa67c]
[a10-cuanschutz01:204961] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf981793e7130]
[a10-cuanschutz01:204961] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf98179433308]
[a10-cuanschutz01:204961] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf9817944957c]
[a10-cuanschutz01:204961] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf98179449ed8]
[a10-cuanschutz01:204961] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf9817944b558]
[a10-cuanschutz01:204961] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf9817944dc84]
[a10-cuanschutz01:204961] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf981793fcecc]
[a10-cuanschutz01:204961] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf981793fcf0c]
[a10-cuanschutz01:204961] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb138989b128c]
[a10-cuanschutz01:204961] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb1389898817c]
[a10-cuanschutz01:204961] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf981793e73fc]
[a10-cuanschutz01:204961] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf981793e74cc]
[a10-cuanschutz01:204961] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb13898989070]
[a10-cuanschutz01:204961] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204994] *** Process received signal ***
[a10-cuanschutz01:204994] Signal: Aborted (6)
[a10-cuanschutz01:204994] Signal code:  (-6)
[a10-cuanschutz01:204994] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf53346cd09d0]
[a10-cuanschutz01:204994] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf53310a3f200]
[a10-cuanschutz01:204994] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf533109fa67c]
[a10-cuanschutz01:204994] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf533109e7130]
[a10-cuanschutz01:204994] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf53310a33308]
[a10-cuanschutz01:204994] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf53310a4957c]
[a10-cuanschutz01:204994] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf53310a49ed8]
[a10-cuanschutz01:204994] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf53310a4b558]
[a10-cuanschutz01:204994] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf53310a4dc84]
[a10-cuanschutz01:204994] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf533109fcecc]
[a10-cuanschutz01:204994] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf533109fcf0c]
[a10-cuanschutz01:204994] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xaf58903a128c]
[a10-cuanschutz01:204994] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xaf589037817c]
[a10-cuanschutz01:204994] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf533109e73fc]
[a10-cuanschutz01:204994] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf533109e74cc]
[a10-cuanschutz01:204994] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xaf5890379070]
[a10-cuanschutz01:204994] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204476] *** Process received signal ***
[a10-cuanschutz01:204476] Signal: Aborted (6)
[a10-cuanschutz01:204476] Signal code:  (-6)
[a10-cuanschutz01:204476] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf66109e809d0]
[a10-cuanschutz01:204476] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf660d3bef200]
[a10-cuanschutz01:204476] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf660d3baa67c]
[a10-cuanschutz01:204476] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf660d3b97130]
[a10-cuanschutz01:204476] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf660d3be3308]
[a10-cuanschutz01:204476] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf660d3bf957c]
[a10-cuanschutz01:204476] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf660d3bf9ed8]
[a10-cuanschutz01:204476] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf660d3bfb558]
[a10-cuanschutz01:204476] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf660d3bfdc84]
[a10-cuanschutz01:204476] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf660d3bacecc]
[a10-cuanschutz01:204476] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf660d3bacf0c]
[a10-cuanschutz01:204476] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xc47a4451128c]
[a10-cuanschutz01:204476] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xc47a444e817c]
[a10-cuanschutz01:204476] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf660d3b973fc]
[a10-cuanschutz01:204476] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf660d3b974cc]
[a10-cuanschutz01:204476] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xc47a444e9070]
[a10-cuanschutz01:204476] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204753] *** Process received signal ***
[a10-cuanschutz01:204753] Signal: Aborted (6)
[a10-cuanschutz01:204753] Signal code:  (-6)
[a10-cuanschutz01:204753] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xe8b0252c09d0]
[a10-cuanschutz01:204753] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xe8afef02f200]
[a10-cuanschutz01:204753] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xe8afeefea67c]
[a10-cuanschutz01:204753] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xe8afeefd7130]
[a10-cuanschutz01:204753] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xe8afef023308]
[a10-cuanschutz01:204753] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xe8afef03957c]
[a10-cuanschutz01:204753] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xe8afef039ed8]
[a10-cuanschutz01:204753] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xe8afef03b558]
[a10-cuanschutz01:204753] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xe8afef03dc84]
[a10-cuanschutz01:204753] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xe8afeefececc]
[a10-cuanschutz01:204753] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xe8afeefecf0c]
[a10-cuanschutz01:204753] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb0d307a7128c]
[a10-cuanschutz01:204753] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb0d307a4817c]
[a10-cuanschutz01:204753] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xe8afeefd73fc]
[a10-cuanschutz01:204753] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xe8afeefd74cc]
[a10-cuanschutz01:204753] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb0d307a49070]
[a10-cuanschutz01:204753] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204795] *** Process received signal ***
[a10-cuanschutz01:204795] Signal: Aborted (6)
[a10-cuanschutz01:204795] Signal code:  (-6)
[a10-cuanschutz01:204795] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf1db91e409d0]
[a10-cuanschutz01:204795] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf1db5bbaf200]
[a10-cuanschutz01:204795] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf1db5bb6a67c]
[a10-cuanschutz01:204795] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf1db5bb57130]
[a10-cuanschutz01:204795] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf1db5bba3308]
[a10-cuanschutz01:204795] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf1db5bbb957c]
[a10-cuanschutz01:204795] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf1db5bbb9ed8]
[a10-cuanschutz01:204795] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf1db5bbbb558]
[a10-cuanschutz01:204795] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf1db5bbbdc84]
[a10-cuanschutz01:204795] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf1db5bb6cecc]
[a10-cuanschutz01:204795] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf1db5bb6cf0c]
[a10-cuanschutz01:204795] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xbb2c36c2128c]
[a10-cuanschutz01:204795] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xbb2c36bf817c]
[a10-cuanschutz01:204795] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf1db5bb573fc]
[a10-cuanschutz01:204795] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf1db5bb574cc]
[a10-cuanschutz01:204795] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xbb2c36bf9070]
[a10-cuanschutz01:204795] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:205082] *** Process received signal ***
[a10-cuanschutz01:205082] Signal: Aborted (6)
[a10-cuanschutz01:205082] Signal code:  (-6)
[a10-cuanschutz01:205082] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xff927db609d0]
[a10-cuanschutz01:205082] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xff92478cf200]
[a10-cuanschutz01:205082] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xff924788a67c]
[a10-cuanschutz01:205082] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xff9247877130]
[a10-cuanschutz01:205082] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xff92478c3308]
[a10-cuanschutz01:205082] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xff92478d957c]
[a10-cuanschutz01:205082] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xff92478d9ed8]
[a10-cuanschutz01:205082] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xff92478db558]
[a10-cuanschutz01:205082] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xff92478ddc84]
[a10-cuanschutz01:205082] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xff924788cecc]
[a10-cuanschutz01:205082] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xff924788cf0c]
[a10-cuanschutz01:205082] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb21f1725128c]
[a10-cuanschutz01:205082] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb21f1722817c]
[a10-cuanschutz01:205082] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xff92478773fc]
[a10-cuanschutz01:205082] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xff92478774cc]
[a10-cuanschutz01:205082] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb21f17229070]
[a10-cuanschutz01:205082] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204939] *** Process received signal ***
[a10-cuanschutz01:204939] Signal: Aborted (6)
[a10-cuanschutz01:204939] Signal code:  (-6)
[a10-cuanschutz01:204939] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf3cb7c7b09d0]
[a10-cuanschutz01:204939] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf3cb4651f200]
[a10-cuanschutz01:204939] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf3cb464da67c]
[a10-cuanschutz01:204939] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf3cb464c7130]
[a10-cuanschutz01:204939] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf3cb46513308]
[a10-cuanschutz01:204939] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf3cb4652957c]
[a10-cuanschutz01:204939] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf3cb46529ed8]
[a10-cuanschutz01:204939] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf3cb4652b558]
[a10-cuanschutz01:204939] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf3cb4652dc84]
[a10-cuanschutz01:204939] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf3cb464dcecc]
[a10-cuanschutz01:204939] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf3cb464dcf0c]
[a10-cuanschutz01:204939] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xc5c02a6c128c]
[a10-cuanschutz01:204939] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xc5c02a69817c]
[a10-cuanschutz01:204939] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf3cb464c73fc]
[a10-cuanschutz01:204939] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf3cb464c74cc]
[a10-cuanschutz01:204939] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xc5c02a699070]
[a10-cuanschutz01:204939] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204928] *** Process received signal ***
[a10-cuanschutz01:204928] Signal: Aborted (6)
[a10-cuanschutz01:204928] Signal code:  (-6)
[a10-cuanschutz01:204928] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf081456d09d0]
[a10-cuanschutz01:204928] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf0810f43f200]
[a10-cuanschutz01:204928] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf0810f3fa67c]
[a10-cuanschutz01:204928] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf0810f3e7130]
[a10-cuanschutz01:204928] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf0810f433308]
[a10-cuanschutz01:204928] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf0810f44957c]
[a10-cuanschutz01:204928] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf0810f449ed8]
[a10-cuanschutz01:204928] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf0810f44b558]
[a10-cuanschutz01:204928] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf0810f44dc84]
[a10-cuanschutz01:204928] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf0810f3fcecc]
[a10-cuanschutz01:204928] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf0810f3fcf0c]
[a10-cuanschutz01:204928] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb49284dc128c]
[a10-cuanschutz01:204928] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb49284d9817c]
[a10-cuanschutz01:204928] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf0810f3e73fc]
[a10-cuanschutz01:204928] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf0810f3e74cc]
[a10-cuanschutz01:204928] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb49284d99070]
[a10-cuanschutz01:204928] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204775] *** Process received signal ***
[a10-cuanschutz01:204775] Signal: Aborted (6)
[a10-cuanschutz01:204775] Signal code:  (-6)
[a10-cuanschutz01:204775] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xfa61816b09d0]
[a10-cuanschutz01:204775] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xfa614b41f200]
[a10-cuanschutz01:204775] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xfa614b3da67c]
[a10-cuanschutz01:204775] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xfa614b3c7130]
[a10-cuanschutz01:204775] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xfa614b413308]
[a10-cuanschutz01:204775] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xfa614b42957c]
[a10-cuanschutz01:204775] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xfa614b429ed8]
[a10-cuanschutz01:204775] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xfa614b42b558]
[a10-cuanschutz01:204775] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xfa614b42dc84]
[a10-cuanschutz01:204775] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xfa614b3dcecc]
[a10-cuanschutz01:204775] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xfa614b3dcf0c]
[a10-cuanschutz01:204775] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xc2c0ae40128c]
[a10-cuanschutz01:204775] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xc2c0ae3d817c]
[a10-cuanschutz01:204775] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xfa614b3c73fc]
[a10-cuanschutz01:204775] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xfa614b3c74cc]
[a10-cuanschutz01:204775] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xc2c0ae3d9070]
[a10-cuanschutz01:204775] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:205005] *** Process received signal ***
[a10-cuanschutz01:205005] Signal: Aborted (6)
[a10-cuanschutz01:205005] Signal code:  (-6)
[a10-cuanschutz01:205005] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf5d8e4bd09d0]
[a10-cuanschutz01:205005] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf5d8ae93f200]
[a10-cuanschutz01:205005] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf5d8ae8fa67c]
[a10-cuanschutz01:205005] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf5d8ae8e7130]
[a10-cuanschutz01:205005] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf5d8ae933308]
[a10-cuanschutz01:205005] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf5d8ae94957c]
[a10-cuanschutz01:205005] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf5d8ae949ed8]
[a10-cuanschutz01:205005] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf5d8ae94b558]
[a10-cuanschutz01:205005] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf5d8ae94dc84]
[a10-cuanschutz01:205005] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf5d8ae8fcecc]
[a10-cuanschutz01:205005] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf5d8ae8fcf0c]
[a10-cuanschutz01:205005] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb3840e27128c]
[a10-cuanschutz01:205005] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb3840e24817c]
[a10-cuanschutz01:205005] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf5d8ae8e73fc]
[a10-cuanschutz01:205005] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf5d8ae8e74cc]
[a10-cuanschutz01:205005] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb3840e249070]
[a10-cuanschutz01:205005] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204403] *** Process received signal ***
[a10-cuanschutz01:204403] Signal: Aborted (6)
[a10-cuanschutz01:204403] Signal code:  (-6)
[a10-cuanschutz01:204403] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xee23027e09d0]
[a10-cuanschutz01:204403] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xee22cc54f200]
[a10-cuanschutz01:204403] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xee22cc50a67c]
[a10-cuanschutz01:204403] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xee22cc4f7130]
[a10-cuanschutz01:204403] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xee22cc543308]
[a10-cuanschutz01:204403] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xee22cc55957c]
[a10-cuanschutz01:204403] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xee22cc559ed8]
[a10-cuanschutz01:204403] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xee22cc55b558]
[a10-cuanschutz01:204403] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xee22cc55dc84]
[a10-cuanschutz01:204403] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xee22cc50cecc]
[a10-cuanschutz01:204403] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xee22cc50cf0c]
[a10-cuanschutz01:204403] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb80bdcd8128c]
[a10-cuanschutz01:204403] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb80bdcd5817c]
[a10-cuanschutz01:204403] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xee22cc4f73fc]
[a10-cuanschutz01:204403] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xee22cc4f74cc]
[a10-cuanschutz01:204403] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb80bdcd59070]
[a10-cuanschutz01:204403] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204950] *** Process received signal ***
[a10-cuanschutz01:204950] Signal: Aborted (6)
[a10-cuanschutz01:204950] Signal code:  (-6)
[a10-cuanschutz01:204950] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xfd5fc7ab09d0]
[a10-cuanschutz01:204950] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xfd5f9181f200]
[a10-cuanschutz01:204950] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xfd5f917da67c]
[a10-cuanschutz01:204950] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xfd5f917c7130]
[a10-cuanschutz01:204950] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xfd5f91813308]
[a10-cuanschutz01:204950] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xfd5f9182957c]
[a10-cuanschutz01:204950] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xfd5f91829ed8]
[a10-cuanschutz01:204950] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xfd5f9182b558]
[a10-cuanschutz01:204950] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xfd5f9182dc84]
[a10-cuanschutz01:204950] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xfd5f917dcecc]
[a10-cuanschutz01:204950] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xfd5f917dcf0c]
[a10-cuanschutz01:204950] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xba9a9d7f128c]
[a10-cuanschutz01:204950] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xba9a9d7c817c]
[a10-cuanschutz01:204950] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xfd5f917c73fc]
[a10-cuanschutz01:204950] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xfd5f917c74cc]
[a10-cuanschutz01:204950] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xba9a9d7c9070]
[a10-cuanschutz01:204950] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:205092] *** Process received signal ***
[a10-cuanschutz01:205092] Signal: Aborted (6)
[a10-cuanschutz01:205092] Signal code:  (-6)
[a10-cuanschutz01:205092] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xedb8a21009d0]
[a10-cuanschutz01:205092] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xedb86be6f200]
[a10-cuanschutz01:205092] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xedb86be2a67c]
[a10-cuanschutz01:205092] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xedb86be17130]
[a10-cuanschutz01:205092] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xedb86be63308]
[a10-cuanschutz01:205092] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xedb86be7957c]
[a10-cuanschutz01:205092] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xedb86be79ed8]
[a10-cuanschutz01:205092] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xedb86be7b558]
[a10-cuanschutz01:205092] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xedb86be7dc84]
[a10-cuanschutz01:205092] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xedb86be2cecc]
[a10-cuanschutz01:205092] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xedb86be2cf0c]
[a10-cuanschutz01:205092] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb977737a128c]
[a10-cuanschutz01:205092] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb9777377817c]
[a10-cuanschutz01:205092] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xedb86be173fc]
[a10-cuanschutz01:205092] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xedb86be174cc]
[a10-cuanschutz01:205092] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb97773779070]
[a10-cuanschutz01:205092] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204562] *** Process received signal ***
[a10-cuanschutz01:204562] Signal: Aborted (6)
[a10-cuanschutz01:204562] Signal code:  (-6)
[a10-cuanschutz01:204562] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xfb4ed85109d0]
[a10-cuanschutz01:204562] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xfb4ea227f200]
[a10-cuanschutz01:204562] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xfb4ea223a67c]
[a10-cuanschutz01:204562] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xfb4ea2227130]
[a10-cuanschutz01:204562] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xfb4ea2273308]
[a10-cuanschutz01:204562] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xfb4ea228957c]
[a10-cuanschutz01:204562] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xfb4ea2289ed8]
[a10-cuanschutz01:204562] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xfb4ea228b558]
[a10-cuanschutz01:204562] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xfb4ea228dc84]
[a10-cuanschutz01:204562] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xfb4ea223cecc]
[a10-cuanschutz01:204562] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xfb4ea223cf0c]
[a10-cuanschutz01:204562] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb2b507a2128c]
[a10-cuanschutz01:204562] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb2b5079f817c]
[a10-cuanschutz01:204562] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xfb4ea22273fc]
[a10-cuanschutz01:204562] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xfb4ea22274cc]
[a10-cuanschutz01:204562] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb2b5079f9070]
[a10-cuanschutz01:204562] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204383] *** Process received signal ***
[a10-cuanschutz01:204383] Signal: Aborted (6)
[a10-cuanschutz01:204383] Signal code:  (-6)
[a10-cuanschutz01:204383] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xe7080a2409d0]
[a10-cuanschutz01:204383] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xe707d3faf200]
[a10-cuanschutz01:204383] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xe707d3f6a67c]
[a10-cuanschutz01:204383] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xe707d3f57130]
[a10-cuanschutz01:204383] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xe707d3fa3308]
[a10-cuanschutz01:204383] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xe707d3fb957c]
[a10-cuanschutz01:204383] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xe707d3fb9ed8]
[a10-cuanschutz01:204383] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xe707d3fbb558]
[a10-cuanschutz01:204383] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xe707d3fbdc84]
[a10-cuanschutz01:204383] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xe707d3f6cecc]
[a10-cuanschutz01:204383] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xe707d3f6cf0c]
[a10-cuanschutz01:204383] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb67509dd128c]
[a10-cuanschutz01:204383] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb67509da817c]
[a10-cuanschutz01:204383] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xe707d3f573fc]
[a10-cuanschutz01:204383] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xe707d3f574cc]
[a10-cuanschutz01:204383] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb67509da9070]
[a10-cuanschutz01:204383] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204709] *** Process received signal ***
[a10-cuanschutz01:204709] Signal: Aborted (6)
[a10-cuanschutz01:204709] Signal code:  (-6)
[a10-cuanschutz01:204709] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf081103909d0]
[a10-cuanschutz01:204709] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf080da0ff200]
[a10-cuanschutz01:204709] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf080da0ba67c]
[a10-cuanschutz01:204709] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf080da0a7130]
[a10-cuanschutz01:204709] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf080da0f3308]
[a10-cuanschutz01:204709] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf080da10957c]
[a10-cuanschutz01:204709] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf080da109ed8]
[a10-cuanschutz01:204709] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf080da10b558]
[a10-cuanschutz01:204709] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf080da10dc84]
[a10-cuanschutz01:204709] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf080da0bcecc]
[a10-cuanschutz01:204709] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf080da0bcf0c]
[a10-cuanschutz01:204709] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb81ac634128c]
[a10-cuanschutz01:204709] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb81ac631817c]
[a10-cuanschutz01:204709] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf080da0a73fc]
[a10-cuanschutz01:204709] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf080da0a74cc]
[a10-cuanschutz01:204709] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb81ac6319070]
[a10-cuanschutz01:204709] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:205148] *** Process received signal ***
[a10-cuanschutz01:205148] Signal: Aborted (6)
[a10-cuanschutz01:205148] Signal code:  (-6)
[a10-cuanschutz01:205148] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf2d59da409d0]
[a10-cuanschutz01:205148] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf2d5677af200]
[a10-cuanschutz01:205148] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf2d56776a67c]
[a10-cuanschutz01:205148] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf2d567757130]
[a10-cuanschutz01:205148] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf2d5677a3308]
[a10-cuanschutz01:205148] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf2d5677b957c]
[a10-cuanschutz01:205148] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf2d5677b9ed8]
[a10-cuanschutz01:205148] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf2d5677bb558]
[a10-cuanschutz01:205148] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf2d5677bdc84]
[a10-cuanschutz01:205148] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf2d56776cecc]
[a10-cuanschutz01:205148] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf2d56776cf0c]
[a10-cuanschutz01:205148] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xc66ee7da128c]
[a10-cuanschutz01:205148] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xc66ee7d7817c]
[a10-cuanschutz01:205148] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf2d5677573fc]
[a10-cuanschutz01:205148] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf2d5677574cc]
[a10-cuanschutz01:205148] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xc66ee7d79070]
[a10-cuanschutz01:205148] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204676] *** Process received signal ***
[a10-cuanschutz01:204676] Signal: Aborted (6)
[a10-cuanschutz01:204676] Signal code:  (-6)
[a10-cuanschutz01:204676] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf05b36c709d0]
[a10-cuanschutz01:204676] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf05b009df200]
[a10-cuanschutz01:204676] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf05b0099a67c]
[a10-cuanschutz01:204676] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf05b00987130]
[a10-cuanschutz01:204676] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf05b009d3308]
[a10-cuanschutz01:204676] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf05b009e957c]
[a10-cuanschutz01:204676] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf05b009e9ed8]
[a10-cuanschutz01:204676] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf05b009eb558]
[a10-cuanschutz01:204676] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf05b009edc84]
[a10-cuanschutz01:204676] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf05b0099cecc]
[a10-cuanschutz01:204676] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf05b0099cf0c]
[a10-cuanschutz01:204676] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xca0dfa4d128c]
[a10-cuanschutz01:204676] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xca0dfa4a817c]
[a10-cuanschutz01:204676] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf05b009873fc]
[a10-cuanschutz01:204676] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf05b009874cc]
[a10-cuanschutz01:204676] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xca0dfa4a9070]
[a10-cuanschutz01:204676] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204665] *** Process received signal ***
[a10-cuanschutz01:204665] Signal: Aborted (6)
[a10-cuanschutz01:204665] Signal code:  (-6)
[a10-cuanschutz01:204665] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xfcf72b6609d0]
[a10-cuanschutz01:204665] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xfcf6f53cf200]
[a10-cuanschutz01:204665] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xfcf6f538a67c]
[a10-cuanschutz01:204665] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xfcf6f5377130]
[a10-cuanschutz01:204665] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xfcf6f53c3308]
[a10-cuanschutz01:204665] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xfcf6f53d957c]
[a10-cuanschutz01:204665] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xfcf6f53d9ed8]
[a10-cuanschutz01:204665] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xfcf6f53db558]
[a10-cuanschutz01:204665] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xfcf6f53ddc84]
[a10-cuanschutz01:204665] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xfcf6f538cecc]
[a10-cuanschutz01:204665] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xfcf6f538cf0c]
[a10-cuanschutz01:204665] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xbe94b4e0128c]
[a10-cuanschutz01:204665] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xbe94b4dd817c]
[a10-cuanschutz01:204665] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xfcf6f53773fc]
[a10-cuanschutz01:204665] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xfcf6f53774cc]
[a10-cuanschutz01:204665] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xbe94b4dd9070]
[a10-cuanschutz01:204665] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204822] *** Process received signal ***
[a10-cuanschutz01:204822] Signal: Aborted (6)
[a10-cuanschutz01:204822] Signal code:  (-6)
[a10-cuanschutz01:204822] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf3ff475709d0]
[a10-cuanschutz01:204822] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf3ff112df200]
[a10-cuanschutz01:204822] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf3ff1129a67c]
[a10-cuanschutz01:204822] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf3ff11287130]
[a10-cuanschutz01:204822] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf3ff112d3308]
[a10-cuanschutz01:204822] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf3ff112e957c]
[a10-cuanschutz01:204822] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf3ff112e9ed8]
[a10-cuanschutz01:204822] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf3ff112eb558]
[a10-cuanschutz01:204822] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf3ff112edc84]
[a10-cuanschutz01:204822] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf3ff1129cecc]
[a10-cuanschutz01:204822] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf3ff1129cf0c]
[a10-cuanschutz01:204822] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xc1325864128c]
[a10-cuanschutz01:204822] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xc1325861817c]
[a10-cuanschutz01:204822] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf3ff112873fc]
[a10-cuanschutz01:204822] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf3ff112874cc]
[a10-cuanschutz01:204822] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xc13258619070]
[a10-cuanschutz01:204822] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204425] *** Process received signal ***
[a10-cuanschutz01:204425] Signal: Aborted (6)
[a10-cuanschutz01:204425] Signal code:  (-6)
[a10-cuanschutz01:204425] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xebfd763509d0]
[a10-cuanschutz01:204425] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xebfd400bf200]
[a10-cuanschutz01:204425] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xebfd4007a67c]
[a10-cuanschutz01:204425] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xebfd40067130]
[a10-cuanschutz01:204425] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xebfd400b3308]
[a10-cuanschutz01:204425] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xebfd400c957c]
[a10-cuanschutz01:204425] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xebfd400c9ed8]
[a10-cuanschutz01:204425] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xebfd400cb558]
[a10-cuanschutz01:204425] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xebfd400cdc84]
[a10-cuanschutz01:204425] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xebfd4007cecc]
[a10-cuanschutz01:204425] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xebfd4007cf0c]
[a10-cuanschutz01:204425] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb1012ca0128c]
[a10-cuanschutz01:204425] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb1012c9d817c]
[a10-cuanschutz01:204425] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xebfd400673fc]
[a10-cuanschutz01:204425] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xebfd400674cc]
[a10-cuanschutz01:204425] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb1012c9d9070]
[a10-cuanschutz01:204425] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204363] *** Process received signal ***
[a10-cuanschutz01:204363] Signal: Aborted (6)
[a10-cuanschutz01:204363] Signal code:  (-6)
[a10-cuanschutz01:204363] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xed7b52f609d0]
[a10-cuanschutz01:204363] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xed7b1cccf200]
[a10-cuanschutz01:204363] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xed7b1cc8a67c]
[a10-cuanschutz01:204363] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xed7b1cc77130]
[a10-cuanschutz01:204363] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xed7b1ccc3308]
[a10-cuanschutz01:204363] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xed7b1ccd957c]
[a10-cuanschutz01:204363] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xed7b1ccd9ed8]
[a10-cuanschutz01:204363] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xed7b1ccdb558]
[a10-cuanschutz01:204363] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xed7b1ccddc84]
[a10-cuanschutz01:204363] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xed7b1cc8cecc]
[a10-cuanschutz01:204363] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xed7b1cc8cf0c]
[a10-cuanschutz01:204363] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xc44a5cc5128c]
[a10-cuanschutz01:204363] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xc44a5cc2817c]
[a10-cuanschutz01:204363] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xed7b1cc773fc]
[a10-cuanschutz01:204363] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xed7b1cc774cc]
[a10-cuanschutz01:204363] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xc44a5cc29070]
[a10-cuanschutz01:204363] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204522] *** Process received signal ***
[a10-cuanschutz01:204522] Signal: Aborted (6)
[a10-cuanschutz01:204522] Signal code:  (-6)
[a10-cuanschutz01:204522] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf7bab64709d0]
[a10-cuanschutz01:204522] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf7ba801df200]
[a10-cuanschutz01:204522] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf7ba8019a67c]
[a10-cuanschutz01:204522] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf7ba80187130]
[a10-cuanschutz01:204522] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf7ba801d3308]
[a10-cuanschutz01:204522] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf7ba801e957c]
[a10-cuanschutz01:204522] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf7ba801e9ed8]
[a10-cuanschutz01:204522] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf7ba801eb558]
[a10-cuanschutz01:204522] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf7ba801edc84]
[a10-cuanschutz01:204522] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf7ba8019cecc]
[a10-cuanschutz01:204522] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf7ba8019cf0c]
[a10-cuanschutz01:204522] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xbe6a8ffe128c]
[a10-cuanschutz01:204522] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xbe6a8ffb817c]
[a10-cuanschutz01:204522] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf7ba801873fc]
[a10-cuanschutz01:204522] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf7ba801874cc]
[a10-cuanschutz01:204522] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xbe6a8ffb9070]
[a10-cuanschutz01:204522] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204595] *** Process received signal ***
[a10-cuanschutz01:204595] Signal: Aborted (6)
[a10-cuanschutz01:204595] Signal code:  (-6)
[a10-cuanschutz01:204595] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf0a0e71309d0]
[a10-cuanschutz01:204595] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf0a0b0e9f200]
[a10-cuanschutz01:204595] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf0a0b0e5a67c]
[a10-cuanschutz01:204595] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf0a0b0e47130]
[a10-cuanschutz01:204595] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf0a0b0e93308]
[a10-cuanschutz01:204595] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf0a0b0ea957c]
[a10-cuanschutz01:204595] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf0a0b0ea9ed8]
[a10-cuanschutz01:204595] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf0a0b0eab558]
[a10-cuanschutz01:204595] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf0a0b0eadc84]
[a10-cuanschutz01:204595] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf0a0b0e5cecc]
[a10-cuanschutz01:204595] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf0a0b0e5cf0c]
[a10-cuanschutz01:204595] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xba4665bc128c]
[a10-cuanschutz01:204595] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xba4665b9817c]
[a10-cuanschutz01:204595] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf0a0b0e473fc]
[a10-cuanschutz01:204595] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf0a0b0e474cc]
[a10-cuanschutz01:204595] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xba4665b99070]
[a10-cuanschutz01:204595] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:205016] *** Process received signal ***
[a10-cuanschutz01:205016] Signal: Aborted (6)
[a10-cuanschutz01:205016] Signal code:  (-6)
[a10-cuanschutz01:205016] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xe8c76be609d0]
[a10-cuanschutz01:205016] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xe8c735bcf200]
[a10-cuanschutz01:205016] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xe8c735b8a67c]
[a10-cuanschutz01:205016] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xe8c735b77130]
[a10-cuanschutz01:205016] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xe8c735bc3308]
[a10-cuanschutz01:205016] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xe8c735bd957c]
[a10-cuanschutz01:205016] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xe8c735bd9ed8]
[a10-cuanschutz01:205016] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xe8c735bdb558]
[a10-cuanschutz01:205016] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xe8c735bddc84]
[a10-cuanschutz01:205016] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xe8c735b8cecc]
[a10-cuanschutz01:205016] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xe8c735b8cf0c]
[a10-cuanschutz01:205016] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb24c4ccb128c]
[a10-cuanschutz01:205016] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb24c4cc8817c]
[a10-cuanschutz01:205016] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xe8c735b773fc]
[a10-cuanschutz01:205016] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xe8c735b774cc]
[a10-cuanschutz01:205016] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb24c4cc89070]
[a10-cuanschutz01:205016] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204551] *** Process received signal ***
[a10-cuanschutz01:204551] Signal: Aborted (6)
[a10-cuanschutz01:204551] Signal code:  (-6)
[a10-cuanschutz01:204551] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xe730309f09d0]
[a10-cuanschutz01:204551] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xe72ffa75f200]
[a10-cuanschutz01:204551] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xe72ffa71a67c]
[a10-cuanschutz01:204551] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xe72ffa707130]
[a10-cuanschutz01:204551] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xe72ffa753308]
[a10-cuanschutz01:204551] [ 5] corrupted size vs. prev_size
/lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xe72ffa76957c]
[a10-cuanschutz01:204551] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xe72ffa769ed8]
[a10-cuanschutz01:204551] [ 7] [a10-cuanschutz01:204584] *** Process received signal ***
[a10-cuanschutz01:204584] Signal: Aborted (6)
[a10-cuanschutz01:204584] Signal code:  (-6)
/lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xe72ffa76b558]
[a10-cuanschutz01:204551] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xe72ffa76dc84]
[a10-cuanschutz01:204551] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xe72ffa71cecc]
[a10-cuanschutz01:204551] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xe72ffa71cf0c]
[a10-cuanschutz01:204551] [11] [a10-cuanschutz01:204584] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xff1e320709d0]
[a10-cuanschutz01:204584] [ 1] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xabeceac0128c]
[a10-cuanschutz01:204551] [12] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xff1dfbddf200]
[a10-cuanschutz01:204584] [ 2] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xabeceabd817c]
[a10-cuanschutz01:204551] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xe72ffa7073fc]
[a10-cuanschutz01:204551] [14] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xff1dfbd9a67c]
[a10-cuanschutz01:204584] [ 3] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xe72ffa7074cc]
[a10-cuanschutz01:204551] [15] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xff1dfbd87130]
[a10-cuanschutz01:204584] [ 4] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xabeceabd9070]
[a10-cuanschutz01:204551] *** End of error message ***
/lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xff1dfbdd3308]
[a10-cuanschutz01:204584] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xff1dfbde957c]
[a10-cuanschutz01:204584] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xff1dfbde9ed8]
[a10-cuanschutz01:204584] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xff1dfbdeb558]
[a10-cuanschutz01:204584] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xff1dfbdedc84]
[a10-cuanschutz01:204584] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xff1dfbd9cecc]
[a10-cuanschutz01:204584] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xff1dfbd9cf0c]
[a10-cuanschutz01:204584] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xae0c5ee4128c]
[a10-cuanschutz01:204584] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xae0c5ee1817c]
[a10-cuanschutz01:204584] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xff1dfbd873fc]
[a10-cuanschutz01:204584] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xff1dfbd874cc]
[a10-cuanschutz01:204584] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xae0c5ee19070]
[a10-cuanschutz01:204584] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204374] *** Process received signal ***
[a10-cuanschutz01:204374] Signal: Aborted (6)
[a10-cuanschutz01:204374] Signal code:  (-6)
[a10-cuanschutz01:204374] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf67c2b3209d0]
[a10-cuanschutz01:204374] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf67bf508f200]
[a10-cuanschutz01:204374] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf67bf504a67c]
[a10-cuanschutz01:204374] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf67bf5037130]
[a10-cuanschutz01:204374] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf67bf5083308]
[a10-cuanschutz01:204374] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf67bf509957c]
[a10-cuanschutz01:204374] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf67bf5099ed8]
[a10-cuanschutz01:204374] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf67bf509b558]
[a10-cuanschutz01:204374] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf67bf509dc84]
[a10-cuanschutz01:204374] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf67bf504cecc]
[a10-cuanschutz01:204374] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf67bf504cf0c]
[a10-cuanschutz01:204374] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xc4a4dc99128c]
[a10-cuanschutz01:204374] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xc4a4dc96817c]
[a10-cuanschutz01:204374] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf67bf50373fc]
[a10-cuanschutz01:204374] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf67bf50374cc]
[a10-cuanschutz01:204374] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xc4a4dc969070]
[a10-cuanschutz01:204374] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204840] *** Process received signal ***
[a10-cuanschutz01:204840] Signal: Aborted (6)
[a10-cuanschutz01:204840] Signal code:  (-6)
[a10-cuanschutz01:204840] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf4e49d2f09d0]
[a10-cuanschutz01:204840] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf4e46705f200]
[a10-cuanschutz01:204840] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf4e46701a67c]
[a10-cuanschutz01:204840] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf4e467007130]
[a10-cuanschutz01:204840] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf4e467053308]
[a10-cuanschutz01:204840] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf4e46706957c]
[a10-cuanschutz01:204840] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf4e467069ed8]
[a10-cuanschutz01:204840] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf4e46706b558]
[a10-cuanschutz01:204840] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf4e46706dc84]
[a10-cuanschutz01:204840] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf4e46701cecc]
[a10-cuanschutz01:204840] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf4e46701cf0c]
[a10-cuanschutz01:204840] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb7e3381d128c]
[a10-cuanschutz01:204840] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb7e3381a817c]
[a10-cuanschutz01:204840] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf4e4670073fc]
[a10-cuanschutz01:204840] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf4e4670074cc]
[a10-cuanschutz01:204840] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb7e3381a9070]
[a10-cuanschutz01:204840] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:205135] *** Process received signal ***
[a10-cuanschutz01:205135] Signal: Aborted (6)
[a10-cuanschutz01:205135] Signal code:  (-6)
[a10-cuanschutz01:205135] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf4029f3809d0]
[a10-cuanschutz01:205135] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf402690ef200]
[a10-cuanschutz01:205135] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf402690aa67c]
[a10-cuanschutz01:205135] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf40269097130]
[a10-cuanschutz01:205135] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf402690e3308]
[a10-cuanschutz01:205135] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf402690f957c]
[a10-cuanschutz01:205135] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf402690f9ed8]
[a10-cuanschutz01:205135] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf402690fb558]
[a10-cuanschutz01:205135] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf402690fdc84]
[a10-cuanschutz01:205135] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf402690acecc]
[a10-cuanschutz01:205135] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf402690acf0c]
[a10-cuanschutz01:205135] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xba138d33128c]
[a10-cuanschutz01:205135] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xba138d30817c]
[a10-cuanschutz01:205135] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf402690973fc]
[a10-cuanschutz01:205135] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf402690974cc]
[a10-cuanschutz01:205135] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xba138d309070]
[a10-cuanschutz01:205135] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204533] *** Process received signal ***
[a10-cuanschutz01:204533] Signal: Aborted (6)
[a10-cuanschutz01:204533] Signal code:  (-6)
[a10-cuanschutz01:204533] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf305fe7c09d0]
[a10-cuanschutz01:204533] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf305c852f200]
[a10-cuanschutz01:204533] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf305c84ea67c]
[a10-cuanschutz01:204533] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf305c84d7130]
[a10-cuanschutz01:204533] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf305c8523308]
[a10-cuanschutz01:204533] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf305c853957c]
[a10-cuanschutz01:204533] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf305c8539ed8]
[a10-cuanschutz01:204533] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf305c853b558]
[a10-cuanschutz01:204533] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf305c853dc84]
[a10-cuanschutz01:204533] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf305c84ececc]
[a10-cuanschutz01:204533] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf305c84ecf0c]
[a10-cuanschutz01:204533] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xc17c6c25128c]
[a10-cuanschutz01:204533] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xc17c6c22817c]
[a10-cuanschutz01:204533] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf305c84d73fc]
[a10-cuanschutz01:204533] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf305c84d74cc]
[a10-cuanschutz01:204533] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xc17c6c229070]
[a10-cuanschutz01:204533] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204742] *** Process received signal ***
[a10-cuanschutz01:204742] Signal: Aborted (6)
[a10-cuanschutz01:204742] Signal code:  (-6)
[a10-cuanschutz01:204742] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf4b7362909d0]
[a10-cuanschutz01:204742] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf4b6fffff200]
[a10-cuanschutz01:204742] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf4b6fffba67c]
[a10-cuanschutz01:204742] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf4b6fffa7130]
[a10-cuanschutz01:204742] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf4b6ffff3308]
[a10-cuanschutz01:204742] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf4b70000957c]
[a10-cuanschutz01:204742] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf4b700009ed8]
[a10-cuanschutz01:204742] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf4b70000b558]
[a10-cuanschutz01:204742] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf4b70000dc84]
[a10-cuanschutz01:204742] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf4b6fffbcecc]
[a10-cuanschutz01:204742] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf4b6fffbcf0c]
[a10-cuanschutz01:204742] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb54a595b128c]
[a10-cuanschutz01:204742] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb54a5958817c]
[a10-cuanschutz01:204742] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf4b6fffa73fc]
[a10-cuanschutz01:204742] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf4b6fffa74cc]
[a10-cuanschutz01:204742] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb54a59589070]
[a10-cuanschutz01:204742] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204718] *** Process received signal ***
[a10-cuanschutz01:204718] Signal: Aborted (6)
[a10-cuanschutz01:204718] Signal code:  (-6)
[a10-cuanschutz01:204718] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xe7954ed409d0]
[a10-cuanschutz01:204718] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xe79518aaf200]
[a10-cuanschutz01:204718] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xe79518a6a67c]
[a10-cuanschutz01:204718] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xe79518a57130]
[a10-cuanschutz01:204718] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xe79518aa3308]
[a10-cuanschutz01:204718] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xe79518ab957c]
[a10-cuanschutz01:204718] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xe79518ab9ed8]
[a10-cuanschutz01:204718] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xe79518abb558]
[a10-cuanschutz01:204718] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xe79518abdc84]
[a10-cuanschutz01:204718] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xe79518a6cecc]
[a10-cuanschutz01:204718] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xe79518a6cf0c]
[a10-cuanschutz01:204718] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb2f9b44c128c]
[a10-cuanschutz01:204718] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb2f9b449817c]
[a10-cuanschutz01:204718] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xe79518a573fc]
[a10-cuanschutz01:204718] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xe79518a574cc]
[a10-cuanschutz01:204718] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb2f9b4499070]
[a10-cuanschutz01:204718] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204573] *** Process received signal ***
[a10-cuanschutz01:204573] Signal: Aborted (6)
[a10-cuanschutz01:204573] Signal code:  (-6)
[a10-cuanschutz01:204573] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf830228009d0]
[a10-cuanschutz01:204573] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf82fec56f200]
[a10-cuanschutz01:204573] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf82fec52a67c]
[a10-cuanschutz01:204573] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf82fec517130]
[a10-cuanschutz01:204573] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf82fec563308]
[a10-cuanschutz01:204573] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf82fec57957c]
[a10-cuanschutz01:204573] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf82fec579ed8]
[a10-cuanschutz01:204573] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf82fec57b558]
[a10-cuanschutz01:204573] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf82fec57dc84]
[a10-cuanschutz01:204573] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf82fec52cecc]
[a10-cuanschutz01:204573] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf82fec52cf0c]
[a10-cuanschutz01:204573] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xbc7645eb128c]
[a10-cuanschutz01:204573] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xbc7645e8817c]
[a10-cuanschutz01:204573] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf82fec5173fc]
[a10-cuanschutz01:204573] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf82fec5174cc]
[a10-cuanschutz01:204573] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xbc7645e89070]
[a10-cuanschutz01:204573] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204764] *** Process received signal ***
[a10-cuanschutz01:204764] Signal: Aborted (6)
[a10-cuanschutz01:204764] Signal code:  (-6)
[a10-cuanschutz01:204764] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf94466d909d0]
[a10-cuanschutz01:204764] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf94430aff200]
[a10-cuanschutz01:204764] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf94430aba67c]
[a10-cuanschutz01:204764] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf94430aa7130]
[a10-cuanschutz01:204764] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf94430af3308]
[a10-cuanschutz01:204764] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf94430b0957c]
[a10-cuanschutz01:204764] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf94430b09ed8]
[a10-cuanschutz01:204764] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf94430b0b558]
[a10-cuanschutz01:204764] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf94430b0dc84]
[a10-cuanschutz01:204764] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf94430abcecc]
[a10-cuanschutz01:204764] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf94430abcf0c]
[a10-cuanschutz01:204764] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xbb076342128c]
[a10-cuanschutz01:204764] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xbb07633f817c]
[a10-cuanschutz01:204764] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf94430aa73fc]
[a10-cuanschutz01:204764] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf94430aa74cc]
[a10-cuanschutz01:204764] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xbb07633f9070]
[a10-cuanschutz01:204764] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204983] *** Process received signal ***
[a10-cuanschutz01:204983] Signal: Aborted (6)
[a10-cuanschutz01:204983] Signal code:  (-6)
[a10-cuanschutz01:204983] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xe9efaa1909d0]
[a10-cuanschutz01:204983] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xe9ef73eff200]
[a10-cuanschutz01:204983] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xe9ef73eba67c]
[a10-cuanschutz01:204983] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xe9ef73ea7130]
[a10-cuanschutz01:204983] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xe9ef73ef3308]
[a10-cuanschutz01:204983] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xe9ef73f0957c]
[a10-cuanschutz01:204983] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xe9ef73f09ed8]
[a10-cuanschutz01:204983] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xe9ef73f0b558]
[a10-cuanschutz01:204983] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xe9ef73f0dc84]
[a10-cuanschutz01:204983] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xe9ef73ebcecc]
[a10-cuanschutz01:204983] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xe9ef73ebcf0c]
[a10-cuanschutz01:204983] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xc38910f0128c]
[a10-cuanschutz01:204983] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xc38910ed817c]
[a10-cuanschutz01:204983] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xe9ef73ea73fc]
[a10-cuanschutz01:204983] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xe9ef73ea74cc]
[a10-cuanschutz01:204983] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xc38910ed9070]
[a10-cuanschutz01:204983] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204727] *** Process received signal ***
[a10-cuanschutz01:204727] Signal: Aborted (6)
[a10-cuanschutz01:204727] Signal code:  (-6)
[a10-cuanschutz01:204727] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf432144e09d0]
[a10-cuanschutz01:204727] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf431de24f200]
[a10-cuanschutz01:204727] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf431de20a67c]
[a10-cuanschutz01:204727] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf431de1f7130]
[a10-cuanschutz01:204727] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf431de243308]
[a10-cuanschutz01:204727] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf431de25957c]
[a10-cuanschutz01:204727] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf431de259ed8]
[a10-cuanschutz01:204727] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf431de25b558]
[a10-cuanschutz01:204727] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf431de25dc84]
[a10-cuanschutz01:204727] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf431de20cecc]
[a10-cuanschutz01:204727] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf431de20cf0c]
[a10-cuanschutz01:204727] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xc67b3951128c]
[a10-cuanschutz01:204727] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xc67b394e817c]
[a10-cuanschutz01:204727] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf431de1f73fc]
[a10-cuanschutz01:204727] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf431de1f74cc]
[a10-cuanschutz01:204727] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xc67b394e9070]
[a10-cuanschutz01:204727] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204851] *** Process received signal ***
[a10-cuanschutz01:204851] Signal: Aborted (6)
[a10-cuanschutz01:204851] Signal code:  (-6)
[a10-cuanschutz01:204851] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xef3f659209d0]
[a10-cuanschutz01:204851] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xef3f2f68f200]
[a10-cuanschutz01:204851] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xef3f2f64a67c]
[a10-cuanschutz01:204851] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xef3f2f637130]
[a10-cuanschutz01:204851] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xef3f2f683308]
[a10-cuanschutz01:204851] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xef3f2f69957c]
[a10-cuanschutz01:204851] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xef3f2f699ed8]
[a10-cuanschutz01:204851] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xef3f2f69b558]
[a10-cuanschutz01:204851] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xef3f2f69dc84]
[a10-cuanschutz01:204851] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xef3f2f64cecc]
[a10-cuanschutz01:204851] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xef3f2f64cf0c]
[a10-cuanschutz01:204851] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xc34094a9128c]
[a10-cuanschutz01:204851] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xc34094a6817c]
[a10-cuanschutz01:204851] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xef3f2f6373fc]
[a10-cuanschutz01:204851] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xef3f2f6374cc]
[a10-cuanschutz01:204851] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xc34094a69070]
[a10-cuanschutz01:204851] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204392] *** Process received signal ***
[a10-cuanschutz01:204392] Signal: Aborted (6)
[a10-cuanschutz01:204392] Signal code:  (-6)
[a10-cuanschutz01:204392] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xef08857e09d0]
[a10-cuanschutz01:204392] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xef084f54f200]
[a10-cuanschutz01:204392] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xef084f50a67c]
[a10-cuanschutz01:204392] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xef084f4f7130]
[a10-cuanschutz01:204392] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xef084f543308]
[a10-cuanschutz01:204392] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xef084f55957c]
[a10-cuanschutz01:204392] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xef084f559ed8]
[a10-cuanschutz01:204392] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xef084f55b558]
[a10-cuanschutz01:204392] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xef084f55dc84]
[a10-cuanschutz01:204392] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xef084f50cecc]
[a10-cuanschutz01:204392] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xef084f50cf0c]
[a10-cuanschutz01:204392] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb61fe4ed128c]
[a10-cuanschutz01:204392] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb61fe4ea817c]
[a10-cuanschutz01:204392] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xef084f4f73fc]
[a10-cuanschutz01:204392] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xef084f4f74cc]
[a10-cuanschutz01:204392] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb61fe4ea9070]
[a10-cuanschutz01:204392] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204831] *** Process received signal ***
[a10-cuanschutz01:204831] Signal: Aborted (6)
[a10-cuanschutz01:204831] Signal code:  (-6)
[a10-cuanschutz01:204831] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xff5b195009d0]
[a10-cuanschutz01:204831] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xff5ae326f200]
[a10-cuanschutz01:204831] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xff5ae322a67c]
[a10-cuanschutz01:204831] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xff5ae3217130]
[a10-cuanschutz01:204831] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xff5ae3263308]
[a10-cuanschutz01:204831] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xff5ae327957c]
[a10-cuanschutz01:204831] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xff5ae3279ed8]
[a10-cuanschutz01:204831] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xff5ae327b558]
[a10-cuanschutz01:204831] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xff5ae327dc84]
[a10-cuanschutz01:204831] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xff5ae322cecc]
[a10-cuanschutz01:204831] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xff5ae322cf0c]
[a10-cuanschutz01:204831] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xc69b1c08128c]
[a10-cuanschutz01:204831] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xc69b1c05817c]
[a10-cuanschutz01:204831] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xff5ae32173fc]
[a10-cuanschutz01:204831] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xff5ae32174cc]
[a10-cuanschutz01:204831] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xc69b1c059070]
[a10-cuanschutz01:204831] *** End of error message ***
corrupted size vs. prev_size
[a10-cuanschutz01:204440] *** Process received signal ***
[a10-cuanschutz01:204440] Signal: Aborted (6)
[a10-cuanschutz01:204440] Signal code:  (-6)
[a10-cuanschutz01:204440] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xe141001809d0]
[a10-cuanschutz01:204440] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xe140c9eef200]
[a10-cuanschutz01:204440] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xe140c9eaa67c]
[a10-cuanschutz01:204440] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xe140c9e97130]
[a10-cuanschutz01:204440] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xe140c9ee3308]
[a10-cuanschutz01:204440] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xe140c9ef957c]
[a10-cuanschutz01:204440] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xe140c9ef9ed8]
[a10-cuanschutz01:204440] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xe140c9efb558]
[a10-cuanschutz01:204440] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xe140c9efdc84]
[a10-cuanschutz01:204440] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xe140c9eacecc]
[a10-cuanschutz01:204440] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xe140c9eacf0c]
[a10-cuanschutz01:204440] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xc85e2d18128c]
[a10-cuanschutz01:204440] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xc85e2d15817c]
[a10-cuanschutz01:204440] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xe140c9e973fc]
[a10-cuanschutz01:204440] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xe140c9e974cc]
[a10-cuanschutz01:204440] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xc85e2d159070]
[a10-cuanschutz01:204440] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:205103] *** Process received signal ***
[a10-cuanschutz01:205103] Signal: Aborted (6)
[a10-cuanschutz01:205103] Signal code:  (-6)
[a10-cuanschutz01:205103] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf6ede30d09d0]
[a10-cuanschutz01:205103] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf6edace3f200]
[a10-cuanschutz01:205103] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf6edacdfa67c]
[a10-cuanschutz01:205103] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf6edacde7130]
[a10-cuanschutz01:205103] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf6edace33308]
[a10-cuanschutz01:205103] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf6edace4957c]
[a10-cuanschutz01:205103] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf6edace49ed8]
[a10-cuanschutz01:205103] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf6edace4b558]
[a10-cuanschutz01:205103] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf6edace4dc84]
[a10-cuanschutz01:205103] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf6edacdfcecc]
[a10-cuanschutz01:205103] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf6edacdfcf0c]
[a10-cuanschutz01:205103] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb257cee7128c]
[a10-cuanschutz01:205103] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb257cee4817c]
[a10-cuanschutz01:205103] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf6edacde73fc]
[a10-cuanschutz01:205103] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf6edacde74cc]
[a10-cuanschutz01:205103] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb257cee49070]
[a10-cuanschutz01:205103] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204906] *** Process received signal ***
[a10-cuanschutz01:204906] Signal: Aborted (6)
[a10-cuanschutz01:204906] Signal code:  (-6)
[a10-cuanschutz01:204906] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf3104bd209d0]
[a10-cuanschutz01:204906] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf31015a8f200]
[a10-cuanschutz01:204906] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf31015a4a67c]
[a10-cuanschutz01:204906] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf31015a37130]
[a10-cuanschutz01:204906] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf31015a83308]
[a10-cuanschutz01:204906] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf31015a9957c]
[a10-cuanschutz01:204906] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf31015a99ed8]
[a10-cuanschutz01:204906] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf31015a9b558]
[a10-cuanschutz01:204906] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf31015a9dc84]
[a10-cuanschutz01:204906] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf31015a4cecc]
[a10-cuanschutz01:204906] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf31015a4cf0c]
[a10-cuanschutz01:204906] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb8b3f8a8128c]
[a10-cuanschutz01:204906] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb8b3f8a5817c]
[a10-cuanschutz01:204906] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf31015a373fc]
[a10-cuanschutz01:204906] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf31015a374cc]
[a10-cuanschutz01:204906] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb8b3f8a59070]
[a10-cuanschutz01:204906] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204786] *** Process received signal ***
[a10-cuanschutz01:204786] Signal: Aborted (6)
[a10-cuanschutz01:204786] Signal code:  (-6)
[a10-cuanschutz01:204786] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf4128d8509d0]
[a10-cuanschutz01:204786] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf412575bf200]
[a10-cuanschutz01:204786] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf4125757a67c]
[a10-cuanschutz01:204786] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf41257567130]
[a10-cuanschutz01:204786] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf412575b3308]
[a10-cuanschutz01:204786] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf412575c957c]
[a10-cuanschutz01:204786] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf412575c9ed8]
[a10-cuanschutz01:204786] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf412575cb558]
[a10-cuanschutz01:204786] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf412575cdc84]
[a10-cuanschutz01:204786] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf4125757cecc]
[a10-cuanschutz01:204786] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf4125757cf0c]
[a10-cuanschutz01:204786] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb2c69985128c]
[a10-cuanschutz01:204786] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb2c69982817c]
[a10-cuanschutz01:204786] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf412575673fc]
[a10-cuanschutz01:204786] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf412575674cc]
[a10-cuanschutz01:204786] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb2c699829070]
[a10-cuanschutz01:204786] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204414] *** Process received signal ***
[a10-cuanschutz01:204414] Signal: Aborted (6)
[a10-cuanschutz01:204414] Signal code:  (-6)
[a10-cuanschutz01:204414] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xfa3fc04b09d0]
[a10-cuanschutz01:204414] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xfa3f8a21f200]
[a10-cuanschutz01:204414] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xfa3f8a1da67c]
[a10-cuanschutz01:204414] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xfa3f8a1c7130]
[a10-cuanschutz01:204414] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xfa3f8a213308]
[a10-cuanschutz01:204414] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xfa3f8a22957c]
[a10-cuanschutz01:204414] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xfa3f8a229ed8]
[a10-cuanschutz01:204414] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xfa3f8a22b558]
[a10-cuanschutz01:204414] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xfa3f8a22dc84]
[a10-cuanschutz01:204414] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xfa3f8a1dcecc]
[a10-cuanschutz01:204414] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xfa3f8a1dcf0c]
[a10-cuanschutz01:204414] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xc7a757b2128c]
[a10-cuanschutz01:204414] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xc7a757af817c]
[a10-cuanschutz01:204414] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xfa3f8a1c73fc]
[a10-cuanschutz01:204414] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xfa3f8a1c74cc]
[a10-cuanschutz01:204414] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xc7a757af9070]
[a10-cuanschutz01:204414] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204862] *** Process received signal ***
[a10-cuanschutz01:204862] Signal: Aborted (6)
[a10-cuanschutz01:204862] Signal code:  (-6)
[a10-cuanschutz01:204862] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xfd225f8409d0]
[a10-cuanschutz01:204862] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xfd22295af200]
[a10-cuanschutz01:204862] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xfd222956a67c]
[a10-cuanschutz01:204862] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xfd2229557130]
[a10-cuanschutz01:204862] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xfd22295a3308]
[a10-cuanschutz01:204862] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xfd22295b957c]
[a10-cuanschutz01:204862] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xfd22295b9ed8]
[a10-cuanschutz01:204862] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xfd22295bb558]
[a10-cuanschutz01:204862] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xfd22295bdc84]
[a10-cuanschutz01:204862] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xfd222956cecc]
[a10-cuanschutz01:204862] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xfd222956cf0c]
[a10-cuanschutz01:204862] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xad291faf128c]
[a10-cuanschutz01:204862] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xad291fac817c]
[a10-cuanschutz01:204862] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xfd22295573fc]
[a10-cuanschutz01:204862] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xfd22295574cc]
[a10-cuanschutz01:204862] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xad291fac9070]
[a10-cuanschutz01:204862] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204606] *** Process received signal ***
[a10-cuanschutz01:204606] Signal: Aborted (6)
[a10-cuanschutz01:204606] Signal code:  (-6)
[a10-cuanschutz01:204606] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xff2341bf09d0]
[a10-cuanschutz01:204606] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xff230b95f200]
[a10-cuanschutz01:204606] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xff230b91a67c]
[a10-cuanschutz01:204606] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xff230b907130]
[a10-cuanschutz01:204606] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xff230b953308]
[a10-cuanschutz01:204606] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xff230b96957c]
[a10-cuanschutz01:204606] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xff230b969ed8]
[a10-cuanschutz01:204606] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xff230b96b558]
[a10-cuanschutz01:204606] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xff230b96dc84]
[a10-cuanschutz01:204606] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xff230b91cecc]
[a10-cuanschutz01:204606] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xff230b91cf0c]
[a10-cuanschutz01:204606] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xca59d9c3128c]
[a10-cuanschutz01:204606] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xca59d9c0817c]
[a10-cuanschutz01:204606] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xff230b9073fc]
[a10-cuanschutz01:204606] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xff230b9074cc]
[a10-cuanschutz01:204606] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xca59d9c09070]
[a10-cuanschutz01:204606] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204972] *** Process received signal ***
[a10-cuanschutz01:204972] Signal: Aborted (6)
[a10-cuanschutz01:204972] Signal code:  (-6)
[a10-cuanschutz01:204972] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf9ed62ca09d0]
[a10-cuanschutz01:204972] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf9ed2ca0f200]
[a10-cuanschutz01:204972] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf9ed2c9ca67c]
[a10-cuanschutz01:204972] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf9ed2c9b7130]
[a10-cuanschutz01:204972] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf9ed2ca03308]
[a10-cuanschutz01:204972] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf9ed2ca1957c]
[a10-cuanschutz01:204972] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf9ed2ca19ed8]
[a10-cuanschutz01:204972] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf9ed2ca1b558]
[a10-cuanschutz01:204972] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf9ed2ca1dc84]
[a10-cuanschutz01:204972] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf9ed2c9ccecc]
[a10-cuanschutz01:204972] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf9ed2c9ccf0c]
[a10-cuanschutz01:204972] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xbf176fef128c]
[a10-cuanschutz01:204972] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xbf176fec817c]
[a10-cuanschutz01:204972] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf9ed2c9b73fc]
[a10-cuanschutz01:204972] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf9ed2c9b74cc]
[a10-cuanschutz01:204972] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xbf176fec9070]
[a10-cuanschutz01:204972] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204617] *** Process received signal ***
[a10-cuanschutz01:204617] Signal: Aborted (6)
[a10-cuanschutz01:204617] Signal code:  (-6)
[a10-cuanschutz01:204617] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xe7ad6c6009d0]
[a10-cuanschutz01:204617] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xe7ad3636f200]
[a10-cuanschutz01:204617] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xe7ad3632a67c]
[a10-cuanschutz01:204617] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xe7ad36317130]
[a10-cuanschutz01:204617] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xe7ad36363308]
[a10-cuanschutz01:204617] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xe7ad3637957c]
[a10-cuanschutz01:204617] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xe7ad36379ed8]
[a10-cuanschutz01:204617] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xe7ad3637b558]
[a10-cuanschutz01:204617] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xe7ad3637dc84]
[a10-cuanschutz01:204617] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xe7ad3632cecc]
[a10-cuanschutz01:204617] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xe7ad3632cf0c]
[a10-cuanschutz01:204617] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xc8345eca128c]
[a10-cuanschutz01:204617] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xc8345ec7817c]
[a10-cuanschutz01:204617] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xe7ad363173fc]
[a10-cuanschutz01:204617] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xe7ad363174cc]
[a10-cuanschutz01:204617] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xc8345ec79070]
[a10-cuanschutz01:204617] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204630] *** Process received signal ***
[a10-cuanschutz01:204630] Signal: Aborted (6)
[a10-cuanschutz01:204630] Signal code:  (-6)
[a10-cuanschutz01:204630] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xeb7ecb7809d0]
[a10-cuanschutz01:204630] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xeb7e954ef200]
[a10-cuanschutz01:204630] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xeb7e954aa67c]
[a10-cuanschutz01:204630] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xeb7e95497130]
[a10-cuanschutz01:204630] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xeb7e954e3308]
[a10-cuanschutz01:204630] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xeb7e954f957c]
[a10-cuanschutz01:204630] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xeb7e954f9ed8]
[a10-cuanschutz01:204630] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xeb7e954fb558]
[a10-cuanschutz01:204630] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xeb7e954fdc84]
[a10-cuanschutz01:204630] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xeb7e954acecc]
[a10-cuanschutz01:204630] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xeb7e954acf0c]
[a10-cuanschutz01:204630] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb3285f14128c]
[a10-cuanschutz01:204630] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb3285f11817c]
[a10-cuanschutz01:204630] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xeb7e954973fc]
[a10-cuanschutz01:204630] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xeb7e954974cc]
[a10-cuanschutz01:204630] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb3285f119070]
[a10-cuanschutz01:204630] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204696] *** Process received signal ***
[a10-cuanschutz01:204696] Signal: Aborted (6)
[a10-cuanschutz01:204696] Signal code:  (-6)
[a10-cuanschutz01:204696] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xe6180ac109d0]
[a10-cuanschutz01:204696] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xe617d497f200]
[a10-cuanschutz01:204696] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xe617d493a67c]
[a10-cuanschutz01:204696] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xe617d4927130]
[a10-cuanschutz01:204696] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xe617d4973308]
[a10-cuanschutz01:204696] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xe617d498957c]
[a10-cuanschutz01:204696] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xe617d4989ed8]
[a10-cuanschutz01:204696] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xe617d498b558]
[a10-cuanschutz01:204696] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xe617d498dc84]
[a10-cuanschutz01:204696] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xe617d493cecc]
[a10-cuanschutz01:204696] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xe617d493cf0c]
[a10-cuanschutz01:204696] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb3966712128c]
[a10-cuanschutz01:204696] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb396670f817c]
[a10-cuanschutz01:204696] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xe617d49273fc]
[a10-cuanschutz01:204696] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xe617d49274cc]
[a10-cuanschutz01:204696] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb396670f9070]
[a10-cuanschutz01:204696] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:205027] *** Process received signal ***
[a10-cuanschutz01:205027] Signal: Aborted (6)
[a10-cuanschutz01:205027] Signal code:  (-6)
[a10-cuanschutz01:205027] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf496a72409d0]
[a10-cuanschutz01:205027] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf49670faf200]
[a10-cuanschutz01:205027] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf49670f6a67c]
[a10-cuanschutz01:205027] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf49670f57130]
[a10-cuanschutz01:205027] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf49670fa3308]
[a10-cuanschutz01:205027] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf49670fb957c]
[a10-cuanschutz01:205027] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf49670fb9ed8]
[a10-cuanschutz01:205027] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf49670fbb558]
[a10-cuanschutz01:205027] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf49670fbdc84]
[a10-cuanschutz01:205027] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf49670f6cecc]
[a10-cuanschutz01:205027] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf49670f6cf0c]
[a10-cuanschutz01:205027] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xbbfcb14c128c]
[a10-cuanschutz01:205027] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xbbfcb149817c]
[a10-cuanschutz01:205027] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf49670f573fc]
[a10-cuanschutz01:205027] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf49670f574cc]
[a10-cuanschutz01:205027] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xbbfcb1499070]
[a10-cuanschutz01:205027] *** End of error message ***
/workspace/hpl.sh: line 259: 205060 Aborted                 (core dumped) ${NUMCMD} ${CPUBIND} ${MEMBIND} ${XHPL} ${DAT}
--------------------------------------------------------------------------
Primary job  terminated normally, but 1 process returned
a non-zero exit code. Per user-direction, the job has been aborted.
--------------------------------------------------------------------------
/workspace/hpl.sh: line 259: 204727 Aborted                 (core dumped) ${NUMCMD} ${CPUBIND} ${MEMBIND} ${XHPL} ${DAT}
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204487] *** Process received signal ***
[a10-cuanschutz01:204487] Signal: Aborted (6)
[a10-cuanschutz01:204487] Signal code:  (-6)
[a10-cuanschutz01:204487] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf13b998a09d0]
[a10-cuanschutz01:204487] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf13b6360f200]
[a10-cuanschutz01:204487] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf13b635ca67c]
[a10-cuanschutz01:204487] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf13b635b7130]
[a10-cuanschutz01:204487] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf13b63603308]
[a10-cuanschutz01:204487] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf13b6361957c]
[a10-cuanschutz01:204487] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf13b63619ed8]
[a10-cuanschutz01:204487] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf13b6361b558]
[a10-cuanschutz01:204487] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf13b6361dc84]
[a10-cuanschutz01:204487] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf13b635ccecc]
[a10-cuanschutz01:204487] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf13b635ccf0c]
[a10-cuanschutz01:204487] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xadd8f967128c]
[a10-cuanschutz01:204487] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xadd8f964817c]
[a10-cuanschutz01:204487] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf13b635b73fc]
[a10-cuanschutz01:204487] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf13b635b74cc]
[a10-cuanschutz01:204487] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xadd8f9649070]
[a10-cuanschutz01:204487] *** End of error message ***
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:205114] *** Process received signal ***
[a10-cuanschutz01:205114] Signal: Aborted (6)
[a10-cuanschutz01:205114] Signal code:  (-6)
[a10-cuanschutz01:205114] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xfb81603b09d0]
[a10-cuanschutz01:205114] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xfb812a11f200]
[a10-cuanschutz01:205114] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xfb812a0da67c]
[a10-cuanschutz01:205114] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xfb812a0c7130]
[a10-cuanschutz01:205114] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xfb812a113308]
[a10-cuanschutz01:205114] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xfb812a12957c]
[a10-cuanschutz01:205114] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xfb812a129ed8]
[a10-cuanschutz01:205114] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xfb812a12b558]
[a10-cuanschutz01:205114] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xfb812a12dc84]
[a10-cuanschutz01:205114] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xfb812a0dcecc]
[a10-cuanschutz01:205114] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xfb812a0dcf0c]
[a10-cuanschutz01:205114] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb3257aad128c]
[a10-cuanschutz01:205114] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb3257aaa817c]
[a10-cuanschutz01:205114] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xfb812a0c73fc]
[a10-cuanschutz01:205114] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xfb812a0c74cc]
[a10-cuanschutz01:205114] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb3257aaa9070]
[a10-cuanschutz01:205114] *** End of error message ***
/workspace/hpl.sh: line 259: 205103 Aborted                 (core dumped) ${NUMCMD} ${CPUBIND} ${MEMBIND} ${XHPL} ${DAT}
/workspace/hpl.sh: line 259: 205082 Aborted                 (core dumped) ${NUMCMD} ${CPUBIND} ${MEMBIND} ${XHPL} ${DAT}
/workspace/hpl.sh: line 259: 204961 Aborted                 (core dumped) ${NUMCMD} ${CPUBIND} ${MEMBIND} ${XHPL} ${DAT}
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204873] *** Process received signal ***
[a10-cuanschutz01:204873] Signal: Aborted (6)
[a10-cuanschutz01:204873] Signal code:  (-6)
[a10-cuanschutz01:204873] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xe27c498e09d0]
[a10-cuanschutz01:204873] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xe27c1364f200]
[a10-cuanschutz01:204873] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xe27c1360a67c]
[a10-cuanschutz01:204873] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xe27c135f7130]
[a10-cuanschutz01:204873] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xe27c13643308]
[a10-cuanschutz01:204873] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xe27c1365957c]
[a10-cuanschutz01:204873] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xe27c13659ed8]
[a10-cuanschutz01:204873] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xe27c1365b558]
[a10-cuanschutz01:204873] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xe27c1365dc84]
[a10-cuanschutz01:204873] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xe27c1360cecc]
[a10-cuanschutz01:204873] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xe27c1360cf0c]
[a10-cuanschutz01:204873] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xc7d1d42f128c]
[a10-cuanschutz01:204873] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xc7d1d42c817c]
[a10-cuanschutz01:204873] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xe27c135f73fc]
[a10-cuanschutz01:204873] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xe27c135f74cc]
[a10-cuanschutz01:204873] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xc7d1d42c9070]
[a10-cuanschutz01:204873] *** End of error message ***
/workspace/hpl.sh: line 259: 204562 Aborted                 (core dumped) ${NUMCMD} ${CPUBIND} ${MEMBIND} ${XHPL} ${DAT}
HPL ERROR: CUBLAS initialization failed
corrupted size vs. prev_size
[a10-cuanschutz01:204641] *** Process received signal ***
[a10-cuanschutz01:204641] Signal: Aborted (6)
[a10-cuanschutz01:204641] Signal code:  (-6)
[a10-cuanschutz01:204641] [ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0xf067f68109d0]
[a10-cuanschutz01:204641] [ 1] /lib/aarch64-linux-gnu/libc.so.6(+0x7f200)[0xf067c057f200]
[a10-cuanschutz01:204641] [ 2] /lib/aarch64-linux-gnu/libc.so.6(raise+0x1c)[0xf067c053a67c]
[a10-cuanschutz01:204641] [ 3] /lib/aarch64-linux-gnu/libc.so.6(abort+0xe4)[0xf067c0527130]
[a10-cuanschutz01:204641] [ 4] /lib/aarch64-linux-gnu/libc.so.6(+0x73308)[0xf067c0573308]
[a10-cuanschutz01:204641] [ 5] /lib/aarch64-linux-gnu/libc.so.6(+0x8957c)[0xf067c058957c]
[a10-cuanschutz01:204641] [ 6] /lib/aarch64-linux-gnu/libc.so.6(+0x89ed8)[0xf067c0589ed8]
[a10-cuanschutz01:204641] [ 7] /lib/aarch64-linux-gnu/libc.so.6(+0x8b558)[0xf067c058b558]
[a10-cuanschutz01:204641] [ 8] /lib/aarch64-linux-gnu/libc.so.6(free+0xb0)[0xf067c058dc84]
[a10-cuanschutz01:204641] [ 9] /lib/aarch64-linux-gnu/libc.so.6(+0x3cecc)[0xf067c053cecc]
[a10-cuanschutz01:204641] [10] /lib/aarch64-linux-gnu/libc.so.6(+0x3cf0c)[0xf067c053cf0c]
[a10-cuanschutz01:204641] [11] /workspace/hpl-linux-aarch64-gpu/xhpl(+0xa128c)[0xb6749c93128c]
[a10-cuanschutz01:204641] [12] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x7817c)[0xb6749c90817c]
[a10-cuanschutz01:204641] [13] /lib/aarch64-linux-gnu/libc.so.6(+0x273fc)[0xf067c05273fc]
[a10-cuanschutz01:204641] [14] /lib/aarch64-linux-gnu/libc.so.6(__libc_start_main+0x98)[0xf067c05274cc]
[a10-cuanschutz01:204641] [15] /workspace/hpl-linux-aarch64-gpu/xhpl(+0x79070)[0xb6749c909070]
[a10-cuanschutz01:204641] *** End of error message ***
/workspace/hpl.sh: line 259: 204522 Aborted                 (core dumped) ${NUMCMD} ${CPUBIND} ${MEMBIND} ${XHPL} ${DAT}
/workspace/hpl.sh: line 259: 205016 Aborted                 (core dumped) ${NUMCMD} ${CPUBIND} ${MEMBIND} ${XHPL} ${DAT}
/workspace/hpl.sh: line 259: 205092 Aborted                 (core dumped) ${NUMCMD} ${CPUBIND} ${MEMBIND} ${XHPL} ${DAT}
--------------------------------------------------------------------------
mpirun detected that one or more processes exited with non-zero status, thus causing
the job to be terminated. The first process to do so was:

  Process name: [[50202,1],9]
  Exit code:    134
-------------------------------------------------------
```
Looks like there is an issue with CUBLAS.
