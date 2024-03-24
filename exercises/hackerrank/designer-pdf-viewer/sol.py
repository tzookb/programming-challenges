def designerPdfViewer(h, word):
    max_h = 0
    for c in word:
        idx = ord(c) - ord("a")
        max_h = max(max_h, h[idx])
    
    return len(word) * max_h
