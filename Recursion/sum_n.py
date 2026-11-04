# parametarise

def sum_n(n):
    '''parametarized'''
    def helper(i, sum):
        if i<1:
            print(sum)
            return
        helper(i-1, sum+i)
    helper(n, 0)

# sum_n(5)

# Functional

def sum_n_functional(n):
    if n<1:
        return n
    return n + sum_n_functional(n-1)

print(sum_n_functional(5))

