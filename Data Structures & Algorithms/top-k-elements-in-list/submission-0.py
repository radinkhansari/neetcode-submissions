class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
        '''counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        freq = sorted(counts, key = lambda x: counts[x], reverse = True)
        return freq[:k]'''
                