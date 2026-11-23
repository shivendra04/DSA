def all_permutation_of_string(ind, arr, size, ans):
    if ind == size:
        ans.append(arr.copy())
        return
    for i in range(ind, size):
        arr[i], arr[ind] = arr[ind], arr[i]
        all_permutation_of_string(ind+1, arr, size, ans)
        arr[i], arr[ind] = arr[ind], arr[i]


def main():
    arr = [1,2,3]
    n = len(arr)
    ans = []
    all_permutation_of_string(0, arr, n, ans)
    print(ans)

main()

# [1,2,3] -> 123, 132, 213, 232, 412, 321