class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap1 = dict()
        hashmap2 = dict()
        for i in s:
            hashmap1[i]=hashmap1.get(i,0)+1
        for i in t:
            hashmap2[i]=hashmap2.get(i,0)+1
        for key in hashmap1:
            if hashmap1[key] != hashmap2.get(key,0):
                return False
        return True
        
        