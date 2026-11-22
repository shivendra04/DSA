def subset_sum_2(ind, size, arr, ds, ans):
    ans.append(ds.copy())
    for i in range(ind, size):
        if i>ind and arr[i] == arr[i-1]:
            continue
        ds.append(arr[i])
        subset_sum_2(i+1, size, arr, ds, ans)
        ds.pop()

def main():
    arr = [1,2,2,2,3,3]
    n =len(arr)
    ds = []
    ans = []
    subset_sum_2(0, n, arr, ds, ans)
    print(ans)

main()