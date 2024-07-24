# Install logs:
---------------


* spack install logs located here ```/tmp/a10-kfotso/spack-stage/spack-stage-gmake-4.4.1-6fyejvsdyi37vk5mh4zls6pou67sstu2/spack-src/spack-build/config.log```
I am getting this:

```bash
configure:4260: /home/a10-kfotso/spack/spack/lib/spack/env/c++ --version >&5
[spack cc] ERROR: Compiler 'gcc@=12.3.0' does not have a C++ compiler configured.
configure:4271: $? = 1
configure:4260: /home/a10-kfotso/spack/spack/lib/spack/env/c++ -v >&5
[spack cc] ERROR: Compiler 'gcc@=12.3.0' does not have a C++ compiler configured.
configure:4271: $? = 1
configure:4362: error: in `/tmp/a10-kfotso/spack-stage/spack-stage-gmake-4.4.1-6fyejvsdyi37vk5mh4zls6pou67sstu2/spack-src/spack-build':
configure:4364: error: C compiler cannot create executables
```

* This indicates that clearly, gcc@=12.3.0 compiler is at fault here. More information about the nature of the fault following this [thread](https://stackoverflow.com/questions/67899951/change-version-of-gcc-which-does-not-support-compiling-c-programs-using-the-co)

* Our " ~/.spack/linux/compilers.yaml" file currently shows the following below:

```bash
/home/a10-kfotso/containers_img_

compilers:
- compiler:
  spec: gcc@=11.4.0
  paths:
   cc: /usr/bin/gcc
   cxx: /usr/bin/g++
   f77: /usr/bin/gfortran
   fc: /usr/bin/gfortran
  flags: {}
  operating_system: ubuntu22.04
  target: aarch64
  modules: []
  environment: {}
  extra_rpaths: []
- compiler:
  spec: gcc@=12.3.0
  paths:
   cc: /usr/bin/gcc-12
   cxx: null
   f77: null
   fc: null
  flags: {}
  operating_system: ubuntu22.04
  target: aarch64
  modules: []
  environment: {}
  extra_rpaths: []
```

So I removed the gcc@=12.3.0 compiler block and then ran the following:

```bash
a10-kfotso@a10-cuanschutz01:~/spack$ spack compiler list 
==> Available compilers
-- gcc ubuntu22.04-aarch64 --------------------------------------
gcc@11.4.0
```
This confirm that we have removed the nonC++ compatible compiler.

Finally it looks like the zlib installation works.

```bash
a10-kfotso@a10-cuanschutz01:~/spack$ spack install nvhpc
[+] /usr (external glibc-2.35-rxmgmi2lpetiqurcupi3ii2jhdphh3w2)
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/gcc-runtime-11.4.0-l6h4twhuoxi3yvh6qmql2rohcv5dv7yc
==> Installing nvhpc-24.5-lwy544yxfvbzqufhsdp5mubg2swkt74j [3/3]
==> No binary for nvhpc-24.5-lwy544yxfvbzqufhsdp5mubg2swkt74j found: installing from source
==> Fetching https://developer.download.nvidia.com/hpc-sdk/24.5/nvhpc_2024_245_Linux_aarch64_cuda_multi.tar.gz
==> No patches needed for nvhpc
==> nvhpc: Executing phase: 'install'
==> nvhpc: Successfully installed nvhpc-24.5-lwy544yxfvbzqufhsdp5mubg2swkt74j
  Stage: 3m 33.36s.  Install: 17.05s.  Post-install: 13.76s.  Total: 4m 4.18s
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/nvhpc-24.5-lwy544yxfvbzqufhsdp5mubg2swkt74j

```
