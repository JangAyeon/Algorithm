arr=[5,3,7,9,5,2,6]

#1
arrMin=float("inf")
for i in range(len(arr)):
    if arr[i]<arrMin:
        arrMin=arr[i]


#2
arrMin=arr[0]
for i in range(1,len(arr)):
    if arr[i]<arrMin:
        arrMin=arr[i]

#3
arrMin=float("inf")
for x in arr:
    if x<arrMin:
        arrMin=x

print(arrMin)