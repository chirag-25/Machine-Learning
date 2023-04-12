Kernel Density Estimate (KDE) clustering is a non-parametric density-based clustering algorithm. It is used to estimate the probability density function of a dataset and identify regions of high density, which are then considered as clusters. The algorithm works by placing a kernel function on each data point and adding up their contributions to estimate the density at a given point.

Here's how the algorithm works in more detail:
1. Choose a kernel function, such as the Gaussian kernel, which is a common choice.

2. Determine the bandwidth parameter of the kernel function. This determines the smoothing of the density estimate and affects the size of the clusters. A smaller bandwidth will result in more local clusters while a larger bandwidth will result in more global clusters.

3. For each data point, calculate the kernel function value at that point, using the chosen kernel function and bandwidth.

4. Sum up the kernel function values for all data points to estimate the density at each point in the dataset.

5. Identify regions of high density by finding local maxima in the estimated density function. These regions represent clusters.

6. Assign each data point to the closest cluster based on its distance to the cluster center.

7. Repeat steps 3-6 until the clusters stabilize or a convergence criterion is met.

KDE clustering is particularly useful for datasets with complex shapes and irregularities, as it does not make assumptions about the underlying distribution of the data. However, it can be computationally expensive for large datasets, and the choice of kernel function and bandwidth can significantly affect the results. Therefore, careful tuning of these parameters is necessary for optimal performance.

With KDE we are using other clustering algorithms. The reason for this is that KDE clustering alone does not assign data points to specific clusters, but rather estimates the density function of the data. In order to obtain cluster assignments, we need to apply a clustering algorithm on top of the estimated densities.