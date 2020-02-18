from collections import defaultdict

def freqQuery(queries):
    d = defaultdict(lambda: 0); output = []
    f = defaultdict(set)

    for (c,v) in queries:
        if c==3: 
          output.append(int( len(f[v])>0 ))
          continue
        f[d[v]].discard(v)
        if c==1:
          d[v] += 1
        elif d[v]>0:
          d[v] -= 1
        f[d[v]].add(v)
        print(f)
        print(d)
        print('------')

    return output

q = [
  [1, 3],
  [2, 3],
  [3, 2],
  [1, 4],
  [1, 5],
  [1, 5],
  [1, 4],
  [3, 2],
  [2, 4],
  [3, 2],
]
print(freqQuery(q))