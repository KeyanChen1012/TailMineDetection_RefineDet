import numpy as np

import Config
layers = 4
minRatio = 0.05
maxRatio = 0.90

step = (maxRatio - minRatio) / (layers - 1)
sizes = Config.INPUT_SIZE[0] * np.array([minRatio + i * step for i in range(layers+1)])
minSizes = sizes[:-1].astype(int)
maxSizes = sizes[1:].astype(int)
print('min_sizes:{}\nmax_sizes:{}'.format(minSizes, maxSizes))
