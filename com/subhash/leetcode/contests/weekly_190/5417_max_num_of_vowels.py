class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_cnt = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        c = 0
        for i in range(k):
            # print(1, i, s[i])
            if s[i] in vowels:
                c += 1

        if c > max_cnt:
            # print("Initial max: ", c)
            max_cnt = c

        s_len = len(s)
        for i in range(k, s_len):
            # print(2, i, s[i])
            if s[i] in vowels:
                c += 1
            if s[i - k] in vowels:
                c -= 1

            if c > max_cnt:
                # print("new max: ", c)
                max_cnt = c

        return max_cnt


if __name__ == "__main__":
    s = Solution()
    print(s.maxVowels("leetcode", 3))