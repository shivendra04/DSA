def count_subsequence_with_sum_k(index,size, given_sum, curr_sum, arr):
    if index == size:
        if given_sum == curr_sum:
            return 1
        else:
            return 0
    curr_sum += arr[index]
    left = count_subsequence_with_sum_k(index+1, size, given_sum, curr_sum, arr)

    curr_sum -= arr[index]
    right = count_subsequence_with_sum_k(index+1, size, given_sum, curr_sum, arr)
    return left + right


def main():
    arr = [1,2,1]
    size = len(arr)
    given_sum = 2
    print(count_subsequence_with_sum_k(0, size, given_sum, 0, arr))

main()
