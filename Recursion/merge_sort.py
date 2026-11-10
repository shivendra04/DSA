# also is to divide and merge
# play around indexes instead of breaking the array
# recursion + backtracking

def merge(arr, low, mid, high):
    merged_arr = []
    left = low
    right = mid + 1
    while left<=mid and right <=high:
        if arr[left]<=arr[right]:
            merged_arr.append(arr[left])
            left += 1
        else:
            merged_arr.append(arr[right])
            right += 1

    while left <= mid:
        merged_arr.append(arr[left])
        left += 1
    while right <= high:
        merged_arr.append(arr[right])
        right += 1

    for i in range(len(merged_arr)):
        arr[low+i] = merged_arr[i]
    return arr

def merge_sort(arr, low, high):
    mid = (low + high)//2
    if low >= high:
        return
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)

    return arr

def main():
    arr = [1,3,5,6,4,3,2]
    low = 0
    high = len(arr)-1
    merge_sort(arr, low, high)
    return arr

print(main())

