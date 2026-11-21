def find_combination(ind, arr, size, target, res , ds):

    # base case
    if ind == size:
        if target == 0:
            res.append(ds.copy())
            #print(ds)
        return

    # pick (same index because we can reuse elements)
    if arr[ind]<=target:
        ds.append(arr[ind])
        find_combination(ind, arr, size, target-arr[ind], res, ds)
        # back track
        ds.pop()
    # Non-pick (move to next index)
    find_combination(ind+1, arr, size, target, res, ds)
    

def main():
    arr = [2,3,6,7]
    target = 7
    n = len(arr)
    res =[]
    ds = []
    find_combination(0, arr, n, target,res, ds)
    print(res)
main()