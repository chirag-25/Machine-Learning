import streamlit as st
from sklearn.datasets import make_blobs
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# Set up Streamlit app
st.title('DBSCAN Clustering Visualization')


with st.sidebar:
    epslon = st.slider('epslon', min_value=0.1, max_value=1.0, value=0.5, step=0.1)
    min_samples = st.slider('min_samples', min_value=1, max_value=10, value=5, step=1)
    sample_count = st.slider('sample_count', min_value=100, max_value=5000, value=1000, step=100)
    st.write('sample_count', sample_count)
    st.write('min_samples', min_samples)
    st.write('epslon', epslon)
    
# Create dataset
X, y = make_blobs(n_samples=sample_count, centers=min_samples, random_state=42)

# Initialize DBSCAN algorithm
dbscan = DBSCAN(eps=epslon, min_samples=min_samples)

# Fit DBSCAN to dataset
dbscan.fit(X)

# Get cluster labels and number of clusters
labels = dbscan.labels_
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)

# Create Voronoi diagram
vor = Voronoi(X)

# Plot Voronoi diagram with cluster colors
fig, ax = plt.subplots()
voronoi_plot_2d(vor, ax=ax, show_points=False, show_vertices=False, line_colors='grey', line_width=1, line_alpha=0.2, point_size=2)

# Plot points with cluster colors
scatter = ax.scatter(X[:, 0], X[:, 1], c=labels, s=5, cmap='viridis')

# Set plot title
ax.set_title(f'DBSCAN Clustering\nNumber of clusters: {n_clusters}')

# Add colorbar to plot
plt.colorbar(scatter)

# Display plot in Streamlit app
st.pyplot(fig)






# from sklearn.datasets import make_blobs
# from sklearn.cluster import DBSCAN
# import matplotlib.pyplot as plt

# # Create dataset
# X, y = make_blobs(n_samples=1000, centers=5, random_state=42)

# # Initialize DBSCAN algorithm
# dbscan = DBSCAN(eps=0.5, min_samples=5)

# # Fit DBSCAN to dataset
# dbscan.fit(X)

# # Get cluster labels and number of clusters
# labels = dbscan.labels_
# n_clusters = len(set(labels)) - (1 if -1 in labels else 0)

# # Plot results  and reduce the size of the points
# plt.scatter(X[:, 0], X[:, 1], c=labels, s=1, cmap='viridis')
# plt.title(f'DBSCAN Clustering\nNumber of clusters: {n_clusters}')
# plt.show()
