import unittest
from rectangle_intersection import rect_intersection_area

class TestRectangleIntersectionArea(unittest.TestCase):
    def test_intersecting_rectangles(self):
        rect1 = (0, 0, 4, 4)
        rect2 = (2, 2, 6, 6)
        self.assertEqual(rect_intersection_area(rect1, rect2), 4)

    def test_intersecting_rectangles_swapped(self):
        rect1 = (2, 2, 6, 6)
        rect2 = (0, 0, 4, 4)
        self.assertEqual(rect_intersection_area(rect1, rect2), 4)

    def test_non_intersecting_rectangles(self):
        rect1 = (0, 0, 2, 2)
        rect2 = (3, 3, 5, 5)
        self.assertEqual(rect_intersection_area(rect1, rect2), 0)

    def test_touching_rectangles_corner(self):
        rect1 = (0, 0, 2, 2)
        rect2 = (2, 2, 4, 4)
        self.assertEqual(rect_intersection_area(rect1, rect2), 0)

    def test_contained_rectangle1(self):
        rect1 = (0, 0, 4, 4)
        rect2 = (1, 1, 3, 3)
        self.assertEqual(rect_intersection_area(rect1, rect2), 4)

    def test_contained_rectangle2(self):
        rect1 = (1, 1, 3, 3)
        rect2 = (0, 0, 4, 4)
        self.assertEqual(rect_intersection_area(rect1, rect2), 4)

    def test_partial_overlap(self):        
        rect1 = (0, 0, 5, 5)        
        rect2 = (3, 3, 7, 7)        
        self.assertEqual(rect_intersection_area(rect1, rect2), 4)

    def test_touching_inside(self):
        rect1 = (0, 0, 3, 3)
        rect2 = (2, 2, 3, 3)
        self.assertEqual(rect_intersection_area(rect1, rect2), 1)

    def test_touching_corner(self):
        rect1 = (0, 0, 3, 3)
        rect2 = (2, 2, 3, 3)        
        self.assertEqual(rect_intersection_area(rect1, rect2), 1)   
        
    def test_touching_side_inside(self):        
        rect1 = (0, 0, 3, 3)        
        rect2 = (1, 0, 2, 1)        
        self.assertEqual(rect_intersection_area(rect1, rect2), 1)    
    
    def test_touching_side_outside(self):        
        rect1 = (0, 0, 3, 3)        
        rect2 = (-2, 1, 0, 2)        
        self.assertEqual(rect_intersection_area(rect1, rect2), 0)    

    def test_identical_rectangles(self):        
        rect1 = (-1, 1, 3, 2)        
        rect2 = (-1, 1, 3, 2)        
        self.assertEqual(rect_intersection_area(rect1, rect2), 4)    

    def test_no_height(self):        
        rect1 = (-1, -1, -1, 4)        
        rect2 = (-1, 1, 3, 2)        
        with self.assertRaises(ValueError):
            rect_intersection_area(rect1, rect2) 

    def test_no_width(self):        
        rect1 = (-1, -1, 4, 4)        
        rect2 = (-1, 1, -1, 10)        
        with self.assertRaises(ValueError):
            rect_intersection_area(rect1, rect2)

    def test_single_point_rectangle(self):        
        rect1 = (-1, -1, 4, 4)        
        rect2 = (2, 2, 2, 2)
        with self.assertRaises(ValueError):
            rect_intersection_area(rect1, rect2)

    def test_single_point_rectangle_outside(self):
        rect1 = (-1, -1, 4, 4)
        rect2 = (5, 10, 5, 10)
        with self.assertRaises(ValueError):
            rect_intersection_area(rect1, rect2)

    def test_single_point_rectangle_inside(self):
        rect1 = (-1, -1, 4, 4)
        rect2 = (2, 2, 2, 2)
        with self.assertRaises(ValueError):
            rect_intersection_area(rect1, rect2)

    def test_x_axis_rect1(self):
        rect1 = (-1, -1, -2, 4)
        rect2 = (1, 2, 3, 4)
        with self.assertRaises(ValueError):
            rect_intersection_area(rect1, rect2)

    def test_x_axis_rect2(self):
        rect2 = (-1, -1, -2, 4)
        rect1 = (1, 2, 3, 4)
        with self.assertRaises(ValueError):
            rect_intersection_area(rect1, rect2)

    def test_y_axis_rect1(self):
        rect1 = (0, 4, 2, 1)
        rect2 = (1, 2, 3, 4)
        with self.assertRaises(ValueError):
            rect_intersection_area(rect1, rect2)

    def test_y_axis_rect2(self):
        rect1 = (1, 2, 3, 4)
        rect2 = (0, 4, 2, 1)
        with self.assertRaises(ValueError):
            rect_intersection_area(rect1, rect2)

if __name__ == "__main__":
    unittest.main()         