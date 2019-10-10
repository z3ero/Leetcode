#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 实现三进制 不进位 相加
        # ones 保存遍历到当前，某个二进制位上是否出现 1 个 1
        # twos 保存遍历到当前，某个二进制位上是否出现 2 个 1
        # 当 ones 和 twos 某个位同时为1，表示该位置出现了3个1, ones和twos该位置同时归0
        ones, twos, threes = 0, 0, 0
        for num in nums:
            twos |= ones & num  # 二进制某位出现1次时，twos为0，出现2次时，twos为1
            ones ^= num  # 二进制某位出现2次时，ones为0，出现1次或者3次时，ones为1
            threes = ones & twos # 二进制某位出现3次时，twos为1, ones 也为1
            ones &= ~threes  # 将二进制下出现3次的位置置为 0
            twos &= ~threes  
        return ones

# @lc code=end

