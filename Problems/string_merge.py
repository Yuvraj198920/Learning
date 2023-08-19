"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other, append the additional letters onto the end
of the merged string.
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
"""

class Merge_alternate:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2
        self.me = ""

    def merge_words(self):
        for idx, i in enumerate(self.word1):
            self.me += i
            if idx+1 != len(self.word1):
                self.me += "-"

        for jdx, j in enumerate(self.word2):
            for kdx, k in enumerate(self.me):
                if k == "-":
                    self.me = self.me[:kdx] + j + self.me[kdx+1:]
                    break

                elif kdx == len(self.me)-1:
                    self.me = self.me + self.word2[jdx:]
                    break
        return self.me

    def check(self, index):
        if self.me[index] == "-":
            return True
        else:
            return False


merge_wr =  Merge_alternate("abc", "pqrs")
combined = merge_wr.merge_words()
check_ = merge_wr.check(1)
print(combined)




