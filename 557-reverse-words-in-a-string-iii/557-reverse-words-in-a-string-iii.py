class Solution:
    def reverseWords(self, s: str) -> str:
        splited = s.split(" ")
        splited= [i[::-1] for i in splited]
        return " ".join(splited)
            