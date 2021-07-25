x = [[1,"a",["cat"],2],[[[3]],"dog"],4,5]
l  = []


def duzlestirici(x):
    for i in x:
        if type(i) == int:
            l.append(i)
        elif type(i) == str:
            l.append(i)

        else:
            a = x.index(i)
            duzlestirici(x[a])

duzlestirici(x)
print(l)
