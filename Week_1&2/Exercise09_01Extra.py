def main():
    s = input("Enter x1, y1, x2, y2, x3, y3, x4, y4: ")
    points = [float(x) for x in s.split()]
    p1 = Point2D(points[0], points[1])
    p2 = Point2D(points[2], points[3])
    p3 = Point2D(points[4], points[5])
    p4 = Point2D(points[6], points[7])
    
    result = getIntersectingPoint(p1, p2, p3, p4)
    
    if result == None:
        print("The two lines are parallel")
    else:
        print("The intersecting point is at (" + str(result.x) + ", " +  str(result.y) + ")")


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def linearEquation(a, b):
    determinant = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    
    if determinant == 0:
        return None
    else:
        x = (b[0] * a[1][1] - b[1] * a[0][1]) / determinant
        y = (b[1] * a[0][0] - b[0] * a[1][0]) / determinant
        return Point2D(x, y)

def getIntersectingPoint(p1, p2, p3, p4):
    x1, y1, x2, y2, x3, y3, x4, y4 = p1.x, p1.y, p2.x, p2.y, p3.x, p3.y, p4.x, p4.y 
    a = (y1 - y2)
    b = -(x1 - x2)
    c = (y3 - y4)
    d = -(x3 - x4)
    e = (y1 - y2) * x1 - (x1 -x2) * y1
    f = (y3 - y4) * x3 - (x3 -x4) * y3
    
    result = linearEquation([[a, b], [c, d]], [e, f])
        
    if result == None:
        return None
    else:
        return result

main()
