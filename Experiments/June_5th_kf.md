Benchmarking:
==============

* Benchmarked the Pi example with float64 precision.

```bash
python  calculate_pi_gpu_opt_clean_float64.py 1000000000
```
Results in --> ```Pi = 3.14159265358980155369, (Diff=0.00000000000000843769) (calculated in 27.445787 secs with 1000000000 steps)```

```bash
python calculate_pi_gpu_opt_clean_float64.py 100000000
```
Results in --> ```Pi = 3.14159265358978467830, (Diff=-0.00000000000000843769) (calculated in 2.899764 secs with 100000000 steps))```

```bash
python calculate_pi_gpu_opt_clean_float64.py 10000000
```
Results in --> ```Pi = 3.14159265358979045146, (Diff=-0.00000000000000266454) (calculated in 0.400337 secs with 10000000 steps)))```

```bash
python calculate_pi_gpu_opt_clean_float64.py 1000000
```
Results in --> ```Pi = 3.14159265358987749295, (Diff=0.00000000000008437695) (calculated in 0.160656 secs with 1000000 steps))))```

```bash
python calculate_pi_gpu_opt_clean_float64.py 100000
```
Results in --> ```Pi = 3.14159265358987749295, (Diff=0.00000000000008437695) (calculated in 0.160656 secs with 100000 steps))))```


```bash
python calculate_pi_gpu_opt_clean_float64.py 10000
```
Results in --> ```Pi = 3.14159265442312651828, (Diff=0.00000000083333340228) (calculated in 0.127680 secs with 10000 steps)))))```



