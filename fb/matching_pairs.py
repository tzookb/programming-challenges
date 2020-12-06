from collections import Counter

def matching_pairs(s, t):
    map_t = {}
    errors = []
    unmatched_s = []
    unmatched_t = []
    matched_s = []
    matched_t = []
    for i, (a, b) in enumerate(zip(s,t)):
        if a != b:
            unmatched_s.append(a)
            unmatched_t.append(b)
        else:
            matched_s.append(a)
            matched_t.append(b)
    unmatched_s = "".join(unmatched_s)
    unmatched_t = "".join(unmatched_t)

    matches = len(s) - len(unmatched_s)

    if unmatched_s == "":
        # no unmatches, so we will check for dups in s
        if len(set(s)) != len(s):
            return matches
        return matches - 2
    if len(unmatched_s) == 1:
        # no unmatches, so we will check for dups in s
        if unmatched_s in matched_s:
            return matches
        else:
            return matches - 1

    s_cnt = Counter()
    t_cnt = Counter()
    for x in unmatched_s:
        s_cnt[x] += 1
    for x in unmatched_t:
        t_cnt[x] += 1
    count = 0
    for c in s_cnt:
        if c not in t_cnt:
            continue
        curCnt = min(t_cnt[c], s_cnt[c])
        count += curCnt
        if count >= 2:
            return matches + 2
    
    if count == 1: 
        return matches + 1
    return matches

    



def test_code() -> None:
    # Test 1)
    assert matching_pairs("abcde", "adcbe") == 5
    assert matching_pairs("abcd", "abcd") == 2
    assert matching_pairs("abce", "abcf") == 2
    assert matching_pairs("abced", "abcfg") == 3
    assert matching_pairs("abced", "abcfe") == 4
    assert matching_pairs("abced", "abcde") == 5
    assert matching_pairs("abceee", "abcdef") == 4
    assert matching_pairs("abcdx", "abxcc") == 4
    assert matching_pairs("dbcd", "dbce") == 3
    assert matching_pairs("mno", "mno") == 1
    assert matching_pairs("mnm", "mnm") == 3
    assert matching_pairs("abcc", "cdea") == 2
    assert matching_pairs("abc", "abd") == 1
    

if __name__ == "__main__":
    test_code()
