class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digits_to_letters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        combos = [""]  
        for d in digits:
            next_combos = []
            for prefix in combos:
                for ch in digits_to_letters[d]:
                    next_combos.append(prefix + ch)
            combos = next_combos
        return combos    