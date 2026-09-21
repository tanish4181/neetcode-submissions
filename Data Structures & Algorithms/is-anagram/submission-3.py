class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_map = {}

        for c in s:
            
            count_map[c] = count_map.get(c,0) + 1
        
        for c in t:
            
            count_map[c] = count_map.get(c,0) - 1
        
        for count in count_map.values():
            if count!=0:
                return False
            
        return True
            