import os

data = []
edges = []
projections = []
max_area = 0

# There have been two previous attempts that check if the four corners of a rectangle are within the original tile shape.
# This works for example data, but does not work for concave shapes.
#
# Instead of checking individual points or corners, we check AREA containment.
#
# Imagine looking at the shape from above and sliding a horizontal line from bottom to top. 
# At each height, the shape occupies one or more continuous stretches along the x-axis.
#
# The rectangle we are testing also occupies exactly one stretch along the x-axis at any given height.
#
# The rectangle is valid if, at every height it spans, its horizontal stretch is
# completely contained within the shape’s horizontal stretch at that same height.
#
# If this is true everywhere, the rectangle never sticks out of the shape at any point, even in concave regions.


def rectangle_fits(p1, p2, projections):
    for ys, ye, x_intervals in projections:

        if ye < p1[1] or ys > p2[1]:
            continue

        for a, b in x_intervals:
            if a <= p1[0] and b >= p2[0]:
                break
        else:
            return False

    return True


with open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r") as file:
    for line in file:
        data.append([int(i) for i in line.strip().split(",")])


for i in range(len(data)):
    p2 = data[(i + 1) % len(data)]
    edges.append((data[i][0], data[i][1], p2[0], p2[1]))


# Find all unique Y coordinates where the polygon changes shape.
# Between any two such Y values, the horizontal projection of the polygon is CONSTANT.
ys = sorted(set(y for _, y in data))


# Build horizontal PROJECTIONS (shadows).
#   (y_start, y_end, [(x1, x2), ...])
#
# For every y ∈ [y_start, y_end], the polygon covers all x-intervals.
for k in range(len(ys) - 1):
    xs = []
    intervals = []

    if ys[k] > ys[k + 1] - 1:
        continue

    y_scan = ys[k] + 0.5
    
    for x1, y1, x2, y2 in edges:

        # horizontal edges do not contribute to crossings
        if y1 == y2:
            continue

        ymin = min(y1, y2)
        ymax = max(y1, y2)

        # avoid double counting
        if y_scan <= ymin or y_scan > ymax:
            continue

        xs.append(x1)

    xs.sort()

    for i in range(0, len(xs), 2):
        a = xs[i]
        b = xs[i + 1] - 1
        if a <= b:
            intervals.append((a, b))

    if intervals:
        projections.append((ys[k], ys[k + 1] - 1, intervals))



for i in range(len(data)):
    for j in range(len(data)):

        xl = min(data[i][0], data[j][0])
        xr = max(data[i][0], data[j][0])
        yl = min(data[i][1], data[j][1])
        yr = max(data[i][1], data[j][1])

        if xl == xr or yl == yr:
            continue

        E = (xr - xl + 1) * (yr - yl + 1)

        if E > max_area and rectangle_fits((xl, yl), (xr, yr), projections):
            max_area = E


print(max_area)
