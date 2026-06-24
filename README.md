# Manhattan_distance

A Python script that sorts points by their Manhattan distance to a target, using a nearest neighbor approach. Supports n-dimensional points.

##  Features

- Calculates Manhattan distance (L1 norm) between two points of arbitrary dimensions
- Sorts points by distance using a clean, readable approach
- Minimal, no external dependencies
- Perfect for understanding distance metrics and nearest-neighbor concepts

##  Usage
**1. Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/manhattan-nn-sorter.git
   cd manhattan-nn-sorter
   ```   
**2. running the code**

```bash
python manhattan_sorter.py
```

## Customization

- Change the target point: modify ```target_point = (x, y, ...)```
- Use your own data: replace `data_points` with a list of coordinate tuples (any dimension)
-Sort order: reverse the sort by adding `reverse=True` in the `sort()` call

## Example Output

```text
Target Point: (5, 5)

Points sorted by Nearest Neighbor (Manhattan Distance):
Point: (4, 5) | Distance: 1
Point: (5, 6) | Distance: 1
Point: (1, 2) | Distance: 7
Point: (8, 8) | Distance: 6
Point: (2, 9) | Distance: 8
```

## licence
this is published under the mit [licence](https://mit-license.org/).
## have fun
