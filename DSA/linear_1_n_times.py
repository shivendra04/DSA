def one_to_n_times(i, n):
    if i > n:
        return
    print(i)
    one_to_n_times(i+1, n)

one_to_n_times(1, 5)