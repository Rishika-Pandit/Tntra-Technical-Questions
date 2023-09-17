#Give biggest and smallest number in array 
import numpy as np

li = list(map(int, input().strip().split()))
arr = np.array(li)
min = arr[0]
max = arr[0]

for i in range(len(arr)):
    if arr[i]>max:
        max = arr[i]
    elif arr[i]<max:
        continue
print(f"Maximum is: {max}")

for i in range(len(arr)):
    if arr[i]<min:
        min = arr[i]
    elif arr[i]>min:
        continue
print(f"Minimum is: {min}")