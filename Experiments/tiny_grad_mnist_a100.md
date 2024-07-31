#BATCH_SIZE=128

```bash

 DEBUG=2 BEAM=2  python mnist.py

jit execs 45 kernels
*** GPU     315971 E_                                       mem  0.12 GB tm      5.12us/ 13752.00ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315972 E_n1                                     mem  0.12 GB tm      5.12us/ 13752.00ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** CUSTOM  315973 custom_random                            mem  0.12 GB 
*** GPU     315974 r_125_32_60000_3_5                       mem  0.12 GB tm      6.14us/ 13752.01ms (    11.72 GFLOPS   39.1|39.1    GB/s) 
*** CUSTOM  315975 custom_random                            mem  0.12 GB 
*** GPU     315976 r_10_10n1                                mem  0.12 GB tm      4.10us/ 13752.01ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315977 E_n2                                     mem  0.12 GB tm      5.12us/ 13752.02ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315978 E_n2                                     mem  0.12 GB tm      4.10us/ 13752.02ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315979 E_64_2                                   mem  0.12 GB tm      5.12us/ 13752.03ms (     0.10 GFLOPS    0.2|0.2     GB/s) 
*** GPU     315980 r_20_112_16_2_4_375_4_7_2                mem  0.12 GB tm   1147.90us/ 13753.18ms ( 12045.25 GFLOPS   44.7|1122.2  GB/s) 
*** GPU     315981 r_250_32_16_15_4                         mem  0.12 GB tm      9.22us/ 13753.18ms (  4222.22 GFLOPS   36.1|2263.9  GB/s) 
*** GPU     315982 r_392_32_4_40_2                          mem  0.12 GB tm      9.22us/ 13753.19ms (   435.56 GFLOPS  446.4|446.4   GB/s) 
*** GPU     315983 r2_64_2_250                              mem  0.12 GB tm      6.14us/ 13753.20ms (  1307.29 GFLOPS    5.3|1338.5  GB/s) 
*** GPU     315984 r_64_2_13_13_2_3_16_2_2_3                mem  0.12 GB tm     15.36us/ 13753.22ms (  3605.33 GFLOPS  727.7|2591.3  GB/s) 
*** GPU     315985 r_16_8                                   mem  0.12 GB tm      7.17us/ 13753.22ms (     0.06 GFLOPS    0.0|0.2     GB/s) 
*** GPU     315986 r_1664_13_2_2_2_16                       mem  0.12 GB tm     10.24us/ 13753.23ms (   270.40 GFLOPS 1352.0|1352.0  GB/s) 
*** GPU     315987 r_3328_13_2_2_16                         mem  0.12 GB tm     10.24us/ 13753.24ms (  1081.60 GFLOPS 1622.4|1622.4  GB/s) 
*** GPU     315988 r_4_128_11_4_16_2_3_3_11_4               mem  0.12 GB tm     99.33us/ 13753.34ms (  8622.19 GFLOPS   68.5|15473.5 GB/s) 
*** GPU     315989 r_512_16_2_2_5_5                         mem  0.12 GB tm      9.22us/ 13753.35ms (   177.78 GFLOPS  519.1|1066.7  GB/s) 
*** GPU     315990 r_512_5_16_2_2_5                         mem  0.12 GB tm     12.29us/ 13753.36ms (   266.67 GFLOPS  400.0|400.0   GB/s) 
*** GPU     315991 E_320_32_4_5                             mem  0.12 GB tm      6.14us/ 13753.37ms (   133.33 GFLOPS  400.0|400.0   GB/s) 
*** GPU     315992 r_32_10_2_16_4_25_2                      mem  0.12 GB tm      9.22us/ 13753.38ms (  1022.22 GFLOPS   96.4|3697.8  GB/s) 
*** GPU     315993 r_4_32_10                                mem  0.12 GB tm      5.12us/ 13753.38ms (     0.23 GFLOPS    1.1|1.1     GB/s) 
*** GPU     315994 r_4_32_10n1                              mem  0.12 GB tm      6.14us/ 13753.39ms (     0.81 GFLOPS    1.0|1.0     GB/s) 
*** GPU     315995 r_8_16_10                                mem  0.12 GB tm      5.12us/ 13753.40ms (     1.02 GFLOPS    1.2|1.2     GB/s) 
*** GPU     315996 r_2_32_10_2                              mem  0.12 GB tm      5.12us/ 13753.40ms (     0.00 GFLOPS    0.1|0.1     GB/s) 
*** GPU     315997 r_128_10n1                               mem  0.12 GB tm      7.17us/ 13753.41ms (     1.96 GFLOPS    1.0|1.8     GB/s) 
*** GPU     315998 E_8_5_16_2                               mem  0.12 GB tm      5.12us/ 13753.41ms (     2.75 GFLOPS    2.5|4.0     GB/s) 
*** GPU     315999 r3_10_16_8n1                             mem  0.12 GB tm      5.12us/ 13753.42ms (     1.28 GFLOPS    1.0|4.2     GB/s) 
*** GPU     316000 r_16_50_16_8_10_2                        mem  0.12 GB tm      7.17us/ 13753.42ms (   685.71 GFLOPS  238.2|1942.9  GB/s) 
*** GPU     316001 E_512_5_16_2_2_5                         mem  0.12 GB tm     12.29us/ 13753.44ms (   366.67 GFLOPS  789.3|933.3   GB/s) 
*** GPU     316002 r3_2_100_16_8_16_5                       mem  0.12 GB tm      8.19us/ 13753.45ms (   878.12 GFLOPS  147.5|2175.0  GB/s) 
*** GPU     316003 E_8_11_64_4_11_4                         mem  0.12 GB tm     24.58us/ 13753.47ms (    74.25 GFLOPS  454.7|454.7   GB/s) 
*** GPU     316004 r3_64_121_128n1                          mem  0.12 GB tm      9.22us/ 13753.48ms (   223.51 GFLOPS  430.4|870.5   GB/s) 
*** GPU     316005 r_32_2_128_8_3_64_4_3_2                  mem  0.12 GB tm     86.02us/ 13753.57ms (  7021.71 GFLOPS  254.4|6070.9  GB/s) 
*** GPU     316006 r_8_32_13_2_13_4_4_4_2                   mem  0.12 GB tm     17.41us/ 13753.58ms (   775.41 GFLOPS 1184.1|2704.0  GB/s) 
*** GPU     316007 r3_16_16_3_2_11_4_32_11_3_2_2            mem  0.12 GB tm    157.70us/ 13753.74ms (  3929.57 GFLOPS   45.5|5881.7  GB/s) 
*** GPU     316008 E_2048_2_13_13_2_2                       mem  0.12 GB tm     25.60us/ 13753.77ms (   865.28 GFLOPS 1189.8|2163.2  GB/s) 
*** GPU     316009 r_4_128_3_2_26_26_3_4                    mem  0.12 GB tm     21.50us/ 13753.79ms (  3476.57 GFLOPS  526.6|6826.9  GB/s) 
*** GPU     316010 r_8_128_4_4_169                          mem  0.12 GB tm     11.26us/ 13753.80ms (   251.64 GFLOPS  984.7|1018.2  GB/s) 
*** GPU     316011 r3_144_2_16_8                            mem  0.12 GB tm      6.14us/ 13753.80ms (    30.75 GFLOPS   25.1|102.0   GB/s) 
*** GPU     316012 r3_32_16_8n1                             mem  0.12 GB tm      5.12us/ 13753.81ms (     4.10 GFLOPS    3.4|13.6    GB/s) 
*** GPU     316013 E_32_4n1                                 mem  0.12 GB tm      5.12us/ 13753.82ms (     0.05 GFLOPS    0.2|0.2     GB/s) 
*** GPU     316014 r_16_8n1                                 mem  0.12 GB tm      6.14us/ 13753.82ms (     0.06 GFLOPS    0.0|0.2     GB/s) 
*** GPU     316015 r_64_2_10                                mem  0.12 GB tm      6.14us/ 13753.83ms (     2.20 GFLOPS    1.1|4.7     GB/s) 
avg:  8611.70 GFLOPS   141.40 GB/s           total: 316015 kernels 118443.78 GOPS  1944.79 GB 13753.83 ms
```

