def rect_intersection_area(rect1, rect2):
    """
    Calculate the area of intersection between two rectangles.
    Each rectangle is represented as a tuple (x1, y1, x2, y2):
    - (x1, y1): bottom-left corner
    - (x2, y2): top-right corner
    """
    # Ensure the rectangles are valid
    if rect1[0] >= rect1[2] or rect1[1] >= rect1[3]:
        raise ValueError(f"Invalid rectangle dimensions for rect1: {rect1}")
    if rect2[0] >= rect2[2] or rect2[1] >= rect2[3]:
        raise ValueError(f"Invalid rectangle dimensions for rect2: {rect2}")

    # Calculate the overlapping region
    x_left = max(rect1[0], rect2[0])
    y_bottom = max(rect1[1], rect2[1])
    x_right = min(rect1[2], rect2[2])
    y_top = min(rect1[3], rect2[3])

    # Check if there is an actual overlap
    if x_left < x_right and y_bottom < y_top:
        return (x_right - x_left) * (y_top - y_bottom)
    else:
        return 0  # No overlap