Install loggings:
-----------------


 Package downloaded from [here](http://www.htslib.org/download/)
 
``bash
./configure --prefix=/home/a10-kfotso/samtools/install --without-curses --disable-bz2 --disable-lzma
make
make install
export PATH=/home/a10-kfotso/samtools/install:$PATH
```
