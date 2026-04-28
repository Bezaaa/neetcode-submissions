class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq_count = 0
        count = defaultdict(int)

        i=0
        max_len = 0
        for j in range(len(s)):
            count[s[j]]+=1
            max_freq_count = max(max_freq_count , count[s[j]] )
            while (j - i + 1) - max_freq_count > k:
                count[s[i]] -= 1
                i += 1
            max_len = max(max_len , j - i + 1)
        return max_len
            




        