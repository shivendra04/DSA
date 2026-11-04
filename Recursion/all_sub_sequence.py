def all_sub_sequence(arr, size, i, sub = None):
    if sub == None:
        sub = []

    if i==size:
        print(sub)
        return 
    # Choice 1: Take the element at index i
    sub.append(arr[i]) # take the element at index i
    all_sub_sequence(arr, size, i+1, sub) # take element at index i
    # Backtrack: Remove the element to try the next choice
    sub.pop()
    # Choice 2: Do not take the element at index i
    all_sub_sequence(arr, size, i+1, sub) # do not take the element at index i


def main():
    arr = [1,2,3]
    size = len(arr)
    all_sub_sequence(arr,size, 0)
main()