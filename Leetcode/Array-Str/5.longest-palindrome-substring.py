"""
5.最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


class Solution:
    # 动态规划
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    # 状态转移方程
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i: j + 1]
        return ans

    @staticmethod
    # 中心扩散法
    def longest_palindrome(s: str) -> str:
        def spread_from_center(string, center_index, offset):
            left_index = center_index
            right_index = center_index + offset
            length = len(string)
            while left_index >= 0 and right_index < length and string[left_index] == string[right_index]:
                left_index = left_index - 1
                right_index = right_index + 1
            left_index = left_index + 1
            sub_str = string[left_index: right_index]
            return sub_str

        max_str = ''
        for index in range(len(s)):
            sub1 = spread_from_center(s, index, 0)
            sub2 = spread_from_center(s, index, 1)
            if len(sub1) > len(max_str):
                max_str = sub1
            if len(sub2) > len(max_str):
                max_str = sub2
        return max_str

    @staticmethod
    # 马拉车(Manacher's Algorithm)算法
    def longest_palindrome1(s: str) -> str:
        t = '#' + '#'.join(s) + '#'
        mx = 0
        id = 0
        p = [0] * len(t)

        for i in range(len(t)):
            if i < mx:
                # 精华
                p[i] = min(mx - i, p[2 * id - i])
            else:
                p[i] = 1

            while i >= p[i] and i + p[i] < len(t) and t[i - p[i]] == t[i + p[i]]:
                p[i] += 1
            if mx < i + p[i]:
                mx, id = i + p[i], i

        i_res = p.index(max(p))
        s_res = t[i_res - (p[i_res]-1): i_res + p[i_res]]
        return s_res.replace('#', '')


if __name__ == '__main__':
    ret = Solution().longest_palindrome1("cbbd")
    print(ret)
