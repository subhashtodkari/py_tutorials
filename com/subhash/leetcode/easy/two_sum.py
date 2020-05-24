from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]].append(i)
            else:
                d[nums[i]] = [i]

        # print(d)

        for (num, l) in d.items():
            if num == target // 2:
                if len(l) == 2:
                    return l
            else:
                if (target - num) in d:
                    return [l[0], d[target - num][0]]


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))
