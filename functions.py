# getting distance between two points
# learning functions and dictionaries
import math

def getDistance(p1, p2):
    x_dif=p1.get("x") - p2.get("x")
    y_dif=p1.get("y") - p2.get("y")
    dis = math.sqrt(math.pow(x_dif,2)+math.pow(y_dif,2))
    return dis

point1 = {
    "x": -5,
    "y": 6
}
point2 = {
    "x": 3,
    "y": 4
}

print(getDistance(point1, point2))