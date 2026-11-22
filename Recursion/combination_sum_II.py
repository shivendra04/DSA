def find_combination_sum_2(ind, arr, target, size, ans, ds):
    if target == 0:
        ans.append(ds.copy())
        return 
    for i in range(ind, size):
        '''
        Think of ind as the starting point of the current recursion level.

        i == ind: This is the first element we're considering at this level. Allow it.

        i > ind: We have already considered an earlier element at this level. If the current element is a duplicate of the previous one, skip it.
        '''
        if i>ind and arr[i] == arr[i-1]:
            continue
        if arr[i]>target:
            break
        ds.append(arr[i])
        find_combination_sum_2(i+1, arr, target-arr[i], size, ans, ds)
        ds.pop()

def main():
    arr = [1,1,2,2]
    target = 4
    n = len(arr)
    ans = []
    ds = []
    find_combination_sum_2(0, arr, target, n, ans, ds)
    print(ans)

main()