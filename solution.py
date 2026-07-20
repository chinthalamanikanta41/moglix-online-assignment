class Solution:
    def longestValidParentheses(self, s: str) -> int:
        index_stack = [-1]
        longest = 0

        for index in range(len(s)):
            if s[index] == '(':
                index_stack.append(index)
            else:
                index_stack.pop()

                if not index_stack:
                    index_stack.append(index)
                else:
                    current_length = index - index_stack[-1]
                    longest = max(longest, current_length)

        return longest


text = input().strip()
solution = Solution()
print(solution.longestValidParentheses(text))
