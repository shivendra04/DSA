def find_subset_sum(ind, arr, size, sum_list, subset_sum):
    if ind == size:
        sum_list.append(subset_sum)
        return
    
    # pick
    find_subset_sum(ind+1, arr, size, sum_list, subset_sum+arr[ind])
    # not pick
    find_subset_sum(ind+1, arr, size, sum_list, subset_sum)



def main():
    arr = [1,3,2]
    n = len(arr)
    sum_list = []
    find_subset_sum(0, arr, n, sum_list, 0) 
    print(sorted(sum_list))

main()