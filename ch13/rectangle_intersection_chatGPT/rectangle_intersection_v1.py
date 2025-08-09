def rect_intersection_area(rect1, rect2):
    """
    Calculate the area of intersection between two rectangles.
    Each rectangle is represented as a tuple (x1, y1, x2, y2):
    - (x1, y1): bottom-left corner
    - (x2, y2): top-right corner
    """
    # Calculate the overlapping region
    x_overlap = max(0, min(rect1[2], rect2[2]) - max(rect1[0], rect2[0]))
    y_overlap = max(0, min(rect1[3], rect2[3]) - max(rect1[1], rect2[1]))

    # If there is an overlap, calculate the area
    return x_overlap * y_overlap