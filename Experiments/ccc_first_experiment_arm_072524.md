Logs:
-----

```python
In [2]: import numpy as np

In [3]: import pandas as pd

In [4]: from ccc.coef import ccc

In [7]: data = np.random.rand(200, 100000)

In [10]: %timeit ccc(data, n_jobs=72)
1min 49s ± 169 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

Changing matrix size

```python

In [7]: data = np.random.rand(200, 1000)

In [9]: %timeit ccc(data, n_jobs=4)
24.1 s ± 436 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```
On Alpine, CPU side:

```python
In [6]: %timeit ccc(data, n_jobs=4)
49.7 s ± 1.08 s per loop (mean ± std. dev. of 7 runs, 1 loop each)
```
