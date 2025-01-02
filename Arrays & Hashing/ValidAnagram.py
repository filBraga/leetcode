# Sorting - O(n log n)
def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

# Set - O(n + m)
def isAnagramAlternative(self, s: str, t: str) -> bool:
    #check len
    if len(s) != len(t):
        return False

    #create hashmaps
    hashmapS, hashmapT = {}, {}

    #go through each string
    for i in range(len(s)):
        hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)
        hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)
    
    return hashmapT == hashmapS
    