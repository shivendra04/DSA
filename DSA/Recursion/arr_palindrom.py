def palindrom(arr):
    def helper_palindrom(start, end):
        if start>end:
            return False
        if start == end and arr[start] == arr[end]:
            return True
        if start + 1 == end and arr[start] == arr[end]:
            return True 
        
        if arr[start] == arr[end]:
            return helper_palindrom(start+1, end-1)
        else:
            return False
    return helper_palindrom(0, len(arr)-1)

#print(palindrom([1,2,1]))
print(palindrom("NAMANA"))