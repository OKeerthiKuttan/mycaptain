import operator
def mostfre(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
string=input("enter string")
di=mostfre(string)
di=sorted_d = dict( sorted(di.items(), key=operator.itemgetter(1),reverse=True))
print(di)
