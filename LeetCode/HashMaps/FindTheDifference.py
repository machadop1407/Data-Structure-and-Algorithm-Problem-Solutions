class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        hashMap = dict()
        hashMap2 = dict()

        for i in range(len(s)):
            if s[i] in hashMap:
                hashMap[s[i]] += 1
            else:
                hashMap[s[i]] = 1

        for i in range(len(t)):
            if t[i] in hashMap2:
                hashMap2[t[i]] += 1
            else:
                hashMap2[t[i]] = 1

            if t[i] not in hashMap:
                return t[i]
            if hashMap2[t[i]] > hashMap[t[i]]:
                return t[i]

        return t[-1]
