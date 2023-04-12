import streamlit as st
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN, MeanShift
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from sklearn.neighbors import KernelDensity
from scipy.signal import find_peaks
from sklearn import metrics
import numpy as np

with st.sidebar:
    st.write("Data Generation Parameters")
    min_samples = st.slider('min_samples', min_value=1, max_value=10, value=5, step=1)
    n_centers = st.slider('n_centers', min_value=1, max_value=20, value=5, step=1)
    st.write("DBSCAN Parameters")
    epslon = st.slider('epslon', min_value=0.1, max_value=1.0, value=0.5, step=0.1)
    sample_count = st.slider('sample_count', min_value=100, max_value=5000, value=1000, step=100)
    st.write(f"KDE Parameters")
    bandwidth = st.slider('bandwidth', min_value=0.1, max_value=1.0, value=0.5, step=0.1)
    st.write('min_samples', min_samples)
    st.write('n_centers', n_centers)
    st.write('sample_count', sample_count)
    st.write('epslon', epslon)
    st.write('bandwidth', bandwidth)

# Create dataset
X, y = make_blobs(n_samples=sample_count, centers=n_centers, random_state=42)

st.title("Original Data")
vor = Voronoi(X)
fig, ax = plt.subplots()
voronoi_plot_2d(vor, ax=ax, show_points=False, show_vertices=False, line_colors='grey', line_width=1, line_alpha=0.2, point_size=2)
ax.scatter(X[:, 0], X[:, 1], s=5, cmap='viridis')
st.pyplot(fig)

# dbscan clustering
st.title('DBSCAN Clustering Visualization')
dbscan = DBSCAN(eps=epslon, min_samples=min_samples)
dbscan.fit(X)
labels = dbscan.labels_
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
fig, ax = plt.subplots()
voronoi_plot_2d(vor, ax=ax, show_points=False, show_vertices=False, line_colors='grey', line_width=1, line_alpha=0.2, point_size=2)
scatter = ax.scatter(X[:, 0], X[:, 1], c=labels, s=5, cmap='viridis')
ax.set_title(f'DBSCAN Clustering\nNumber of clusters: {n_clusters}')
plt.colorbar(scatter)
st.pyplot(fig)
st.write('Silhouette Score DBSCAN', metrics.silhouette_score(X, labels)) 




# KDE clustering
st.title('KDE Clustering Visualization')
kde_model = KernelDensity(kernel='gaussian', bandwidth=bandwidth).fit(X)
log_dens = np.exp(kde_model.score_samples(X))
ms = MeanShift().fit(log_dens.reshape(-1, 1))
labels_kde = ms.labels_
fig, ax = plt.subplots()
n_clusters_kde = len(set(labels_kde)) - (1 if -1 in labels_kde else 0)
voronoi_plot_2d(vor, ax=ax, show_points=False, show_vertices=False, line_colors='grey', line_width=1, line_alpha=0.2, point_size=2)
scatter_kde = ax.scatter(X[:, 0], X[:, 1], c=labels_kde, s=5, cmap='viridis')
ax.set_title(f'KDE\nNumber of clusters: {n_clusters_kde}')
plt.colorbar(scatter_kde)
# Display plot in Streamlit app
st.pyplot(fig)
st.write('Silhouette Score KDE', metrics.silhouette_score(X, labels_kde))



