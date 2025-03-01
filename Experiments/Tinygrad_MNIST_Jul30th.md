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

# Ran tinygrad with optimization:

```bash
 DEBUG=2 BEAM=2  python mnist.py


jit execs 45 kernels
*** GPU     315926 E_                                     mem  0.12 GB tm      3.68us/ 30622.38ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315927 E_n1                                   mem  0.12 GB tm      3.55us/ 30622.38ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** CUSTOM  315928 custom_random                          mem  0.12 GB 
*** GPU     315929 r_75_32_60000_5_5                      mem  0.12 GB tm      6.30us/ 30622.39ms (    10.66 GFLOPS   38.1|38.1    GB/s) 
*** CUSTOM  315930 custom_random                          mem  0.12 GB 
*** GPU     315931 r_5_2_10n1                             mem  0.12 GB tm      6.43us/ 30622.40ms (     0.05 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315932 E_n2                                   mem  0.12 GB tm      4.29us/ 30622.40ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315933 E_n2                                   mem  0.12 GB tm      3.36us/ 30622.40ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315934 E_32_4                                 mem  0.12 GB tm      4.16us/ 30622.41ms (     0.12 GFLOPS    0.2|0.2     GB/s) 
*** GPU     315935 r_20_98_16_2_1500_4_4_2_2              mem  0.12 GB tm   3071.17us/ 30625.48ms (  4411.19 GFLOPS   16.7|369.6   GB/s) 
*** GPU     315936 r_250_16_16_4_15_2                     mem  0.12 GB tm     13.25us/ 30625.49ms (  2898.55 GFLOPS   25.1|1212.6  GB/s) 
*** GPU     315937 r_1568_16_4_10_4                       mem  0.12 GB tm     10.27us/ 30625.50ms (   547.09 GFLOPS  400.5|625.2   GB/s) 
*** GPU     315938 r2_32_4_250                            mem  0.12 GB tm      4.83us/ 30625.51ms (  1662.25 GFLOPS    6.8|1702.0  GB/s) 
*** GPU     315939 r_8_13_8_13_2_2_3_3_16_4               mem  0.12 GB tm     23.68us/ 30625.53ms (  2338.59 GFLOPS  472.0|1023.1  GB/s) 
*** GPU     315940 r_64_2                                 mem  0.12 GB tm      5.18us/ 30625.54ms (     0.84 GFLOPS    0.0|3.3     GB/s) 
*** GPU     315941 r_1664_8_13_2_2_4                      mem  0.12 GB tm     17.86us/ 30625.55ms (   116.30 GFLOPS  775.3|775.3   GB/s) 
*** GPU     315942 r_1664_2_13_2_4_2_2_2                  mem  0.12 GB tm     13.57us/ 30625.57ms (   765.28 GFLOPS 1224.5|1224.5  GB/s) 
*** GPU     315943 r_8_128_11_2_16_2_3_11_4_3             mem  0.12 GB tm    248.00us/ 30625.82ms (  3453.32 GFLOPS   27.5|5499.7  GB/s) 
*** GPU     315944 r_512_5_16_2_2_5                       mem  0.12 GB tm     12.99us/ 30625.83ms (   252.22 GFLOPS  368.2|1765.5  GB/s) 
*** GPU     315945 r_512_5_16_2_2_5n1                     mem  0.12 GB tm     14.72us/ 30625.84ms (   389.57 GFLOPS  380.7|1780.9  GB/s) 
*** GPU     315946 E_800_8_16_2                           mem  0.12 GB tm      5.98us/ 30625.85ms (   136.90 GFLOPS  410.7|410.7   GB/s) 
*** GPU     315947 r_64_5_16_4_2_2_25                     mem  0.12 GB tm      8.90us/ 30625.86ms (  1049.78 GFLOPS   99.9|3370.4  GB/s) 
*** GPU     315948 r_64_2_10                              mem  0.12 GB tm      3.68us/ 30625.86ms (     0.35 GFLOPS    1.5|1.5     GB/s) 
*** GPU     315949 r_64_2_10n1                            mem  0.12 GB tm      3.87us/ 30625.87ms (     1.32 GFLOPS    1.6|1.6     GB/s) 
*** GPU     315950 r_4_32_10n2                            mem  0.12 GB tm      3.71us/ 30625.87ms (     1.38 GFLOPS    1.7|1.7     GB/s) 
*** GPU     315951 r_2_16_4_10                            mem  0.12 GB tm      4.00us/ 30625.87ms (     1.98 GFLOPS    0.4|1.8     GB/s) 
*** GPU     315952 r_8_8_2_10                             mem  0.12 GB tm      4.26us/ 30625.88ms (     3.34 GFLOPS    1.7|3.0     GB/s) 
*** GPU     315953 E_8_5_16_2                             mem  0.12 GB tm      3.71us/ 30625.88ms (     5.52 GFLOPS    3.5|8.4     GB/s) 
*** GPU     315954 r3_10_16_8n1                           mem  0.12 GB tm      3.84us/ 30625.88ms (     1.71 GFLOPS    1.4|5.7     GB/s) 
*** GPU     315955 r_2_25_4_16_4_4_4_10                   mem  0.12 GB tm      6.53us/ 30625.89ms (   721.57 GFLOPS  261.6|878.4   GB/s) 
*** GPU     315956 E_5_512_16_2_2_5                       mem  0.12 GB tm     19.74us/ 30625.91ms (   228.20 GFLOPS  491.3|580.9   GB/s) 
*** GPU     315957 r3_25_5_8_4_4_8_2_2_4                  mem  0.12 GB tm      7.17us/ 30625.92ms (   752.23 GFLOPS  168.6|1562.5  GB/s) 
*** GPU     315958 E_8_32_11_2_2_11_4_2                   mem  0.12 GB tm     40.45us/ 30625.96ms (    44.84 GFLOPS  276.3|276.3   GB/s) 
*** GPU     315959 r3_64_121_128n1                        mem  0.12 GB tm      6.27us/ 30625.96ms (   328.43 GFLOPS  632.4|1279.1  GB/s) 
*** GPU     315960 r_32_32_8_3_4_16_4_4_3_4               mem  0.12 GB tm    175.26us/ 30626.14ms (  3446.11 GFLOPS  124.8|2405.1  GB/s) 
*** GPU     315961 r_128_13_2_2_13_4_4_4_2                mem  0.12 GB tm     32.42us/ 30626.17ms (   416.41 GFLOPS  635.9|1452.1  GB/s) 
*** GPU     315962 r3_8_16_3_2_2_11_128_11_3_4            mem  0.12 GB tm    225.25us/ 30626.40ms (  2559.14 GFLOPS   31.9|3022.9  GB/s) 
*** GPU     315963 E_128_13_13_2_4_2_2_2_2                mem  0.12 GB tm     33.63us/ 30626.43ms (   617.47 GFLOPS  905.6|1152.6  GB/s) 
*** GPU     315964 r_128_4_3_2_26_26_4_3                  mem  0.12 GB tm     27.68us/ 30626.46ms (  2700.87 GFLOPS  409.1|5303.6  GB/s) 
*** GPU     315965 r_4_128_8_4_169                        mem  0.12 GB tm     12.06us/ 30626.47ms (   234.95 GFLOPS  919.4|950.7   GB/s) 
*** GPU     315966 r3_288_16_8n1                          mem  0.12 GB tm      4.51us/ 30626.48ms (    41.87 GFLOPS   34.2|138.9   GB/s) 
*** GPU     315967 r3_8_4_32_4                            mem  0.12 GB tm      4.00us/ 30626.48ms (    13.57 GFLOPS    4.3|47.1    GB/s) 
*** GPU     315968 E_32_4n1                               mem  0.12 GB tm      5.09us/ 30626.48ms (     0.05 GFLOPS    0.2|0.2     GB/s) 
*** GPU     315969 r_8_16                                 mem  0.12 GB tm      4.13us/ 30626.49ms (     0.05 GFLOPS    0.0|0.1     GB/s) 
*** GPU     315970 r_64_2_10n2                            mem  0.12 GB tm      5.50us/ 30626.49ms (     2.45 GFLOPS    1.2|5.3     GB/s) 
jit execs 45 kernels
*** GPU     315971 E_                                     mem  0.12 GB tm      4.48us/ 30626.50ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315972 E_n1                                   mem  0.12 GB tm      4.58us/ 30626.50ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** CUSTOM  315973 custom_random                          mem  0.12 GB 
*** GPU     315974 r_75_32_60000_5_5                      mem  0.12 GB tm      5.50us/ 30626.51ms (    12.21 GFLOPS   43.6|43.6    GB/s) 
*** CUSTOM  315975 custom_random                          mem  0.12 GB 
*** GPU     315976 r_5_2_10n1                             mem  0.12 GB tm      5.57us/ 30626.51ms (     0.05 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315977 E_n2                                   mem  0.12 GB tm      4.54us/ 30626.52ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315978 E_n2                                   mem  0.12 GB tm      4.35us/ 30626.52ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315979 E_32_4                                 mem  0.12 GB tm      4.29us/ 30626.53ms (     0.12 GFLOPS    0.2|0.2     GB/s) 
*** GPU     315980 r_20_98_16_2_1500_4_4_2_2              mem  0.12 GB tm   3075.84us/ 30629.60ms (  4404.49 GFLOPS   16.7|369.0   GB/s) 
*** GPU     315981 r_250_16_16_4_15_2                     mem  0.12 GB tm     13.25us/ 30629.62ms (  2898.55 GFLOPS   25.1|1212.6  GB/s) 
*** GPU     315982 r_1568_16_4_10_4                       mem  0.12 GB tm     11.39us/ 30629.63ms (   493.30 GFLOPS  361.2|563.8   GB/s) 
*** GPU     315983 r2_32_4_250                            mem  0.12 GB tm      5.47us/ 30629.63ms (  1467.84 GFLOPS    6.0|1502.9  GB/s) 
*** GPU     315984 r_8_13_8_13_2_2_3_3_16_4               mem  0.12 GB tm     24.48us/ 30629.66ms (  2262.17 GFLOPS  456.6|989.7   GB/s) 
*** GPU     315985 r_64_2                                 mem  0.12 GB tm      4.10us/ 30629.66ms (     1.06 GFLOPS    0.0|4.2     GB/s) 
*** GPU     315986 r_1664_8_13_2_2_4                      mem  0.12 GB tm     18.75us/ 30629.68ms (   110.74 GFLOPS  738.3|738.3   GB/s) 
*** GPU     315987 r_1664_2_13_2_4_2_2_2                  mem  0.12 GB tm     14.37us/ 30629.70ms (   722.67 GFLOPS 1156.3|1156.3  GB/s) 
*** GPU     315988 r_8_128_11_2_16_2_3_11_4_3             mem  0.12 GB tm    247.90us/ 30629.94ms (  3454.66 GFLOPS   27.5|5501.9  GB/s) 
*** GPU     315989 r_512_5_16_2_2_5                       mem  0.12 GB tm     13.28us/ 30629.96ms (   246.75 GFLOPS  360.2|1727.2  GB/s) 
*** GPU     315990 r_512_5_16_2_2_5n1                     mem  0.12 GB tm     15.01us/ 30629.97ms (   382.09 GFLOPS  373.4|1746.7  GB/s) 
*** GPU     315991 E_800_8_16_2                           mem  0.12 GB tm      6.40us/ 30629.98ms (   128.00 GFLOPS  384.0|384.0   GB/s) 
*** GPU     315992 r_64_5_16_4_2_2_25                     mem  0.12 GB tm      8.90us/ 30629.99ms (  1049.78 GFLOPS   99.9|3370.4  GB/s) 
*** GPU     315993 r_64_2_10                              mem  0.12 GB tm      4.38us/ 30629.99ms (     0.29 GFLOPS    1.3|1.3     GB/s) 
*** GPU     315994 r_64_2_10n1                            mem  0.12 GB tm      5.02us/ 30630.00ms (     1.02 GFLOPS    1.2|1.2     GB/s) 
*** GPU     315995 r_4_32_10n2                            mem  0.12 GB tm      3.68us/ 30630.00ms (     1.39 GFLOPS    1.7|1.7     GB/s) 
*** GPU     315996 r_2_16_4_10                            mem  0.12 GB tm      4.29us/ 30630.00ms (     1.85 GFLOPS    0.4|1.7     GB/s) 
*** GPU     315997 r_8_8_2_10                             mem  0.12 GB tm      5.34us/ 30630.01ms (     2.66 GFLOPS    1.4|2.4     GB/s) 
*** GPU     315998 E_8_5_16_2                             mem  0.12 GB tm      3.68us/ 30630.01ms (     5.57 GFLOPS    3.5|8.5     GB/s) 
*** GPU     315999 r3_10_16_8n1                           mem  0.12 GB tm      4.10us/ 30630.02ms (     1.60 GFLOPS    1.3|5.3     GB/s) 
*** GPU     316000 r_2_25_4_16_4_4_4_10                   mem  0.12 GB tm      6.59us/ 30630.02ms (   714.56 GFLOPS  259.0|869.9   GB/s) 
*** GPU     316001 E_5_512_16_2_2_5                       mem  0.12 GB tm     19.39us/ 30630.04ms (   232.34 GFLOPS  500.2|591.4   GB/s) 
*** GPU     316002 r3_25_5_8_4_4_8_2_2_4                  mem  0.12 GB tm      7.07us/ 30630.05ms (   762.44 GFLOPS  170.9|1583.7  GB/s) 
*** GPU     316003 E_8_32_11_2_2_11_4_2                   mem  0.12 GB tm     40.51us/ 30630.09ms (    44.76 GFLOPS  275.8|275.8   GB/s) 
*** GPU     316004 r3_64_121_128n1                        mem  0.12 GB tm      6.21us/ 30630.10ms (   331.81 GFLOPS  638.9|1292.3  GB/s) 
*** GPU     316005 r_32_32_8_3_4_16_4_4_3_4               mem  0.12 GB tm    172.48us/ 30630.27ms (  3501.74 GFLOPS  126.9|2443.9  GB/s) 
*** GPU     316006 r_128_13_2_2_13_4_4_4_2                mem  0.12 GB tm     32.38us/ 30630.30ms (   416.82 GFLOPS  636.5|1453.5  GB/s) 
*** GPU     316007 r3_8_16_3_2_2_11_128_11_3_4            mem  0.12 GB tm    248.10us/ 30630.55ms (  2323.46 GFLOPS   28.9|2744.5  GB/s) 
*** GPU     316008 E_128_13_13_2_4_2_2_2_2                mem  0.12 GB tm     34.02us/ 30630.58ms (   610.50 GFLOPS  895.4|1139.6  GB/s) 
*** GPU     316009 r_128_4_3_2_26_26_4_3                  mem  0.12 GB tm     27.65us/ 30630.61ms (  2704.00 GFLOPS  409.6|5309.8  GB/s) 
*** GPU     316010 r_4_128_8_4_169                        mem  0.12 GB tm     12.96us/ 30630.62ms (   218.71 GFLOPS  855.9|884.9   GB/s) 
*** GPU     316011 r3_288_16_8n1                          mem  0.12 GB tm      5.54us/ 30630.63ms (    34.13 GFLOPS   27.9|113.2   GB/s) 
*** GPU     316012 r3_8_4_32_4                            mem  0.12 GB tm      4.16us/ 30630.63ms (    13.05 GFLOPS    4.1|45.3    GB/s) 
*** GPU     316013 E_32_4n1                               mem  0.12 GB tm      3.78us/ 30630.64ms (     0.07 GFLOPS    0.3|0.3     GB/s) 
*** GPU     316014 r_8_16                                 mem  0.12 GB tm      4.48us/ 30630.64ms (     0.04 GFLOPS    0.0|0.1     GB/s) 
*** GPU     316015 r_64_2_10n2                            mem  0.12 GB tm      5.70us/ 30630.65ms (     2.37 GFLOPS    1.2|5.1     GB/s) 
avg:  3793.43 GFLOPS    63.65 GB/s           total: 316015 kernels 116195.23 GOPS  1949.62 GB 30630.65 ms

```
# Just switched MNIST batch to 256 from 128

Result below:


```bash
 DEBUG=2 BEAM=2  python mnist.py 

 jit execs 45 kernels
*** GPU     315971 E_                                     mem  0.19 GB tm      3.78us/ 54095.46ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315972 E_n1                                   mem  0.19 GB tm      4.10us/ 54095.47ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** CUSTOM  315973 custom_random                          mem  0.19 GB 
*** GPU     315974 r_75_32_60000_5_5                      mem  0.19 GB tm      6.02us/ 54095.47ms (    11.17 GFLOPS   39.9|39.9    GB/s) 
*** CUSTOM  315975 custom_random                          mem  0.19 GB 
*** GPU     315976 r_5_2_10                               mem  0.19 GB tm      5.50us/ 54095.48ms (     0.05 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315977 E_n2                                   mem  0.19 GB tm      4.70us/ 54095.48ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315978 E_n2                                   mem  0.19 GB tm      4.61us/ 54095.49ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     315979 E_8_32                                 mem  0.19 GB tm      4.32us/ 54095.49ms (     0.24 GFLOPS    0.5|0.5     GB/s) 
*** GPU     315980 r_56_10_32_2_2_3000_8_7                mem  0.19 GB tm   5463.46us/ 54100.96ms (  5038.04 GFLOPS    9.4|434.1   GB/s) 
*** GPU     315981 r_2_250_32_16_15_4                     mem  0.19 GB tm     20.74us/ 54100.98ms (  3753.09 GFLOPS   17.6|2012.3  GB/s) 
*** GPU     315982 r_896_32_20_7                          mem  0.19 GB tm     11.20us/ 54100.99ms (   358.40 GFLOPS  376.3|376.3   GB/s) 
*** GPU     315983 r2_128_2_250                           mem  0.19 GB tm      5.76us/ 54100.99ms (    11.16 GFLOPS   11.3|11.3    GB/s) 
*** GPU     315984 r_4_16_13_13_2_2_3_3_16_4_2            mem  0.19 GB tm     41.73us/ 54101.04ms (  2654.23 GFLOPS  535.7|1011.9  GB/s) 
*** GPU     315985 r_16_4_4                               mem  0.19 GB tm      4.16us/ 54101.04ms (     1.08 GFLOPS    0.1|4.1     GB/s) 
*** GPU     315986 r_13312_8_2_13_2                       mem  0.19 GB tm     40.96us/ 54101.08ms (   202.80 GFLOPS  676.0|1622.4  GB/s) 
*** GPU     315987 r_3328_4_13_2_2_4_2                    mem  0.19 GB tm     41.22us/ 54101.12ms (   537.44 GFLOPS  806.2|806.2   GB/s) 
*** GPU     315988 r_8_256_11_2_16_2_3_11_4_3             mem  0.19 GB tm    485.66us/ 54101.61ms (  3526.82 GFLOPS   27.9|5616.8  GB/s) 
*** GPU     315989 r_1024_16_2_2_5_5                      mem  0.19 GB tm     18.34us/ 54101.63ms (   357.42 GFLOPS  521.8|2501.9  GB/s) 
*** GPU     315990 r_1024_5_16_2_5_2                      mem  0.19 GB tm     24.77us/ 54101.65ms (   297.67 GFLOPS  452.5|926.1   GB/s) 
*** GPU     315991 E_800_4_32_4                           mem  0.19 GB tm      7.65us/ 54101.66ms (   214.23 GFLOPS  642.7|642.7   GB/s) 
*** GPU     315992 r_128_5_16_4_2_2_25                    mem  0.19 GB tm     12.06us/ 54101.67ms (  1548.22 GFLOPS  142.0|4970.6  GB/s) 
*** GPU     315993 r_16_8_2_10                            mem  0.19 GB tm      3.74us/ 54101.67ms (     0.68 GFLOPS    3.0|3.0     GB/s) 
*** GPU     315994 r_2_8_16_10                            mem  0.19 GB tm      3.78us/ 54101.68ms (     2.71 GFLOPS    3.3|3.3     GB/s) 
*** GPU     315995 r_32_8_10                              mem  0.19 GB tm      5.73us/ 54101.68ms (     1.83 GFLOPS    2.1|2.1     GB/s) 
*** GPU     315996 r_8_8_4_10                             mem  0.19 GB tm      5.09us/ 54101.69ms (     3.12 GFLOPS    0.7|2.9     GB/s) 
*** GPU     315997 r_8_32_10n4                            mem  0.19 GB tm      4.42us/ 54101.69ms (     6.38 GFLOPS    3.3|5.9     GB/s) 
*** GPU     315998 E_8_2_16_5_2                           mem  0.19 GB tm      3.74us/ 54101.70ms (    10.53 GFLOPS    6.9|10.0    GB/s) 
*** GPU     315999 r3_5_2_8_4_8                           mem  0.19 GB tm      4.54us/ 54101.70ms (     4.01 GFLOPS    2.3|14.1    GB/s) 
*** GPU     316000 r_25_2_16_16_10_4_4_2                  mem  0.19 GB tm      7.58us/ 54101.71ms (  1296.20 GFLOPS  441.9|1242.2  GB/s) 
*** GPU     316001 E_5_1024_16_2_2_5                      mem  0.19 GB tm     37.82us/ 54101.75ms (   238.24 GFLOPS  512.9|606.4   GB/s) 
*** GPU     316002 r3_25_5_8_4_4_64_2_2                   mem  0.19 GB tm     10.82us/ 54101.76ms (   877.22 GFLOPS  187.9|1792.9  GB/s) 
*** GPU     316003 E_16_32_11_2_2_11_4_2                  mem  0.19 GB tm     76.74us/ 54101.83ms (    47.27 GFLOPS  291.2|291.2   GB/s) 
*** GPU     316004 r3_64_128_4_4_4_4                      mem  0.19 GB tm     13.98us/ 54101.85ms (   235.50 GFLOPS  567.2|923.2   GB/s) 
*** GPU     316005 r_64_121_8_3_16_4_4_3_4                mem  0.19 GB tm    404.70us/ 54102.25ms (  2821.57 GFLOPS  108.0|1969.2  GB/s) 
*** GPU     316006 r_2_256_13_4_13_4_4_4                  mem  0.19 GB tm     62.75us/ 54102.32ms (   529.49 GFLOPS  656.9|1500.2  GB/s) 
*** GPU     316007 r3_16_3_16_11_11_256_4_3_2             mem  0.19 GB tm    473.15us/ 54102.79ms (  3059.35 GFLOPS   29.4|4426.9  GB/s) 
*** GPU     316008 E_256_13_13_2_16_2_2                   mem  0.19 GB tm     68.45us/ 54102.86ms (   606.79 GFLOPS  890.0|1132.7  GB/s) 
*** GPU     316009 r_256_8_3_26_26_3_4                    mem  0.19 GB tm     61.41us/ 54102.92ms (  2434.87 GFLOPS  368.8|4781.3  GB/s) 
*** GPU     316010 r_256_32_13_13_4                       mem  0.19 GB tm     28.99us/ 54102.95ms (   238.76 GFLOPS  765.2|984.4   GB/s) 
*** GPU     316011 r3_144_2_64_4                          mem  0.19 GB tm      5.41us/ 54102.95ms (   289.70 GFLOPS   55.8|1063.4  GB/s) 
*** GPU     316012 r3_4_8_16_16                           mem  0.19 GB tm      6.30us/ 54102.96ms (     3.98 GFLOPS    5.3|13.6    GB/s) 
*** GPU     316013 E_2_32_4n1                             mem  0.19 GB tm      4.61us/ 54102.96ms (     0.11 GFLOPS    0.4|0.4     GB/s) 
*** GPU     316014 r_32_8                                 mem  0.19 GB tm      3.97us/ 54102.97ms (     0.32 GFLOPS    0.1|1.2     GB/s) 
*** GPU     316015 r_256_10                               mem  0.19 GB tm      6.18us/ 54102.97ms (    13.68 GFLOPS    2.2|46.8    GB/s) 
avg:  4283.87 GFLOPS    60.86 GB/s           total: 316015 kernels 231770.02 GOPS  3292.84 GB 54102.97 ms
```

# Just switched MNIST batch size to 512

```bash
python mnist.py


*** GPU     329978 r_256_2_10                             mem  0.32 GB tm      5.95us/114677.55ms (    50.41 GFLOPS    4.6|185.2   GB/s) 
jit execs 47 kernels
*** GPU     329979 E_                                     mem  0.32 GB tm      4.19us/114677.55ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     329980 E_n1                                   mem  0.32 GB tm      4.29us/114677.56ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** CUSTOM  329981 custom_random                          mem  0.32 GB 
*** GPU     329982 r_75_32_60000_5_5                      mem  0.32 GB tm      6.21us/114677.57ms (    10.82 GFLOPS   38.7|38.7    GB/s) 
*** CUSTOM  329983 custom_random                          mem  0.32 GB 
*** GPU     329984 r_5_2_10                               mem  0.32 GB tm      3.42us/114677.57ms (     0.08 GFLOPS    0.0|0.0     GB/s) 
*** GPU     329985 E_n2                                   mem  0.32 GB tm      4.26us/114677.57ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     329986 E_n2                                   mem  0.32 GB tm      3.20us/114677.58ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     329987 E_32_8_2                               mem  0.32 GB tm      3.74us/114677.58ms (     0.55 GFLOPS    1.1|1.1     GB/s) 
*** GPU     329988 r_196_10_32_16_375_16_4                mem  0.32 GB tm     13.85ms/114691.43ms (  4420.45 GFLOPS    3.7|305.4   GB/s) 
*** GPU     329989 r_4_250_32_8_30_4                      mem  0.32 GB tm     33.02us/114691.47ms (  3968.99 GFLOPS   13.0|1596.9  GB/s) 
*** GPU     329990 r_1792_32_10_7                         mem  0.32 GB tm     11.78us/114691.48ms (   340.87 GFLOPS  375.0|375.0   GB/s) 
*** GPU     329991 r2_256_2_250                           mem  0.32 GB tm      7.26us/114691.49ms (    17.69 GFLOPS   18.0|18.0    GB/s) 
*** GPU     329992 r_32_4_13_13_2_2_3_3_16_4_2            mem  0.32 GB tm     71.14us/114691.56ms (  3113.92 GFLOPS  628.4|1187.2  GB/s) 
*** GPU     329993 r_64_2_4                               mem  0.32 GB tm      4.03us/114691.56ms (     1.17 GFLOPS    0.1|4.3     GB/s) 
*** GPU     329994 r_13312_8_13_2_2_2                     mem  0.32 GB tm     70.21us/114691.63ms (   118.32 GFLOPS  788.8|788.8   GB/s) 
*** GPU     329995 r_13312_4_13_2_4_2                     mem  0.32 GB tm     76.58us/114691.71ms (   578.54 GFLOPS  867.8|867.8   GB/s) 
*** GPU     329996 r_8_512_11_2_16_2_3_11_4_3             mem  0.32 GB tm    959.04us/114692.67ms (  3572.01 GFLOPS   28.2|5688.8  GB/s) 
*** GPU     329997 r_2048_16_2_2_5_5                      mem  0.32 GB tm     37.82us/114692.70ms (   346.53 GFLOPS  505.9|2425.7  GB/s) 
*** GPU     329998 r_2048_5_16_2_2_5                      mem  0.32 GB tm     45.76us/114692.75ms (   358.04 GFLOPS  489.8|1002.5  GB/s) 
*** GPU     329999 E_640_32_8_5                           mem  0.32 GB tm     12.00us/114692.76ms (   273.07 GFLOPS  819.2|819.2   GB/s) 
*** GPU     330000 r_2_128_2_16_4_25_5_2                  mem  0.32 GB tm     17.73us/114692.78ms (  2125.63 GFLOPS  189.6|6210.5  GB/s) 
*** GPU     330001 r_16_32_10                             mem  0.32 GB tm      4.03us/114692.78ms (     1.14 GFLOPS    5.6|5.6     GB/s) 
*** GPU     330002 r_16_32_10n1                           mem  0.32 GB tm      3.74us/114692.79ms (     5.47 GFLOPS    6.6|6.6     GB/s) 
*** GPU     330003 r_16_32_10n3                           mem  0.32 GB tm      4.32us/114692.79ms (     4.74 GFLOPS    5.7|5.7     GB/s) 
*** GPU     330004 r_16_32_10n5                           mem  0.32 GB tm      4.03us/114692.80ms (     7.75 GFLOPS    1.7|7.2     GB/s) 
*** GPU     330005 r_16_32_10n6                           mem  0.32 GB tm      4.03us/114692.80ms (    13.97 GFLOPS    7.2|12.8    GB/s) 
*** GPU     330006 E_16_5_32_2                            mem  0.32 GB tm      4.51us/114692.80ms (    18.16 GFLOPS   11.5|27.8    GB/s) 
*** GPU     330007 r3_10_8_16_4                           mem  0.32 GB tm      4.26us/114692.81ms (    44.81 GFLOPS    4.9|170.8   GB/s) 
*** GPU     330008 r_25_32_2_4_4_10_4_4_2                 mem  0.32 GB tm     11.01us/114692.82ms (  1786.05 GFLOPS  603.0|1711.6  GB/s) 
*** GPU     330009 E_256_5_16_2_2_2_2_2_5                 mem  0.32 GB tm     66.91us/114692.89ms (   269.34 GFLOPS  579.8|685.6   GB/s) 
*** GPU     330010 r3_100_2_2_8_64_5_4_2                  mem  0.32 GB tm     18.72us/114692.91ms (  1039.49 GFLOPS  196.7|981.2   GB/s) 
*** GPU     330011 E_32_32_11_2_2_11_4_2                  mem  0.32 GB tm    148.38us/114693.05ms (    48.89 GFLOPS  301.2|301.2   GB/s) 
*** GPU     330012 r_32_64_8_4_2_64_9_4_2_2               mem  0.32 GB tm   1026.05us/114694.08ms (  2354.97 GFLOPS   85.1|1512.5  GB/s) 
*** GPU     330013 r_4_128_32_8_11_4_11_3_3_2             mem  0.32 GB tm    723.84us/114694.80ms (  3549.50 GFLOPS   50.2|5720.6  GB/s) 
*** GPU     330014 r_32_64_2_121_2_4                      mem  0.32 GB tm     25.98us/114694.83ms (  9384.35 GFLOPS  612.9|38147.8 GB/s) 
*** GPU     330015 r_512_2_13_2_13_4_4_4_2                mem  0.32 GB tm    107.20us/114694.94ms (   503.67 GFLOPS  769.1|1756.4  GB/s) 
*** GPU     330016 r3_1536_2_16_8_3_2                     mem  0.32 GB tm     17.76us/114694.95ms (   650.38 GFLOPS  556.3|2092.3  GB/s) 
*** GPU     330017 r3_32_2_32_8                           mem  0.32 GB tm      4.86us/114694.96ms (    23.58 GFLOPS   13.8|84.2    GB/s) 
*** GPU     330018 E_512_13_13_2_16_2_2                   mem  0.32 GB tm    138.82us/114695.10ms (   598.40 GFLOPS  877.6|1117.0  GB/s) 
*** GPU     330019 r_256_8_3_2_26_2_3_26_2                mem  0.32 GB tm     93.41us/114695.19ms (  2667.87 GFLOPS  481.7|3912.9  GB/s) 
*** GPU     330020 r_256_32_13_2_4_13                     mem  0.32 GB tm     53.95us/114695.25ms (   230.95 GFLOPS  821.8|939.6   GB/s) 
*** GPU     330021 r3_144_2_64_4                          mem  0.32 GB tm      5.06us/114695.25ms (   309.87 GFLOPS   59.7|1137.4  GB/s) 
*** GPU     330022 r3_4_8_16_16                           mem  0.32 GB tm      5.54us/114695.26ms (     4.53 GFLOPS    6.1|15.5    GB/s) 
*** GPU     330023 E_4_32_4n2                             mem  0.32 GB tm      4.51us/114695.26ms (     0.23 GFLOPS    0.9|0.9     GB/s) 
*** GPU     330024 r_256_2n1                              mem  0.32 GB tm      4.93us/114695.27ms (    13.40 GFLOPS    0.1|53.7    GB/s) 
*** GPU     330025 r_256_2_10                             mem  0.32 GB tm      5.41us/114695.27ms (    55.48 GFLOPS    5.0|203.8   GB/s) 
avg:  4372.00 GFLOPS    53.25 GB/s           total: 330025 kernels 501447.41 GOPS  6107.83 GB 114695.27 ms

```
# With srun and 512 batches:

```bash
srun -p gpu --gres=gpu:1g.23gb:1 ./mnist.sh 

*** GPU     329978 r_256_2_10                             mem  0.32 GB tm      5.70us/104018.59ms (    52.67 GFLOPS    4.8|193.5   GB/s) 
jit execs 47 kernels
*** GPU     329979 E_                                     mem  0.32 GB tm      3.71us/104018.60ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     329980 E_n1                                   mem  0.32 GB tm      3.90us/104018.60ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** CUSTOM  329981 custom_random                          mem  0.32 GB 
*** GPU     329982 r_75_32_60000_5_5                      mem  0.32 GB tm      4.51us/104018.61ms (    14.89 GFLOPS   53.2|53.2    GB/s) 
*** CUSTOM  329983 custom_random                          mem  0.32 GB 
*** GPU     329984 r_5_2_10                               mem  0.32 GB tm      3.30us/104018.61ms (     0.09 GFLOPS    0.0|0.0     GB/s) 
*** GPU     329985 E_n2                                   mem  0.32 GB tm      4.26us/104018.61ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     329986 E_n2                                   mem  0.32 GB tm      3.39us/104018.62ms (     0.00 GFLOPS    0.0|0.0     GB/s) 
*** GPU     329987 E_32_8_2                               mem  0.32 GB tm      3.58us/104018.62ms (     0.57 GFLOPS    1.1|1.1     GB/s) 
*** GPU     329988 r_196_10_32_16_375_16_4                mem  0.32 GB tm     10.76ms/104029.38ms (  5689.11 GFLOPS    4.8|393.0   GB/s) 
*** GPU     329989 r_4_250_32_8_30_4                      mem  0.32 GB tm     33.76us/104029.42ms (  3882.46 GFLOPS   12.7|1562.1  GB/s) 
*** GPU     329990 r_1792_32_10_7                         mem  0.32 GB tm     11.36us/104029.43ms (   353.35 GFLOPS  388.7|388.7   GB/s) 
*** GPU     329991 r2_256_2_250                           mem  0.32 GB tm      6.37us/104029.44ms (    20.18 GFLOPS   20.5|20.5    GB/s) 
*** GPU     329992 r_32_4_13_13_2_2_3_3_16_4_2            mem  0.32 GB tm     71.78us/104029.51ms (  3086.15 GFLOPS  622.8|1176.6  GB/s) 
*** GPU     329993 r_64_2_4                               mem  0.32 GB tm      4.48us/104029.51ms (     1.06 GFLOPS    0.1|3.9     GB/s) 
*** GPU     329994 r_13312_8_13_2_2_2                     mem  0.32 GB tm     69.76us/104029.58ms (   119.08 GFLOPS  793.8|793.8   GB/s) 
*** GPU     329995 r_13312_4_13_2_4_2                     mem  0.32 GB tm     74.66us/104029.66ms (   593.42 GFLOPS  890.1|890.1   GB/s) 
*** GPU     329996 r_8_512_11_2_16_2_3_11_4_3             mem  0.32 GB tm    958.21us/104030.61ms (  3575.11 GFLOPS   28.2|5693.7  GB/s) 
*** GPU     329997 r_2048_16_2_2_5_5                      mem  0.32 GB tm     35.42us/104030.65ms (   370.01 GFLOPS  540.2|2590.1  GB/s) 
*** GPU     329998 r_2048_5_16_2_2_5                      mem  0.32 GB tm     46.30us/104030.70ms (   353.84 GFLOPS  484.0|990.7   GB/s) 
*** GPU     329999 E_640_32_8_5                           mem  0.32 GB tm     11.52us/104030.71ms (   284.44 GFLOPS  853.3|853.3   GB/s) 
*** GPU     330000 r_2_128_2_16_4_25_5_2                  mem  0.32 GB tm     16.22us/104030.72ms (  2322.68 GFLOPS  207.2|6786.3  GB/s) 
*** GPU     330001 r_16_32_10                             mem  0.32 GB tm      5.12us/104030.73ms (     0.90 GFLOPS    4.4|4.4     GB/s) 
*** GPU     330002 r_16_32_10n1                           mem  0.32 GB tm      4.16us/104030.73ms (     4.92 GFLOPS    5.9|5.9     GB/s) 
*** GPU     330003 r_16_32_10n2                           mem  0.32 GB tm      4.19us/104030.74ms (     4.89 GFLOPS    5.9|5.9     GB/s) 
*** GPU     330004 r_16_32_10n3                           mem  0.32 GB tm      3.97us/104030.74ms (     7.87 GFLOPS    1.7|7.4     GB/s) 
*** GPU     330005 r_16_32_10n4                           mem  0.32 GB tm      4.00us/104030.75ms (    14.08 GFLOPS    7.3|12.9    GB/s) 
*** GPU     330006 E_16_5_32_2                            mem  0.32 GB tm      4.51us/104030.75ms (    18.16 GFLOPS   11.5|27.8    GB/s) 
*** GPU     330007 r3_10_8_16_4                           mem  0.32 GB tm      4.26us/104030.75ms (    44.81 GFLOPS    4.9|170.8   GB/s) 
*** GPU     330008 r_25_32_2_4_4_10_4_4_2                 mem  0.32 GB tm     10.72us/104030.76ms (  1834.03 GFLOPS  619.2|1757.6  GB/s) 
*** GPU     330009 E_256_5_16_2_2_2_2_2_5                 mem  0.32 GB tm     68.93us/104030.83ms (   261.47 GFLOPS  562.9|665.6   GB/s) 
*** GPU     330010 r3_100_2_2_8_64_5_4_2                  mem  0.32 GB tm     18.69us/104030.85ms (  1041.27 GFLOPS  197.0|982.9   GB/s) 
*** GPU     330011 E_32_32_11_2_2_11_4_2                  mem  0.32 GB tm    148.54us/104031.00ms (    48.83 GFLOPS  300.9|300.9   GB/s) 
*** GPU     330012 r_32_64_8_4_2_64_9_4_2_2               mem  0.32 GB tm   1039.74us/104032.04ms (  2323.95 GFLOPS   84.0|1492.6  GB/s) 
*** GPU     330013 r_4_128_32_8_11_4_11_3_3_2             mem  0.32 GB tm    723.36us/104032.76ms (  3551.86 GFLOPS   50.3|5724.4  GB/s) 
*** GPU     330014 r_32_64_2_121_2_4                      mem  0.32 GB tm     25.57us/104032.79ms (  9537.04 GFLOPS  622.9|38768.5 GB/s) 
*** GPU     330015 r_512_2_13_2_13_4_4_4_2                mem  0.32 GB tm    105.98us/104032.90ms (   509.45 GFLOPS  777.9|1776.5  GB/s) 
*** GPU     330016 r3_1536_2_16_8_3_2                     mem  0.32 GB tm     19.26us/104032.91ms (   599.60 GFLOPS  512.9|1928.9  GB/s) 
*** GPU     330017 r3_32_2_32_8                           mem  0.32 GB tm      4.86us/104032.92ms (    23.58 GFLOPS   13.8|84.2    GB/s) 
*** GPU     330018 E_512_13_13_2_16_2_2                   mem  0.32 GB tm    137.44us/104033.06ms (   604.39 GFLOPS  886.4|1128.2  GB/s) 
*** GPU     330019 r_256_8_3_2_26_2_3_26_2                mem  0.32 GB tm     91.87us/104033.15ms (  2712.48 GFLOPS  489.8|3978.3  GB/s) 
*** GPU     330020 r_256_32_13_2_4_13                     mem  0.32 GB tm     53.12us/104033.20ms (   234.56 GFLOPS  834.6|954.3   GB/s) 
*** GPU     330021 r3_144_2_64_4                          mem  0.32 GB tm      8.19us/104033.21ms (   191.25 GFLOPS   36.8|702.0   GB/s) 
*** GPU     330022 r3_4_8_16_16                           mem  0.32 GB tm      4.51us/104033.21ms (     5.56 GFLOPS    7.4|19.1    GB/s) 
*** GPU     330023 E_4_32_4                               mem  0.32 GB tm      4.54us/104033.22ms (     0.23 GFLOPS    0.9|0.9     GB/s) 
*** GPU     330024 r_256_2                                mem  0.32 GB tm      4.03us/104033.22ms (    16.38 GFLOPS    0.1|65.7    GB/s) 
*** GPU     330025 r_256_2_10                             mem  0.32 GB tm      5.44us/104033.23ms (    55.15 GFLOPS    5.0|202.6   GB/s) 
avg:  4820.07 GFLOPS    58.71 GB/s           total: 330025 kernels 501447.41 GOPS  6107.83 GB 104033.23 ms
```
