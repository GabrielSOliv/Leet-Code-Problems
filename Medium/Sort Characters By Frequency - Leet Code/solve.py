class Solution:
    def frequencySort(self, s: str) -> str:
        hm = {}
        res = ''

        for i in range(len(s)):
            hm[s[i]] = 1 + hm.get(s[i], 0)

        hm = dict(sorted(hm.items(), key=lambda x: x[1], reverse=True))

        for key, value in hm.items():
            res += key * value

        return res
