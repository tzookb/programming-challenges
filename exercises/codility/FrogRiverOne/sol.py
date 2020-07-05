
a = [1,2,3,4,4]
x = 5

def solution(x, a):
    steps = [0] * x
    counter = 0
    for sec, leaf in enumerate(a):
        if not steps[leaf-1]:
            steps[leaf-1] = 1
            counter += 1
        if counter == x:
            break
    
    if counter < x:
        return -1
    return sec

solution(x, a)