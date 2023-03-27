def missingNumbers(arr, brr):
    # Write your code here
    lst=[]
    for i in brr:
        if i not in arr or arr.count(i) != brr.count(i) and i not in lst:
            lst.append(i)
    return sorted(lst)
