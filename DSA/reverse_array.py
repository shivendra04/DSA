def reverse_array(arr):
    n = len(arr)
    def reverse_helper(i, size):
        if  i==size:
            return
        reverse_helper(i+1, size)
        print(arr[i])

    reverse_helper(0, n)

reverse_array([1,2,3,4,5])