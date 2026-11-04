def n_to_one(i, n):
    if i>n:
        return
    n_to_one(i+1, n)
    print(i)

n_to_one(1, 5)