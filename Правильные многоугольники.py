from PIL.ImageDraw import ImageDraw
import math


class MyImageDraw(ImageDraw):
    def regular_polygon(self, center_coords, sides, radius, rotation=0, fill=None, outline=None):
        points = []
        angle = -math.degrees(rotation)
        while angle < 360 - math.degrees(rotation):
            points.append((int(-math.sin(math.radians(angle)) * radius + center_coords[0]),
                           int(-math.cos(math.radians(angle)) * radius + center_coords[1])))
            angle += 360 / sides
        self.polygon(points, fill, outline)



