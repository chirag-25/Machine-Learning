import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.neighbors import KernelDensity
from sklearn.cluster import MeanShift

# generate sample data
X, _ = make_blobs(n_samples=1000, centers=4, random_state=42)

# compute kernel density estimate
kde = KernelDensity(kernel='gaussian', bandwidth=0.5).fit(X)
densities = np.exp(kde.score_samples(X))

# cluster using mean-shift algorithm
ms = MeanShift(bandwidth=1.0, bin_seeding=True)
ms.fit(X)

# plot results
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# plot kernel density estimate
scatter = ax[0].scatter(X[:, 0], X[:, 1], c=densities, cmap='viridis', s=10)
ax[0].set_title('Kernel Density Estimate')

# plot clusters
ax[1].scatter(X[:, 0], X[:, 1], c=ms.labels_, cmap='viridis', s=10)
ax[1].set_title('Clusters')
plt.colorbar(scatter)
plt.show()
