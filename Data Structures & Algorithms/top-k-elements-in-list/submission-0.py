class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        # Keep only elements with frequency >= k
        result = [num for num, count in freq.most_common(k)]
        return result
        