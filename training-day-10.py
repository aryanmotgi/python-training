class Rectangle:
    """ A Python object that describes the properties of a rectangle """
    def __init__(self, width, height, center=(0.0, 0.0)):
        """ Sets the attributes of a particular instance of `Rectangle`.

            Parameters
            ----------
            width : float
                The x-extent of this rectangle instance.

            height : float
                The y-extent of this rectangle instance.

            center : Tuple[float, float], optional (default=(0, 0))
                The (x, y) position of this rectangle's center"""
        self.width = width
        self.height = height
        self.center = center

    def __repr__(self):
        """ Returns a string to be used as a printable representation
            of a given rectangle."""
        return "Rectangle(width={w}, height={h}, center={c})".format(h=self.height,
                                                                     w=self.width,
                                                                     c=self.center)
    
    def __str__(self):
        """ Returns a string to be used as a printable representation
            of a given rectangle."""
        return "Rectangle with width {w}, height {h}, and center {c}".format(h=self.height,
                                                                     w=self.width,
                                                                     c=self.center)

    def compute_area(self):
        """ Returns the area of this rectangle

            Returns
            -------
            float"""
        return self.width * self.height

    def compute_corners(self):
        """ Computes the (x, y) corner-locations of this rectangle, starting with the
            'top-right' corner, and proceeding clockwise.

            Returns
            -------
            List[Tuple[float, float], Tuple[float, float], Tuple[float, float], Tuple[float, float]]"""
        cx, cy = self.center
        dx = self.width / 2.0
        dy = self.height / 2.0
        return [(cx + x, cy + y) for x,y in ((dx, dy), (dx, -dy), (-dx, -dy), (-dx, dy))]

test = Rectangle(4,5)
print(test)
