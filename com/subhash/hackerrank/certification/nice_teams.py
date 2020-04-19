
def maxPairs(skillLevel, minDiff):
    # Write your code here
    sl = sorted(skillLevel)
    i = 0
    mid = len(sl) // 2
    j = mid
    pairs = 0
    while i < mid and j < len(sl):
        # print(i, j, len(sl))
        while (sl[j] - sl[i] < minDiff):
            j += 1
            if j >= len(sl):
                break
        if j >= len(sl):
            break
        pairs += 1
        i += 1
        j += 1

    return pairs

    return pairs


if __name__ == "__main__":
    print(maxPairs([709552565, 473251358, 803612259, 579542802, 183012194, 689345248, 151290765, 123232501, 994391793, 25107191, 862726097], 440987423))