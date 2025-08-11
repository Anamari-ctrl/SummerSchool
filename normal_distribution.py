import numpy as np
import statistics as st

normal_distribution = np.random.normal(5, 2, (1, 100000)).reshape(-1).tolist()
print(st.mean(normal_distribution))
print(st.variance(normal_distribution))
