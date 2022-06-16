class Solution:
    def reverseString(self, s: List[str]) -> None:
        sLen = len(s)
        j = sLen-1
        for i in range(sLen//2):
            s[i],s[j] = s[j],s[i]
            j -= 1