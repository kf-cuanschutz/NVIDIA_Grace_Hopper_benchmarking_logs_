### Ran the tinygrad example MNIST:
------------------------------------

Links to tinygrad [here](https://docs.tinygrad.org/mnist/) and [here](https://github.com/tinygrad/tinygrad/tree/master).
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

Stable diffusion not working

```bash
python3 examples/stable_diffusion.py

(tiny_grad_env) a10-kfotso@a10-cuanschutz01:~/benchmarking_/tiny_grad/tinygrad$ python3 examples/stable_diffusion.py
ram used:  4.26 GB, cond_stage_model.transformer.text_model.final_layer_norm.bias: 100%|████████████████████████████████████████████████████████████████████████████████████| 1131/1131 [00:00<00:00, 2105.27it/s]
loaded weights in 540.05 ms, 4.26 GB loaded at 7.90 GB/s
got CLIP context (1, 77, 768)
got unconditional CLIP context (1, 77, 768)
running for [1, 201, 401, 601, 801] timesteps
  0%|                                                                                                                                                                                       | 0/5 [00:00<?, ?it/s]4 errors generated.
Traceback (most recent call last):
  File "/home/a10-kfotso/benchmarking_/tiny_grad/tinygrad/examples/stable_diffusion.py", line 274, in <module>
    latent = run(model, unconditional_context, context, latent, Tensor([timestep]), alphas[tid], alphas_prev[tid], Tensor([args.guidance]))
  File "/home/a10-kfotso/benchmarking_/tiny_grad/tinygrad/tinygrad/engine/jit.py", line 172, in __call__
    self.ret = self.fxn(*args, **kwargs)
  File "/home/a10-kfotso/benchmarking_/tiny_grad/tinygrad/examples/stable_diffusion.py", line 265, in run
    def run(model, *x): return model(*x).realize()
  File "/home/a10-kfotso/benchmarking_/tiny_grad/tinygrad/examples/stable_diffusion.py", line 200, in __call__
    return x_prev.realize()
  File "/home/a10-kfotso/benchmarking_/tiny_grad/tinygrad/tinygrad/tensor.py", line 3167, in _wrapper
    ret = fn(*args, **kwargs)
  File "/home/a10-kfotso/benchmarking_/tiny_grad/tinygrad/tinygrad/tensor.py", line 203, in realize
    run_schedule(*self.schedule_with_vars(*lst), do_update_stats=do_update_stats)
  File "/home/a10-kfotso/benchmarking_/tiny_grad/tinygrad/tinygrad/engine/realize.py", line 223, in run_schedule
    for ei in lower_schedule(schedule):
  File "/home/a10-kfotso/benchmarking_/tiny_grad/tinygrad/tinygrad/engine/realize.py", line 216, in lower_schedule
    raise e
  File "/home/a10-kfotso/benchmarking_/tiny_grad/tinygrad/tinygrad/engine/realize.py", line 210, in lower_schedule
    try: yield lower_schedule_item(si)
  File "/home/a10-kfotso/benchmarking_/tiny_grad/tinygrad/tinygrad/engine/realize.py", line 194, in lower_schedule_item
    runner = get_runner(si.outputs[0].device, si.ast)
  File "/home/a10-kfotso/benchmarking_/tiny_grad/tinygrad/tinygrad/engine/realize.py", line 164, in get_runner
    method_cache[ckey] = method_cache[bkey] = ret = CompiledRunner(replace(prg, dname=dname))
  File "/home/a10-kfotso/benchmarking_/tiny_grad/tinygrad/tinygrad/engine/realize.py", line 82, in __init__
    self.lib:bytes = precompiled if precompiled is not None else Device[p.dname].compiler.compile_cached(p.src)
  File "/home/a10-kfotso/benchmarking_/tiny_grad/tinygrad/tinygrad/device.py", line 183, in compile_cached
    lib = self.compile(src)
  File "/home/a10-kfotso/benchmarking_/tiny_grad/tinygrad/tinygrad/runtime/ops_gpu.py", line 26, in compile
    raise CompileError(f"OpenCL Compile Error\n\n{mstr.value.decode()}")
tinygrad.device.CompileError: OpenCL Compile Error

<kernel>:39:38: error: call to 'exp2' is ambiguous
    data0[alu1] = (float)((cast1*(1/(exp2((cast1*((half)(-1.4426950408889634))))+(half)(1.0)))));
                                     ^~~~
cl_kernel.h:1473:24: note: candidate function
float __OVERLOADABLE__ exp2(float);
                       ^
cl_kernel.h:1474:25: note: candidate function
double __OVERLOADABLE__ exp2(double);
                        ^
cl_kernel.h:1475:25: note: candidate function
float2 __OVERLOADABLE__ exp2(float2); 
                        ^
cl_kernel.h:1477:25: note: candidate function
float3 __OVERLOADABLE__ exp2(float3); 
                        ^
cl_kernel.h:1479:25: note: candidate function
float4 __OVERLOADABLE__ exp2(float4); 
                        ^
cl_kernel.h:1480:25: note: candidate function
float8 __OVERLOADABLE__ exp2(float8); 
                        ^
cl_kernel.h:1481:26: note: candidate function
float16 __OVERLOADABLE__ exp2(float16); 
                         ^
cl_kernel.h:1482:26: note: candidate function
double2 __OVERLOADABLE__ exp2(double2); 
                         ^
cl_kernel.h:1484:26: note: candidate function
double3 __OVERLOADABLE__ exp2(double3); 
                         ^
cl_kernel.h:1486:26: note: candidate function
double4 __OVERLOADABLE__ exp2(double4); 
                         ^
cl_kernel.h:1487:26: note: candidate function
double8 __OVERLOADABLE__ exp2(double8); 
                         ^
cl_kernel.h:1488:27: note: candidate function
double16 __OVERLOADABLE__ exp2(double16); 
                          ^
<kernel>:40:38: error: call to 'exp2' is ambiguous
    data0[alu2] = (float)((cast2*(1/(exp2((cast2*((half)(-1.4426950408889634))))+(half)(1.0)))));
                                     ^~~~
cl_kernel.h:1473:24: note: candidate function
float __OVERLOADABLE__ exp2(float);
                       ^
cl_kernel.h:1474:25: note: candidate function
double __OVERLOADABLE__ exp2(double);
                        ^
cl_kernel.h:1475:25: note: candidate function
float2 __OVERLOADABLE__ exp2(float2); 
                        ^
cl_kernel.h:1477:25: note: candidate function
float3 __OVERLOADABLE__ exp2(float3); 
                        ^
cl_kernel.h:1479:25: note: candidate function
float4 __OVERLOADABLE__ exp2(float4); 
                        ^
cl_kernel.h:1480:25: note: candidate function
float8 __OVERLOADABLE__ exp2(float8); 
                        ^
cl_kernel.h:1481:26: note: candidate function
float16 __OVERLOADABLE__ exp2(float16); 
                         ^
cl_kernel.h:1482:26: note: candidate function
double2 __OVERLOADABLE__ exp2(double2); 
                         ^
cl_kernel.h:1484:26: note: candidate function
double3 __OVERLOADABLE__ exp2(double3); 
                         ^
cl_kernel.h:1486:26: note: candidate function
double4 __OVERLOADABLE__ exp2(double4); 
                         ^
cl_kernel.h:1487:26: note: candidate function
double8 __OVERLOADABLE__ exp2(double8); 
                         ^
cl_kernel.h:1488:27: note: candidate function
double16 __OVERLOADABLE__ exp2(double16); 
                          ^
<kernel>:41:38: error: call to 'exp2' is ambiguous
    data0[alu3] = (float)((cast3*(1/(exp2((cast3*((half)(-1.4426950408889634))))+(half)(1.0)))));
                                     ^~~~
cl_kernel.h:1473:24: note: candidate function
float __OVERLOADABLE__ exp2(float);
                       ^
cl_kernel.h:1474:25: note: candidate function
double __OVERLOADABLE__ exp2(double);
                        ^
cl_kernel.h:1475:25: note: candidate function
float2 __OVERLOADABLE__ exp2(float2); 
                        ^
cl_kernel.h:1477:25: note: candidate function
float3 __OVERLOADABLE__ exp2(float3); 
                        ^
cl_kernel.h:1479:25: note: candidate function
float4 __OVERLOADABLE__ exp2(float4); 
                        ^
cl_kernel.h:1480:25: note: candidate function
float8 __OVERLOADABLE__ exp2(float8); 
                        ^
cl_kernel.h:1481:26: note: candidate function
float16 __OVERLOADABLE__ exp2(float16); 
                         ^
cl_kernel.h:1482:26: note: candidate function
double2 __OVERLOADABLE__ exp2(double2); 
                         ^
cl_kernel.h:1484:26: note: candidate function
double3 __OVERLOADABLE__ exp2(double3); 
                         ^
cl_kernel.h:1486:26: note: candidate function
double4 __OVERLOADABLE__ exp2(double4); 
                         ^
cl_kernel.h:1487:26: note: candidate function
double8 __OVERLOADABLE__ exp2(double8); 
                         ^
cl_kernel.h:1488:27: note: candidate function
double16 __OVERLOADABLE__ exp2(double16); 
                          ^
<kernel>:42:38: error: call to 'exp2' is ambiguous
    data0[alu0] = (float)((cast0*(1/(exp2((cast0*((half)(-1.4426950408889634))))+(half)(1.0)))));
                                     ^~~~
cl_kernel.h:1473:24: note: candidate function
float __OVERLOADABLE__ exp2(float);
                       ^
cl_kernel.h:1474:25: note: candidate function
double __OVERLOADABLE__ exp2(double);
                        ^
cl_kernel.h:1475:25: note: candidate function
float2 __OVERLOADABLE__ exp2(float2); 
                        ^
cl_kernel.h:1477:25: note: candidate function
float3 __OVERLOADABLE__ exp2(float3); 
                        ^
cl_kernel.h:1479:25: note: candidate function
float4 __OVERLOADABLE__ exp2(float4); 
                        ^
cl_kernel.h:1480:25: note: candidate function
float8 __OVERLOADABLE__ exp2(float8); 
                        ^
cl_kernel.h:1481:26: note: candidate function
float16 __OVERLOADABLE__ exp2(float16); 
                         ^
cl_kernel.h:1482:26: note: candidate function
double2 __OVERLOADABLE__ exp2(double2); 
                         ^
cl_kernel.h:1484:26: note: candidate function
double3 __OVERLOADABLE__ exp2(double3); 
                         ^
cl_kernel.h:1486:26: note: candidate function
double4 __OVERLOADABLE__ exp2(double4); 
                         ^
cl_kernel.h:1487:26: note: candidate function
double8 __OVERLOADABLE__ exp2(double8); 
                         ^
cl_kernel.h:1488:27: note: candidate function
double16 __OVERLOADABLE__ exp2(double16); 

```


I ran tinygrad GAN:

```bash
DEBUG=3 python examples/mnist_gan.py

*** GPU     5426454 r_16_16_8_16_128_4_4_4n1               mem  0.07 GB tm    390.40us/473979.31ms (  1393.98 GFLOPS   24.2|1391.3  GB/s) ['leakyrelu', 'leakyrelu bw', 'dropout', 'dot bw', 'dropout bw', '__add__']
*** GPU     5426455 r_4_49_32_4_256_4_4_4n2                mem  0.07 GB tm    622.18us/473979.94ms (  1325.17 GFLOPS   13.7|1326.5  GB/s) ['tanh bw', 'dot bw']
*** GPU     5426456 r_16_16_8_16_196_4_4_4n1               mem  0.07 GB tm    641.47us/473980.58ms (  1289.73 GFLOPS   14.0|1288.1  GB/s) ['leakyrelu', 'leakyrelu bw', 'dot bw', '__add__']
*** GPU     5426457 r_49_16_4_16_128_4_4_4                 mem  0.07 GB tm    167.97us/473980.75ms (  4894.29 GFLOPS   41.2|4913.4  GB/s) ['dot bw']
*** GPU     5426458 r_16_8_8_16_256_4_4_4n1                mem  0.07 GB tm    383.97us/473981.13ms (  1405.05 GFLOPS   16.4|1403.7  GB/s) ['leakyrelu', 'leakyrelu bw', 'dot bw', '__add__']
*** GPU     5426459 r_32_8_8_16_128_4_4_4                  mem  0.07 GB tm    152.00us/473981.28ms (  3532.05 GFLOPS   34.5|3545.8  GB/s) ['dot bw']
*** GPU     5426460 E_32_49_8_16_4                         mem  0.07 GB tm     26.53us/473981.31ms (    90.79 GFLOPS  363.2|363.2   GB/s) ['__rmul__', '__add__']
*** GPU     5426461 E_32_49_8_16_4n1                       mem  0.07 GB tm     25.12us/473981.33ms (   127.84 GFLOPS  383.5|383.5   GB/s) ['__rmul__', '__mul__', '__add__']
*** GPU     5426462 r_16_4_8_16_128_4_4_4n1                mem  0.07 GB tm    122.02us/473981.46ms (  1110.74 GFLOPS   21.5|1108.6  GB/s) ['leakyrelu', 'leakyrelu bw', 'dot bw', '__add__']
*** GPU     5426463 r_16_4_8_16_128_4_4_4n2                mem  0.07 GB tm     95.23us/473981.55ms (  1409.38 GFLOPS   22.0|1414.9  GB/s) ['dot bw']
*** GPU     5426464 E_64_16_8_16_4n2                       mem  0.06 GB tm     13.50us/473981.56ms (   116.47 GFLOPS  465.9|465.9   GB/s) ['__rmul__', '__add__']
*** GPU     5426465 E_64_16_8_16_4n3                       mem  0.06 GB tm     13.38us/473981.58ms (   156.78 GFLOPS  470.4|470.4   GB/s) ['__rmul__', '__mul__', '__add__']
*** GPU     5426466 E_6272_32_4n5                          mem  0.06 GB tm     18.59us/473981.60ms (   399.42 GFLOPS  690.9|820.4   GB/s) ['__truediv__', '__truediv__', 'sqrt', '__add__', '__truediv__', '__mul__', '__sub__']
*** GPU     5426467 r_8_2_8_16_128_4_4_4                   mem  0.06 GB tm     98.43us/473981.69ms (   340.89 GFLOPS    9.3|342.2   GB/s) ['dot bw']
*** GPU     5426468 E_32_8_8_16_4n2                        mem  0.06 GB tm      8.35us/473981.70ms (    47.08 GFLOPS  188.3|188.3   GB/s) ['__rmul__', '__add__']
*** GPU     5426469 E_32_8_8_16_4n3                        mem  0.06 GB tm      7.68us/473981.71ms (    68.27 GFLOPS  204.8|204.8   GB/s) ['__rmul__', '__mul__', '__add__']
*** GPU     5426470 E_4096_32_4n7                          mem  0.06 GB tm     13.92us/473981.72ms (   348.40 GFLOPS  602.6|715.6   GB/s) ['__truediv__', '__truediv__', 'sqrt', '__add__', '__truediv__', '__mul__', '__sub__']
*** GPU     5426471 E_16_4_8_16_4n2                        mem  0.06 GB tm      6.46us/473981.73ms (    15.21 GFLOPS   60.8|60.8    GB/s) ['__rmul__', '__add__']
*** GPU     5426472 E_16_4_8_16_4n3                        mem  0.06 GB tm      6.50us/473981.74ms (    20.18 GFLOPS   60.5|60.5    GB/s) ['__rmul__', '__mul__', '__add__']
*** GPU     5426473 E_1024_32_4n7                          mem  0.06 GB tm      7.81us/473981.75ms (   155.28 GFLOPS  268.6|319.0   GB/s) ['__truediv__', '__truediv__', 'sqrt', '__add__', '__truediv__', '__mul__', '__sub__']
*** GPU     5426474 E_256_32_4n2                           mem  0.06 GB tm      7.36us/473981.75ms (    41.18 GFLOPS   71.2|84.6    GB/s) ['__truediv__', '__truediv__', 'sqrt', '__add__', '__truediv__', '__mul__', '__sub__']
*** GPU     5426475 E_4_32_4n3                             mem  0.06 GB tm      6.59us/473981.76ms (     0.16 GFLOPS    0.6|0.6     GB/s) ['log_softmax']
*** GPU     5426476 r_256_2_2n2                            mem  0.06 GB tm      6.37us/473981.77ms (    11.14 GFLOPS    1.9|43.4    GB/s) ['log_softmax', '__mul__', 'mean']
*** CLANG   5426477 copy        4,   CLANG <- GPU          mem  0.06 GB tm     35.23us/473981.80ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     5426478 r_2_4_8_16_32_4_4_4                    mem  0.06 GB tm     23.49us/473981.82ms (   182.06 GFLOPS    9.8|181.4   GB/s) ['dot', 'leakyrelu']
*** GPU     5426479 r_2_8_8_16_64_4_4_4                    mem  0.06 GB tm     34.24us/473981.86ms (   494.77 GFLOPS   21.1|493.8   GB/s) ['dot', 'leakyrelu']
*** GPU     5426480 r_2_16_8_16_128_4_4_4                  mem  0.06 GB tm     91.07us/473981.95ms (   740.48 GFLOPS   27.3|739.8   GB/s) ['dot', 'leakyrelu']
*** GPU     5426481 r_49_16_4_256_4_4_4                    mem  0.06 GB tm    148.93us/473982.10ms (   692.02 GFLOPS   24.7|691.3   GB/s) ['dot', 'tanh']
*** CLANG   5426482 copy   200704,   CLANG <- GPU          mem  0.06 GB tm     64.06us/473982.16ms (     0.00 GFLOPS    3.1|0.0     GB/s) 
Generator loss: 1.3740071058273315, Discriminator loss: 0.9452890753746033: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 300/300 [59:45<00:00,  0.08it/s]
Training Completed!
avg:  1422.23 GFLOPS    31.69 GB/s           total: 5426482 kernels 674113.69 GOPS 15022.08 GB 473982.16 ms
```
