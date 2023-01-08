def person_lister(f):
    def inner(people):
        # complete the function
        l=[]
        people.sort(key=lambda x: x[2])
        for i in people:
            if i[3] == "F":
                i[1] = f"Ms. {i[0]} {i[1]}"
                l.append(i[1])
            else:
                i[1] = f"Mr. {i[0]} {i[1]}"
                l.append(i[1])
        return l
    return inner
