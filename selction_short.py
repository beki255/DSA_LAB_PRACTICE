# arr=[12,10,9,20,1]

# for i in range(len(arr)):
#     minindex=i

#     for j in range(i+1, len(arr)):
#         if(arr[j])>arr[minindex]:
#             minindex=j

#     if minindex !=i:
#         arr[i], arr[minindex]= arr[minindex], arr[i]

# print(f"sorted array: {arr}")

arr = [12, 10, 9, 20, 1]

i = 0

while i < len(arr):
    minindex = i
    j = i + 1
    
    while j < len(arr):
        if arr[j] < arr[minindex]:
            minindex = j
        j = j + 1

    if minindex != i:
        arr[i], arr[minindex] = arr[minindex], arr[i]

    i += 1

print(f"sorted array: {arr}")



