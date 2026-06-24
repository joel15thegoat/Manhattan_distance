import numpy as np
def numpy_nearest_neighbor_sort(target, points):
    """
    Sorts an array of points based on Manhattan distance using NumPy.
    """
    # Convert inputs to numpy arrays
    target = np.array(target)
    points = np.array(points)
    
    # Calculate Manhattan distances for all points at once (vectorized)
    # np.abs gets absolute difference, axis=1 sums across the dimensions (x, y, etc.)
    distances = np.sum(np.abs(points - target), axis=1)
    
    # Get the indices that would sort the distances array
    sorted_indices = np.argsort(distances)
    
    # Use those indices to sort the original points and the distances
    sorted_points = points[sorted_indices]
    sorted_distances = distances[sorted_indices]
    
    return sorted_points, sorted_distances

# --- Example Usage ---
target_point = [5, 5]
data_points = [[1, 2], [8, 8], [5, 6], [2, 9], [4, 5]]

sorted_pts, sorted_dists = numpy_nearest_neighbor_sort(target_point, data_points)

print("Sorted Points:\n", sorted_pts)
print("Corresponding Distances:\n", sorted_dists)
