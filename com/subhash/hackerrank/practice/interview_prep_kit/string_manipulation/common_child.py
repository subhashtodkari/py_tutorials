
def print_dp(dp, s1, s2, msg):
    print("dp " + msg)
    s1, s2 = s2, s1
    print(s1)
    print(s2)
    s2 = " " + s2
    i = 0
    print("  " + " ".join([c for c in " " + s1]))
    for row in dp:
        print(s2[i] + " " + " ".join([str(c) for c in row]))
        i += 1
    print()


def common_child_length(s1, s2):
    dp = [[0 for x in range(len(s1) + 1)] for y in range(len(s2) + 1)]

    # print_dp(dp, s1, s2, " initialized")

    for row in range(1, len(s1) + 1):
        s1_char = s1[row - 1]
        # print("s1_char: ", s1_char)
        matched = 0
        for col in range(1, len(s2) + 1):
            # print("s2_char: ", s2[col - 1])
            dp[row][col] = max(dp[row][col - 1], dp[row - 1][col - 1], dp[row - 1][col])
            if not matched and s1_char == s2[col - 1]:
                # if s1_char == s2[col - 1]:
                matched = 1
                dp[row][col] = max(matched + dp[row - 1][col - 1], dp[row][col])
                matched = 0

        # print(dp[row])
        # print()

    # print_dp(dp, s1, s2, " finalized")

    return dp[len(s1)][len(s2)]


if __name__ == "__main__":
    # s1, s2 = input().split()
    # print(common_child_length(s1, s2))
    '''
    print(common_child_length("AA", "BB"))
    print(common_child_length("HARRY", "SALLY"))
    print(common_child_length("HARRY", "RRASY"))
    print(common_child_length("ABCDEF", "FBDAMN"))
    '''
    print(common_child_length("NOHARAAA", "SHINCHAN"))
    print(common_child_length("SHINCHAN", "NOHARAAA"))
