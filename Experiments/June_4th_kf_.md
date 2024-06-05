Benchmarking:
==============

* Benchmarked the Pi example with float32 precision.

```bash
python calculate_pi_gpu_opt_clean.py 100000000000
```
Results in --> ```numba.cuda.cudadrv.driver.CudaAPIError: [2] Call to cuMemAlloc results in CUDA_ERROR_OUT_OF_MEMORY```

```bash
python calculate_pi_gpu_opt_clean.py 10000000000
```
Results in --> ```numba.cuda.cudadrv.driver.CudaAPIError: [2] Call to cuMemAlloc results in CUDA_ERROR_OUT_OF_MEMORY```

```bash
python calculate_pi_gpu_opt_clean.py 1000000000
```
Results in --> ```Pi = 3.14154419200000001311, (Diff=-0.00004846158979310289) (calculated in 12.747416 secs with 1000000000 steps)
```

```bash
python calculate_pi_gpu_opt_clean.py 100000000
```
Results in --> ```Pi = 3.14159423999999987132, (Diff=0.00000158641020675532) (calculated in 1.377563 secs with 100000000 steps))```

```bash
python calculate_pi_gpu_opt_clean.py 10000000
```
Results in --> ```Pi = 3.14159379999999988087, (Diff=0.00000114641020676487) (calculated in 0.256684 secs with 10000000 steps)))```

```bash
python calculate_pi_gpu_opt_clean.py 10000000
```
Results in --> ```Pi = 3.14159299999999985786, (Diff=0.00000034641020674187) (calculated in 0.140953 secs with 1000000 steps)```


```bash
python calculate_pi_gpu_opt_clean.py 100000
```
Results in --> ```Pi = 3.14159250259399414062, (Diff=-0.00000023841857910156) (calculated in 0.155593 secs with 10000 steps)```

```bash
python calculate_pi_gpu_opt_clean.py 10000
```

** To do: Perhaps profile it with nsys and nprof and then compare it with A100 benchmarking. There is room for improvement in the code kernel utilization which was low (<10%)
** The original code was fetched from [here](https://github.com/kf-cuanschutz/gpu_programming_December_2023/blob/main/calculate_pi_gpu_opt_clean.py)
