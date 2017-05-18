import sys
import bisect
from collections import deque

def dfs(d,start,path=[]):
        q = [start]
        while q:
                v = q.pop()
                if v not in path:
                        path.append(v)
                        q.extend([x for x in d[v][::-1] if x not in path])
        for j in path:
                print j,

def bfs(d,start,path=[]):
        q = deque()
        q.append(start)
        while q:
                v = q.popleft()
                if v not in path:
                        path.append(v)
                        q.extend([x for x in d[v] if x not in path])
        for j in path:
                print j,

r = lambda: sys.stdin.readline()
a,b,c = map(int,r().split())
d = {}
for i in xrange(1,a+1):
        d[i] = []
for i in xrange(0,b):
        x,y = map(int,r().split())
        bisect.insort_left(d[x],y)
        bisect.insort_left(d[y],x)
dfs(d,c)
print ''
bfs(d,c)
