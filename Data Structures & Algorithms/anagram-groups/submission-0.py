class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        
        output = []
        prev_pattern = []
        for s in strs:
            sorted_s = sorted(s)
            if sorted_s in prev_pattern:
                i = prev_pattern.index(sorted_s)
                output[i].append(s)
            else:
                prev_pattern.append(sorted_s)
                output.append([s])
        return output  