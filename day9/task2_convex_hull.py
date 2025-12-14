import os

data = []
max_area = 0

def point_in_polygon(point, polygon):
    """
    Check if a point lies within a polygon.

    Credit: Geek for geeks
    https://www.geeksforgeeks.org/dsa/how-to-check-if-a-given-point-lies-inside-a-polygon/
    
    :param point: point to check if it belongs in convex hull
    :param polygon: list of points of the polygon
    """
    num_vertices = len(polygon)
    x, y = point[0], point[1]
    inside = False

    # Store the first point in the polygon and initialize the second point
    p1 = polygon[0]

    # Loop through each edge in the polygon
    for i in range(1, num_vertices + 1):
        # Get the next point in the polygon
        p2 = polygon[i % num_vertices]

        # Check if the point is above the minimum y coordinate of the edge
        if y > min(p2[1], p1[1]):
            # Check if the point is below the maximum y coordinate of the edge
            if y <= max(p2[1], p1[1]):
                # Check if the point is to the left of the maximum x coordinate of the edge
                if x <= max(p2[0], p1[0]):
                    # Calculate the x-intersection of the line connecting the point to the edge
                    x_intersection = (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0]

                    # Check if the point is on the same line as the edge or to the left of the x-intersection
                    if p1[0] == p2[0] or x <= x_intersection:
                        # Flip the inside flag
                        inside = not inside

        # Store the current point as the first point for the next iteration
        p1 = p2

    # Return the value of the inside flag
    return inside

with open(os.path.dirname(os.path.realpath(__file__)) + "/input.txt", "r") as file:
    for line in file:
        data.append([int(i) for i in line.strip().split(",")])


for i in range(len(data)):
    for j in range(len(data)):
        E = (1 + abs(data[j][0] - data[i][0])) * (1 + abs(data[j][1] - data[i][1]))

        corners = [[data[i][0], data[j][1]], [data[j][0], data[i][1]]]
        for c in corners:
            if not point_in_polygon(c,data):
                break
        else:
            if E > max_area:
                max_area = E

print(max_area)