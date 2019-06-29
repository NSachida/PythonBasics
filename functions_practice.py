import math

# getting distance between two points
# learning functions and dictionaries

square = lambda num : num*num

def getDistance(p1, p2):
    x_dif = p1.get("x") - p2.get("x")
    y_dif = p1.get("y") - p2.get("y")
    dis = math.sqrt(square(x_dif) + square(y_dif))
    return dis

point1 = {
    "x": -5,
    "y": 6
}
point2 = {
    "x": 3,
    "y": 4
}

print("Distance: ", getDistance(point1, point2))

# finding GCD and LCM
# learning while loop, boolean syntax and conditinal assignments
# using functions and dictionaries 


def findGCD(set):
    small = set.get("num1") if set.get("num1") < set.get("num2") else set.get("num2") 
    for i in range(small, 0,-1):
        if set.get("num1") % i==0 and set.get("num2") % i==0:
            return i


def findLCM(set):
    great = set.get("num1") if set.get("num1") > set.get("num2") else set.get("num2") 
    while (True):
        if great % set.get("num1") == 0 and great % set.get("num2") == 0:
            return great
        great+=1


set = dict(num1= 3, num2=19)
print("GCD: ", findGCD(set), "LCM: ", findLCM(set))