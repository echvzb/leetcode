class Solution:
    def letter_combinations(self, digits: str) -> List[str]:
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        def backtrack(current, digits):
            if len(digits) == 0:
                if current != "":
                    result.append(current)
                return
            for letter in keyboard[digits[0]]:
                backtrack(current + letter, digits[1:])

        backtrack('', digits)
        return result
        