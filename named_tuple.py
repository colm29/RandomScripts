# named tuples are immmutable
# come in handy for classes containing just data and no methods
# for comparison - instead of defining __eq__ magic method to compare (to override object ref to object ref comparison) use named tuple

from collections import namedtuple

Point = namedtuple('Point', 'x  y')
p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
print(p1.x, p1.y)
