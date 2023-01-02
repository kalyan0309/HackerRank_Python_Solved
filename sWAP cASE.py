def swap_case(s):
    fs=""
    for i in s:
        if i.islower():
             i = i.upper()
             fs+=i
        else:
            i = i.lower()
            fs+=i
    return fs
