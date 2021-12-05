from collections import deque

g = {}
g["you"] = ["Josh", "Bob", "John", "Alice", "Troy"]
g["Josh"] = ["you", "Bob", "Frank", "Callum"]

def getLastLetter(n):
    return n[-1] == 'm'

def bfs(n):
    s_q = deque()
    s_q += g[n]
    s = []
    d_c = set(g[n])
    while s_q:
        p = s_q.popleft()
        if not p in s:
            s.append(p)
            if g.get(p) is not None:
                for r in g[p]:
                    if getLastLetter(r):
                        print r + "'s name ends with m."
                        return True
                    if r not in d_c:
                        print "No Relation: " + r
                    else:
                        print "Relation: " + r
                s_q += g[p]
    return False

bfs("you")
