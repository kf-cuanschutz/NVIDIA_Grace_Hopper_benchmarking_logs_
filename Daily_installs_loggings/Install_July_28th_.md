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
