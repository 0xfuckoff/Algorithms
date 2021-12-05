def bin_search(a, f, l, x):
    if l >= f:
        m = f + (l - f) // 2
        if a[m] == x:
            return m
        elif a[m] <= x:
            return bin_search(a, m+1, l, x)
        else:
            return bin_search(a, f, m-1, x)
    else:
        return None

a = [1, 3, 5, 7, 9]

print bin_search(a, 0, len(a) - 1, 7)
