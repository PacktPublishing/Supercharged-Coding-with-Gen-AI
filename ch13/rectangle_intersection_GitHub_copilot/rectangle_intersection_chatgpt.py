def rect_intersection_area(rect1, rect2):
    x1_1, y1_1, x2_1, y2_1 = rect1
    x1_2, y1_2, x2_2, y2_2 = rect2

    # Validate input rectangles
    def is_invalid_rect(x1, y1, x2, y2):
        return x1 >= x2 or y1 >= y2

    if is_invalid_rect(x1_1, y1_1, x2_1, y2_1) or is_invalid_rect(x1_2, y1_2, x2_2, y2_2):
        raise ValueError("Invalid rectangle with non-positive width or height")

    # Find intersection bounds
    inter_left = max(x1_1, x1_2)
    inter_right = min(x2_1, x2_2)
    inter_bottom = max(y1_1, y1_2)
    inter_top = min(y2_1, y2_2)

    # Check if rectangles intersect
    if inter_left >= inter_right or inter_bottom >= inter_top:
        return 0

    # Compute and return intersection area
    return (inter_right - inter_left) * (inter_top - inter_bottom)
