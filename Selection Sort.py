def smallest(a):
    s = a[0]
    idx = 0
    for i in range(1, len(a)):
        if a[i] < s:
            idx = i
            s = a[i]
    return idx
    
def selection_sort(a):
    n = []
    for i in range(len(a)):
        s = smallest(a)
        n.append(a.pop(s))
    return n

a = [9, 2, 5, 1, 8, 4]

print selection_sort(a)
