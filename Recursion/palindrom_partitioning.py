def is_palindrom(s):
    if s == s[::-1]:
        return True
    return False

def palindrom_partition(ind, string, size, res, ds):
    if ind == size:
        res.append(ds.copy())
        return

    for i in range(ind, size):
        if is_palindrom(string[ind:i+1]):
            ds.append(string[ind:i+1])
            palindrom_partition(i+1, string, size, res, ds)
            ds.pop()

def main():
    string = 'aabb'
    res = []
    ds = []
    palindrom_partition(0, string, len(string), res, ds)
    print(res)

main()