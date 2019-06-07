# finding intesection of two sets:
# learning conditional statments, loops and arrays
firstArr = [3, 1, 5, 11, 22]
secondArr = [6, 3, 1, 5, 14, 16]
intersection = []
print(firstArr, secondArr)
for num in firstArr:
    if num in secondArr and num not in intersection:
        intersection.append(num)
print(intersection)

# bubble sort algorithm
# learning nested loops and swapping syntax

arr = [1, 2, 3, 7, -5, 16, 222, -5, 0, 0, -3, 11, 23]

for i in range(len(arr)-2):
    for j in range(len(arr)-i-2):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)
