import math
# finding intesection of two sets:
# learning conditional statments, loops and arrays
firstArr = [3, 1, 5, 11, 22]
secondArr = [6, 3, 1, 5, 14, 16]
intersection = []
#print(firstArr, secondArr)
for num in firstArr:
    if num in secondArr and num not in intersection:
        intersection.append(num)
print("intersection: ", intersection)

# bubble sort algorithm
# learning nested loops and swapping syntax

arr = [1, 2, 3, 7, -5, 16, 222, -5, 0, 0, -3, 11, 23]

for i in range(len(arr)-2):
    for j in range(len(arr)-i-2):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted array: ", arr)

# solving quadratic equations
# learning conditinal statements

a = 1
b = 6
c = 1
delta = b*b - 4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta))/2*a
    x2 = (-b - math.sqrt(delta))/2*a
    print("Solution set", x1,x2)
elif delta==0:
    x = (-b + math.sqrt(delta))/2*a
    print("Solution set", x)
else:
    print("No solution in R")
