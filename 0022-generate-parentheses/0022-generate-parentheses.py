class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(cur: list[str], open_used: int, close_used: int):
            if len(cur) == 2 * n:
                res.append("".join(cur))
                return
            if open_used < n:                      # we can add '('
                cur.append('(')
                backtrack(cur, open_used + 1, close_used)
                cur.pop()
            if close_used < open_used:             # we can add ')'
                cur.append(')')
                backtrack(cur, open_used, close_used + 1)
                cur.pop()
        backtrack([], 0, 0)
        return res