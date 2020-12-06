from collections import Counter

def rotateChar(c, n):
    uni = ord(c)    
    if c.isnumeric():
        circ = 10
    else:
        circ = 26
    
    rotations = n % circ
    uni += rotations
    if c.isnumeric():
        if uni > ord("9"):
            uni = uni + ord("0") - ord("9")-1
    else:
        if uni > ord("z") and c.islower():
            uni = uni + ord("a") - ord("z")-1
        elif uni > ord("Z") and c.isupper():
            uni = uni + ord("A") - ord("Z")-1
    return chr(uni)

def rotationalCipher(input, rotation_factor):
    ciphered = []
    for c in input:
        if c.isalpha() or c.isnumeric():
            nextC = rotateChar(c, rotation_factor)
        else:
            nextC = c
        ciphered.append(nextC)
    return "".join(ciphered)

input_1 = "All-convoYs-9-be:Alert1."
rotation_factor_1 = 4
expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
res = rotationalCipher(input_1, rotation_factor_1)

print(res)
print(expected_1 == res)
