from collections import Counter

def are_they_equal(a, b):
    ac = Counter()
    bc = Counter()
    for aitem in a:
        ac[aitem] += 1
    for bitem in b:
        bc[bitem] += 1

    for akey in ac:
        if akey not in bc:
            return False
        if ac[akey] != bc[akey]:
            return False
        del bc[akey]
    
    if len(bc):
        return False
    
    return True


def test_code() -> None:
    # Test 1)
    a = [1, 2, 3, 4]
    b = [1, 4, 3, 2]
    assert are_they_equal(a, b)
    print("success")

if __name__ == "__main__":
    test_code()
