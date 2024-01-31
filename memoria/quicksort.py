def quicksort(arr):
    if len(arr) <= 1:
        return arr
    privot = arr[len(arr)// 2]
    left = [x for x in arr if x < privot]
    middle = [x for x in arr if x == privot]
    right = [x for x in arr if x > privot]
    return quicksort(left) + middle + quicksort(right)