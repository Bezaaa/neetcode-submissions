class Solution:
    def encode(self, strs):
   
        if not strs:
            return ""
        return "\x1e".join(str(len(s)) + ":" + s for s in strs)

    def decode(self, s):
        """Decodes a single string to a list of strings."""
        if not s:
            return []
        i, n, res = 0, len(s), []
        while i < n:
            colon_index = s.find(":", i)
            length = int(s[i:colon_index])
            i = colon_index + 1
            res.append(s[i:i + length])
            i += length + 1
        return res


