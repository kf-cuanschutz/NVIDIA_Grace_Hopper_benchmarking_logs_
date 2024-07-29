Install_log:
------------

* Successfully installed petsc.

```bash
[horovod_env] a10-kfotso@a10-cuanschutz01:~/spack$  spack env create petsc
==> Created environment petsc in: /home/a10-kfotso/spack/spack/var/spack/environments/petsc
==> Activate with: spack env activate petsc
[horovod_env] a10-kfotso@a10-cuanschutz01:~/spack$ despacktivate
a10-kfotso@a10-cuanschutz01:~/spack$ spacktivate -p petsc
[petsc] a10-kfotso@a10-cuanschutz01:~/spack$ spack list '*petsc*'
petsc  py-petsc4py
==> 2 packages
[petsc] a10-kfotso@a10-cuanschutz01:~/spack$ spack install --add petsc^C
[petsc] a10-kfotso@a10-cuanschutz01:~/spack$ spack install --add petsc
==> Concretized 1 spec
 -   zbmgc2d  petsc@3.21.3%gcc@11.4.0~
==> Installing petsc-3.21.3-zbmgc2dhs2mo4ia7qvwvakzzytl2ai3d [45/45]
==> No binary for petsc-3.21.3-zbmgc2dhs2mo4ia7qvwvakzzytl2ai3d found: installing from source
==> Fetching http://web.cels.anl.gov/projects/petsc/download/release-snapshots/petsc-3.21.3.tar.gz
==> No patches needed for petsc
==> petsc: Executing phase: 'configure'
==> petsc: Executing phase: 'build'
==> petsc: Executing phase: 'install'
==> petsc: Successfully installed petsc-3.21.3-zbmgc2dhs2mo4ia7qvwvakzzytl2ai3d
  Stage: 2.19s.  Configure: 3m 2.70s.  Build: 24.53s.  Install: 0.97s.  Post-install: 1.31s.  Total: 3m 31.84s
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/petsc-3.21.3-zbmgc2dhs2mo4ia7qvwvakzzytl2ai3d
==> Updating view at /home/a10-kfotso/spack/spack/var/spack/environments/petsc/.spack-env/view
```

* Installed hpc toolkit

```bash
a10-kfotso@a10-cuanschutz01:~/spack$ spack env create hpctoolkit_cuda
==> Created environment hpctoolkit_cuda in: /home/a10-kfotso/spack/spack/var/spack/environments/hpctoolkit_cuda
==> Activate with: spack env activate hpctoolkit_cuda
a10-kfotso@a10-cuanschutz01:~/spack$ spacktivate -p hpctoolkit_cuda
[hpctoolkit_cuda] a10-kfotso@a10-cuanschutz01:~/spack$ spack install --add hpctoolkit +cuda 
==> Concretized 1 spec
 -   qze5q6l  hpctoolkit@2024.01.1%gcc@11.4.0~cray+cuda~debug~level_zero~mpi~opencl+papi~python~rocm+viewer build_system=autotools arch=linux-ubuntu22.04-neoverse_v2
[+]  eufptuo      ^autoconf@2.72%gcc@11.4.0 build_system=autotools arch=linux-ubuntu22.04-neoverse_v2
[+]  avqird5          ^m4@1.4.19%gcc@11.4.0+sigsegv build_system=autotools patches=9dc5fbd,bfdffa7 arch=linux-ubuntu22.04-neoverse_v2
[+]  fxzbzyp              ^libsigsegv@2.14%gcc@11.4.0 build_system=autotools arch=linux-ubuntu22.04-neoverse_v2
[+]  nvjoca3          ^perl@5.38.2%gcc@11.4.0+cpanm+opcode+open+shared+threads build_system=generic arch=linux-ubuntu22.04-neoverse_v2
[+]  u6uwac4              ^berkeley-db@18.1.40%gcc@11.4.0+cxx~docs+stl build_system=autotools patches=26090f4,b231fcc arch=linux-ubuntu22.04-neoverse_v2
[+]  ul5srcv              ^gdbm@1.23%gcc@11.4.0 build_system=autotools arch=linux-ubuntu22.04-neoverse_v2
[+]  7ogvkdu                  ^readline@8.2%gcc@11.4.0 build_system=autotools patches=bbf97f1 arch=linux-ubuntu22.04-neoverse_v2
[+]  bsngu3v      ^automake@1.16.5%gcc@11.4.0 build_system=autotools arch=linux-ubuntu22.04-neoverse_v2
[+]  scemr2v      ^boost@1.85.0%gcc@11.4.0+atomic+chrono~clanglibcpp~container~context~contract~coroutine+date_time~debug~exception~fiber+filesystem+graph~graph_parallel~icu~iostreams~json~locale~log~math~mpi+multithreaded~nowide~numpy~pic~program_options~python~random+regex~serialization+shared~signals~singlethreaded~stacktrace+system~taggedlayout~test+thread+timer~type_erasure~versionedlayout~wave build_system=generic cxxstd=11 patches=a440f96 visibility=global arch=linux-ubuntu22.04-neoverse_v2
[+]  htzsjvp      ^bzip2@1.0.8%gcc@11.4.0~debug~pic+shared build_system=generic arch=linux-ubuntu22.04-neoverse_v2
[+]  fliy6rl          ^diffutils@3.10%gcc@11.4.0 build_system=autotools arch=linux-ubuntu22.04-neoverse_v2
[+]  km6x5wu      ^cuda@12.5.1%gcc@11.4.0~allow-unsupported-compilers~dev build_system=generic arch=linux-ubuntu22.04-neoverse_v2
[+]  6m35i67          ^libxml2@2.10.3%gcc@11.4.0+pic~python+shared build_system=autotools arch=linux-ubuntu22.04-neoverse_v2
[+]  gay3rhm      ^dyninst@13.0.0%gcc@11.4.0~ipo+openmp~stat_dysect~static build_system=cmake build_type=Release generator=make arch=linux-ubuntu22.04-neoverse_v2
[+]  tsr7iwo          ^cmake@3.29.6%gcc@11.4.0~doc+ncurses+ownlibs build_system=generic build_type=Release patches=dbc3892 arch=linux-ubuntu22.04-neoverse_v2
[+]  chizrqv              ^ncurses@6.5%gcc@11.4.0~symlinks+termlib abi=none build_system=autotools patches=7a351bc arch=linux-ubuntu22.04-neoverse_v2
[+]  gjbrmm7      ^elfutils@0.190%gcc@11.4.0~debuginfod+exeprefix~nls build_system=autotools arch=linux-ubuntu22.04-neoverse_v2
[+]  japagtp          ^pkgconf@2.2.0%gcc@11.4.0 build_system=autotools arch=linux-ubuntu22.04-neoverse_v2
[+]  dasks5n          ^zstd@1.5.6%gcc@11.4.0+programs build_system=makefile compression=none libs=shared,static arch=linux-ubuntu22.04-neoverse_v2
[+]  l6h4twh      ^gcc-runtime@11.4.0%gcc@11.4.0 build_system=generic arch=linux-ubuntu22.04-neoverse_v2
[e]  rxmgmi2      ^glibc@2.35%gcc@11.4.0 build_system=autotools arch=linux-ubuntu22.04-neoverse_v2
[+]  p3tf5z6      ^gmake@4.4.1%gcc@11.4.0~guile build_system=generic arch=linux-ubuntu22.04-neoverse_v2
[+]  ysqp2pd      ^gnuconfig@2022-09-17%gcc@11.4.0 build_system=generic arch=linux-ubuntu22.04-neoverse_v2
[+]  3oamlyz      ^hpcviewer@2024.02%gcc@11.4.0 build_system=generic arch=linux-ubuntu22.04-neoverse_v2
[+]  pkqzgsd          ^openjdk@17.0.11_9%gcc@11.4.0 build_system=generic arch=linux-ubuntu22.04-neoverse_v2
[+]  5t5oica      ^intel-tbb@2021.12.0%gcc@11.4.0~ipo+shared+tm build_system=cmake build_type=Release cxxstd=default generator=make arch=linux-ubuntu22.04-neoverse_v2
[+]  4xlx5is          ^hwloc@2.9.3%gcc@11.4.0~cairo~cuda~gl~libudev+libxml2~netloc~nvml~oneapi-level-zero~opencl+pci~rocm build_system=autotools libs=shared,static arch=linux-ubuntu22.04-neoverse_v2
[+]  u4ii7d7              ^libpciaccess@0.17%gcc@11.4.0 build_system=autotools arch=linux-ubuntu22.04-neoverse_v2
[+]  qgaswnf                  ^util-macros@1.20.1%gcc@11.4.0 build_system=autotools arch=linux-ubuntu22.04-neoverse_v2
[+]  lovx6yy      ^libiberty@2.41%gcc@11.4.0+pic build_system=autotools arch=linux-ubuntu22.04-neoverse_v2
[+]  jq3uyjc      ^libmonitor@2023.03.15%gcc@11.4.0~commrank~dlopen+hpctoolkit build_system=autotools arch=linux-ubuntu22.04-neoverse_v2
[+]  rxaft4i      ^libtool@2.4.7%gcc@11.4.0 build_system=autotools arch=linux-ubuntu22.04-neoverse_v2
[+]  bcsdesr          ^findutils@4.9.0%gcc@11.4.0 build_system=autotools patches=440b954 arch=linux-ubuntu22.04-neoverse_v2
[+]  pilwcrj      ^libunwind@1.6.2%gcc@11.4.0~block_signals~conservative_checks~cxx_exceptions~debug~debug_frame+docs~pic+tests+weak_backtrace+xz~zlib build_system=autotools components=none libs=shared,static arch=linux-ubuntu22.04-neoverse_v2
[+]  hefxq3l      ^papi@7.1.0%gcc@11.4.0~cuda~debug+example~infiniband~lmsensors~nvml~powercap~rapl~rocm~rocm_smi~sde+shared~static_tools build_system=autotools patches=48cb202 arch=linux-ubuntu22.04-neoverse_v2
[+]  zbejvl7      ^xerces-c@3.2.5%gcc@11.4.0 build_system=autotools cxxstd=default netaccessor=curl transcoder=iconv arch=linux-ubuntu22.04-neoverse_v2
[+]  jgl64lf          ^curl@8.7.1%gcc@11.4.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2+nghttp2 build_system=autotools libs=shared,static tls=openssl arch=linux-ubuntu22.04-neoverse_v2
[+]  ugkla5k              ^nghttp2@1.62.0%gcc@11.4.0 build_system=autotools arch=linux-ubuntu22.04-neoverse_v2
[+]  tvgbeze              ^openssl@3.3.1%gcc@11.4.0~docs+shared build_system=generic certs=mozilla arch=linux-ubuntu22.04-neoverse_v2
[+]  5jjomw3                  ^ca-certificates-mozilla@2023-05-30%gcc@11.4.0 build_system=generic arch=linux-ubuntu22.04-neoverse_v2
[+]  2gpu6ki      ^xz@5.4.6%gcc@11.4.0~pic build_system=autotools libs=shared,static arch=linux-ubuntu22.04-neoverse_v2
[+]  cqgw4ov      ^yaml-cpp@0.7.0%gcc@11.4.0~ipo+pic+shared~tests build_system=cmake build_type=Release generator=make arch=linux-ubuntu22.04-neoverse_v2
[+]  mldkqch      ^zlib@1.3.1%gcc@11.4.0+optimize+pic+shared build_system=makefile arch=linux-ubuntu22.04-neoverse_v2

[+] /usr (external glibc-2.35-rxmgmi2lpetiqurcupi3ii2jhdphh3w2)
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/gcc-runtime-11.4.0-l6h4twhuoxi3yvh6qmql2rohcv5dv7yc
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/bzip2-1.0.8-htzsjvp7ywog3vsd3irxm5xnbjjvjkj3
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/papi-7.1.0-hefxq3lypy5qppfnpk4w44y3pdvqd2fq
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/ncurses-6.5-chizrqvo3i5wyvdbo6ps5apltscolpvq
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/yaml-cpp-0.7.0-cqgw4ovjstkrkltk6jkh5zansggvtq6j
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/xz-5.4.6-2gpu6kir75qdgy43d2mx3ibo575fbtwx
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/openjdk-17.0.11_9-pkqzgsdadhdfw7dloyyxe64ctqzo7qjc
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/libsigsegv-2.14-fxzbzyp3v6fg23wjazzrtfkdqmpajsu6
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/libmonitor-2023.03.15-jq3uyjcbtlyckxe3pmshlteugbohun4p
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/nghttp2-1.62.0-ugkla5ki64xmr7ozdp7j744vmdlvdqhb
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/boost-1.85.0-scemr2vfjtaioxvidbgrihi7u6zrjssw
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/zlib-1.3.1-mldkqchxuqjsjfunxxqy5veegrp2i6fp
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/findutils-4.9.0-bcsdesrzpvxrw52khukej4a3qclalzgd
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/libpciaccess-0.17-u4ii7d7yrpk5aojnrajcel655xtcji2p
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/berkeley-db-18.1.40-u6uwac4jo4pwh52s3kzarzo264hsbo4m
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/zstd-1.5.6-dasks5npkv5ns4yzcfkes4b5gfvzsnsx
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/gnuconfig-2022-09-17-ysqp2pdst367qahoooook3lytmv2lc6y
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/gmake-4.4.1-p3tf5z6thwfxnav22qtrknf6cxtobbjl
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/hpcviewer-2024.02-3oamlyzrgfiuhr62d3nhve7cgih3tfqx
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/libxml2-2.10.3-6m35i67yd3vbplgzfgjotliiwuyic4js
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/libtool-2.4.7-rxaft4ib5atetghxvnufsg5rzefoplrn
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/m4-1.4.19-avqird52ab4ungwrclh25byinxjafoau
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/openssl-3.3.1-tvgbezeutbafwgsejnssjsbo3d4ri3in
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/libiberty-2.41-lovx6yy3pzoamksdzyylqtktxg5zktu6
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/readline-8.2-7ogvkdusm5igpdsfmspz2eiw2kqeqad4
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/libunwind-1.6.2-pilwcrj7umfj5xrwpo6prk7ijopp5prf
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/pkgconf-2.2.0-japagtporebgefmxqoyhrvmx5sifqjhm
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/cuda-12.5.1-km6x5wujysbjs4h5zyzclcsislyniyhn
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/gdbm-1.23-ul5srcvk56d64lnrfyay2llyrzd7ddrs
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/elfutils-0.190-gjbrmm75p6x4ukr7ywjgikpq5rpl6rwv
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/hwloc-2.9.3-4xlx5is6ptxgxjbw7senxifuexppw6p6
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/curl-8.7.1-jgl64lfvpwnxv7byngpvsz7khcqq7ygt
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/perl-5.38.2-nvjoca33g34quhszsyplgqlitb7u56qu
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/intel-tbb-2021.12.0-5t5oicawuqjydtecexblk33g44vxh76a
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/xerces-c-3.2.5-zbejvl76nlpjfeqx2rfwhsu43ffwkcqq
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/automake-1.16.5-bsngu3vawabt5o3idxeeuclnywy3l4vb
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/autoconf-2.72-eufptuorl4xyjihpskahug7utmkpfby5
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/dyninst-13.0.0-gay3rhmqoiw7c3qhwwb7yxil5yvpm27z
==> Installing hpctoolkit-2024.01.1-qze5q6lfi4vtmreuaawdvlwfhmgnt6kx [40/40]
==> No binary for hpctoolkit-2024.01.1-qze5q6lfi4vtmreuaawdvlwfhmgnt6kx found: installing from source
==> Using cached archive: /home/a10-kfotso/spack/spack/var/spack/cache/_source-cache/git//hpctoolkit/hpctoolkit.git/0672b9a9a2a1e3846c5e2059fb73a07a129f22cd.tar.gz
==> Warning: Fetching from mirror without a checksum!
  This package is normally checked out from a version control system, but it has been archived on a spack mirror.  This means we cannot know a checksum for the tarball in advance. Be sure that your connection to this mirror is secure!
==> No patches needed for hpctoolkit
==> hpctoolkit: Executing phase: 'autoreconf'
==> hpctoolkit: Executing phase: 'configure'
==> hpctoolkit: Executing phase: 'build'
==> hpctoolkit: Executing phase: 'install'
==> hpctoolkit: Successfully installed hpctoolkit-2024.01.1-qze5q6lfi4vtmreuaawdvlwfhmgnt6kx
  Stage: 0.26s.  Autoreconf: 3.99s.  Configure: 10.43s.  Build: 58.00s.  Install: 1.11s.  Post-install: 0.11s.  Total: 1m 14.01s
[+] /home/a10-kfotso/spack/spack/opt/spack/linux-ubuntu22.04-neoverse_v2/gcc-11.4.0/hpctoolkit-2024.01.1-qze5q6lfi4vtmreuaawdvlwfhmgnt6kx
==> Updating view at /home/a10-kfotso/spack/spack/var/spack/environments/hpctoolkit_cuda/.spack-env/view

```
