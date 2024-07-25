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

I need to test that on Alpine as well.
