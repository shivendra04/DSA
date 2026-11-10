def subsequence_with_sum_k(size, index, arr, given_sum, cur_sum, sub_seq = None):
    if sub_seq == None:
        sub_seq = []
    if index == size:
        if given_sum == cur_sum:
            print(sub_seq)
        return 
    sub_seq.append(arr[index])
    cur_sum += arr[index]
    subsequence_with_sum_k(size, index+1, arr, given_sum, cur_sum, sub_seq) # take the current index
    #back trace to remove current element
    sub_seq.pop()
    cur_sum -= arr[index]
    # do not take current element
    subsequence_with_sum_k(size, index+1,arr, given_sum, cur_sum, sub_seq)


def main():
    arr = [1,2,1]
    size = len(arr)
    given_sum = 2
    subsequence_with_sum_k(size, 0, arr, given_sum, 0)

main()

