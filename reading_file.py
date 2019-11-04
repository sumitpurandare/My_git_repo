def intersect (s1,s2):
    res = []
    for x in s1:
        if x in s2:
            res.append(x)
    return res
    print(res)

intersect([1,2,3,4,5],[1,2,45,23,4,43])
