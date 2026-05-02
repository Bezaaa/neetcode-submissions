class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            # find the '#'
            while s[j] != "#":
                j += 1

            # get the length
            length = int(s[i:j])

            # extract the word
            word = s[j+1 : j+1+length]
            res.append(word)

            # move pointer forward
            i = j + 1 + length

        return res