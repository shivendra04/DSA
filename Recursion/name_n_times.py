def print_name_n_times(i, n):
    if i>n:
        return
    print(name)
    print_name_n_times(i+1, n)

n = 5
name = 'Shivendra'
print_name_n_times(1, n)