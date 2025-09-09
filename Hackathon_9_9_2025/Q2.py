def rotateLeft(d, arr):
    n = len(arr)
    d = d % n  
    return arr[d:] + arr[:d]

n, d = map(int, input("Enter size of array and d rotations: ").split())
arr = list(map(int, input("Enter array elements: ").split()))

result = rotateLeft(d, arr)

print("Rotated Array:", *result)
