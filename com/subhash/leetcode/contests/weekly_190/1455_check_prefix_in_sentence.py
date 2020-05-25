class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for i in range(len(words)):
            if words[i].startswith(searchWord):
                return i+1
        return -1


if __name__ == "__main__":
    s = Solution()
    count = s.isPrefixOfWord("i love eating burger", "burg")
    print(count)
