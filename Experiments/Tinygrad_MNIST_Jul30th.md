### Ran the tinygrad example MNIST:
------------------------------------

```bash
DEBUG=2 python mnist.py 

*** GPU     315970 r_16_8_10                              mem  0.12 GB tm      7.46us/ 65512.16ms (     1.28 GFLOPS    0.9|1.8     GB/s) 
jit execs 45 kernels
*** GPU     315971 E_                                     mem  0.12 GB tm      4.64us/ 65512.17ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315972 E_n1                                   mem  0.12 GB tm      4.26us/ 65512.17ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** CUSTOM  315973 custom_random                          mem  0.12 GB 
*** GPU     315974 r_625_32_15000_3_4                     mem  0.12 GB tm      6.94us/ 65512.18ms (   164.17 GFLOPS   34.6|34.6    GB/s) 
*** CUSTOM  315975 custom_random                          mem  0.12 GB 
*** GPU     315976 r_5_2_10n1                             mem  0.12 GB tm      6.91us/ 65512.18ms (     0.04 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315977 E_n2                                   mem  0.12 GB tm      4.00us/ 65512.19ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315978 E_n2                                   mem  0.12 GB tm      4.48us/ 65512.19ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315979 E_32_4                                 mem  0.12 GB tm      3.58us/ 65512.20ms (     0.14 GFLOPS    0.3|0.3     GB/s) 
*** GPU     315980 r_8_49_5_4_4_8_375_4_4_4               mem  0.12 GB tm   4037.28us/ 65516.23ms (  3728.45 GFLOPS   12.7|747.7   GB/s) 
*** GPU     315981 r_125_32_2_60_4_4                      mem  0.12 GB tm     18.11us/ 65516.25ms (  1696.11 GFLOPS   18.4|538.9   GB/s) 
*** GPU     315982 r_3136_32_10_4                         mem  0.12 GB tm     14.27us/ 65516.27ms (   281.26 GFLOPS  288.3|288.3   GB/s) 
*** GPU     315983 r2_4_32_250                            mem  0.12 GB tm      6.08us/ 65516.27ms (     5.28 GFLOPS    5.4|5.4     GB/s) 
*** GPU     315984 r_32_13_13_8_2_2_4_4_3_3               mem  0.12 GB tm     72.90us/ 65516.35ms (   721.70 GFLOPS  153.3|617.2   GB/s) 
*** GPU     315985 r_16_8                                 mem  0.12 GB tm      4.03us/ 65516.35ms (     0.10 GFLOPS    0.0|0.3     GB/s) 
*** GPU     315986 r_1664_13_32_2_2                       mem  0.12 GB tm     51.04us/ 65516.40ms (    40.69 GFLOPS  271.2|271.2   GB/s) 
*** GPU     315987 r_416_13_32_4_2_2                      mem  0.12 GB tm     73.02us/ 65516.47ms (   142.19 GFLOPS  227.5|227.5   GB/s) 
*** GPU     315988 r_4_11_11_8_16_32_4_4_3_3              mem  0.12 GB tm    579.90us/ 65517.05ms (   987.98 GFLOPS   11.7|993.1   GB/s) 
*** GPU     315989 r_256_5_5_32_2_2                       mem  0.12 GB tm     21.34us/ 65517.07ms (    28.79 GFLOPS  191.9|191.9   GB/s) 
*** GPU     315990 r_64_5_5_32_4_2_2                      mem  0.12 GB tm     28.32us/ 65517.10ms (   108.47 GFLOPS  173.6|173.6   GB/s) 
*** GPU     315991 E_1600_32_4                            mem  0.12 GB tm      7.30us/ 65517.11ms (   112.28 GFLOPS  336.8|336.8   GB/s) 
*** GPU     315992 r_128_10_16_100                        mem  0.12 GB tm     41.76us/ 65517.15ms (   106.42 GFLOPS   21.3|429.6   GB/s) 
*** GPU     315993 r_4_32_10                              mem  0.12 GB tm      4.03us/ 65517.16ms (     0.29 GFLOPS    1.4|1.4     GB/s) 
*** GPU     315994 r_4_32_10n1                            mem  0.12 GB tm      4.32us/ 65517.16ms (     1.16 GFLOPS    1.4|1.4     GB/s) 
*** GPU     315995 r_4_32_10n2                            mem  0.12 GB tm      4.22us/ 65517.16ms (     1.21 GFLOPS    1.5|1.5     GB/s) 
*** GPU     315996 r_4_32_10n3                            mem  0.12 GB tm      3.71us/ 65517.17ms (     2.10 GFLOPS    0.5|2.0     GB/s) 
*** GPU     315997 r_4_32_10n4                            mem  0.12 GB tm      4.00us/ 65517.17ms (     3.52 GFLOPS    1.8|3.2     GB/s) 
*** GPU     315998 E_5_32_2_4                             mem  0.12 GB tm      4.10us/ 65517.18ms (     5.31 GFLOPS    3.2|9.7     GB/s) 
*** GPU     315999 r3_10_16_8n1                           mem  0.12 GB tm      3.78us/ 65517.18ms (     1.74 GFLOPS    1.4|5.8     GB/s) 
*** GPU     316000 r_4_25_8_16_4_4_10                     mem  0.12 GB tm      7.87us/ 65517.19ms (   598.37 GFLOPS  216.9|728.5   GB/s) 
*** GPU     316001 E_64_5_5_32_2_2_4                      mem  0.12 GB tm     77.92us/ 65517.27ms (    63.08 GFLOPS  124.5|210.3   GB/s) 
*** GPU     316002 r3_5_25_2_16_32_4_4n1                  mem  0.12 GB tm     15.17us/ 65517.28ms (   287.18 GFLOPS   79.7|703.6   GB/s) 
*** GPU     316003 E_16_11_11_8_16_4                      mem  0.12 GB tm     84.90us/ 65517.37ms (    32.11 GFLOPS  132.0|140.1   GB/s) 
*** GPU     316004 r3_64_16_8_121n1                       mem  0.12 GB tm     29.98us/ 65517.40ms (    34.19 GFLOPS  132.3|135.8   GB/s) 
*** GPU     316005 r_16_2_121_2_16_3_16_4_3_4             mem  0.12 GB tm    378.56us/ 65517.77ms (  1508.21 GFLOPS   57.8|1806.7  GB/s) 
*** GPU     316006 r_16_2_13_13_8_16_4_4                  mem  0.12 GB tm    124.22us/ 65517.90ms (   339.92 GFLOPS  165.9|378.9   GB/s) 
*** GPU     316007 r3_8_2_2_16_3_128_11_4_3_11n1          mem  0.12 GB tm   2645.31us/ 65520.54ms (   215.95 GFLOPS    2.7|186.6   GB/s) 
*** GPU     316008 E_32_13_13_32_2_2_4                    mem  0.12 GB tm    269.15us/ 65520.81ms (    82.30 GFLOPS  113.2|205.7   GB/s) 
*** GPU     316009 r_32_8_3_4_26_4_3_26                   mem  0.12 GB tm    102.21us/ 65520.92ms (   487.63 GFLOPS  110.8|348.4   GB/s) 
*** GPU     316010 r_4_8_8_16_169_4                       mem  0.12 GB tm     18.72us/ 65520.93ms (   147.91 GFLOPS  592.5|592.5   GB/s) 
*** GPU     316011 r3_288_16_8n1                          mem  0.12 GB tm      4.54us/ 65520.94ms (    41.58 GFLOPS   34.0|137.9   GB/s) 
*** GPU     316012 r3_32_16_8n1                           mem  0.12 GB tm      4.03us/ 65520.94ms (     5.21 GFLOPS    4.3|17.3    GB/s) 
*** GPU     316013 E_32_4n1                               mem  0.12 GB tm      4.48us/ 65520.95ms (     0.06 GFLOPS    0.2|0.2     GB/s) 
*** GPU     316014 r_16_8n1                               mem  0.12 GB tm      4.51us/ 65520.95ms (     0.09 GFLOPS    0.0|0.3     GB/s) 
*** GPU     316015 r_16_8_10                              mem  0.12 GB tm      8.35us/ 65520.96ms (     1.14 GFLOPS    0.8|1.6     GB/s) 
avg:  1872.42 GFLOPS    29.55 GB/s           total: 316015 kernels 122682.53 GOPS  1936.39 GB 65520.96 ms

```
