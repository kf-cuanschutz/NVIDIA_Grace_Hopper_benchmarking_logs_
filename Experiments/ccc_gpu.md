Logs:
-----

```python
random_feature1 = np.random.rand(10000)
random_feature2 = np.random.rand(10000)

np.save('array1.npy', random_feature1)
np.save('array2.npy', random_feature2)
```

Output CPU parts

```bash
[[[0 1 1 ... 0 0 0]
  [0 2 1 ... 1 1 0]
  [0 3 2 ... 1 1 0]
  ...
  [0 7 4 ... 3 2 1]
  [0 8 4 ... 3 3 1]
  [0 8 5 ... 4 3 1]]

 [[1 1 0 ... 1 0 1]
  [2 1 1 ... 1 1 1]
  [3 2 1 ... 2 1 2]
  ...
  [6 4 2 ... 4 3 4]
  [7 5 3 ... 5 3 5]
  [8 5 3 ... 5 4 5]]]

CPU time is 0.35521507263183594

```

Output GPU parts

```bash
GPU parts:
[[[0 0 1 ... 1 0 1]
  [0 1 2 ... 2 0 1]
  [0 1 3 ... 3 0 2]
  ...
  [0 3 7 ... 6 0 4]
  [0 4 8 ... 7 0 5]
  [1 4 9 ... 8 0 5]]

 [[1 0 0 ... 1 1 0]
  [2 0 1 ... 2 2 0]
  [3 1 1 ... 3 3 0]
  ...
  [6 2 3 ... 6 7 0]
  [6 2 3 ... 7 8 0]
  [7 2 4 ... 8 8 0]]]

GPU time is 2.7425854206085205

```

Lot of nan:

```bash
GPU percentiles: [0.5 nan nan nan nan nan nan nan nan]
GPU quantiles: [0.5008643755592058                nan                nan
                nan                nan                nan
                nan                nan                nan]
GPU percentiles: [0.3333333333333333 0.6666666666666667                nan
                nan                nan                nan
                nan                nan                nan]
GPU quantiles: [0.33260897569783154 0.6641338135760118                  nan
                 nan                 nan                 nan
                 nan                 nan                 nan]
GPU percentiles: [0.25 0.5  0.75  nan  nan  nan  nan  nan  nan]
GPU quantiles: [0.2451335619930029 0.5008643755592058 0.7473250297638401
                nan                nan                nan
                nan                nan                nan]

```
