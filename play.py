paths =[[1, 2, 5], [1, 3]]
res = ["->".join([str(pathStep) for pathStep in pathItems]) for pathItems in paths]
# res = list(map(lambda x: "->".join(str(x)), arr))
print(res)