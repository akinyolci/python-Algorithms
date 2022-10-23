
#Sorts two consecutive values in a list and continues this process until the whole list is ordered.

arr = [99,3,44,55,23,32,43]
def bubble(arr):
    for n in range(len(arr)):
        for j in range(n+1,len(arr)):
            if arr[n] > arr[j]:
                arr[n],arr[j] = arr[j],arr[n]
    return
