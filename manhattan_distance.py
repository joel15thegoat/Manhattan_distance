def manhattan_distance(point1, point2): 
    """Calculates the Manhattan distance between two n-dimensional points.""" 
    return sum(abs(a - b) for a, b in zip(point1, point2)) 
def sort_by_nearest_neighbor(target, points): 
    """ 
    Sorts a list of points based on their Manhattan distance to the target point. 
    Returns a list of tuples: (distance, point). 
    """ 
    # Create a list of (distance, point) pairs 
    distances = [(manhattan_distance(target, p), p) for p in points] 
    # Sort the list by the distance (the first element of the tuple) 
    distances.sort(key=lambda x: x[0]) 
    return distances 
# --- Example Usage --- 
if __name__ == "__main__": 
    target_point = (5, 5) 
    # A list of random 2D points 
    data_points = [(1, 2), (8, 8), (5, 6), (2, 9), (4, 5)] 
    sorted_points = sort_by_nearest_neighbor(target_point, data_points) 
    print(f"Target Point: {target_point}\n") 
    print("Points sorted by Nearest Neighbor (Manhattan Distance):") 
    for distance, point in sorted_points: 
        print(f"Point: {point} | Distance: {distance}")
