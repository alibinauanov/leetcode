class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        freq = Counter(word)
        cf = Counter(freq.values())

        if len(cf) == 1:
            (f, c) = next(iter(cf.items()))
            return f == 1 or c == 1
        
        if len(cf) == 2:
            (f1, c1), (f2, c2) = sorted(cf.items())
            return (f1 == 1 and c1 == 1) or (f2 == f1 + 1 and c2 == 1)
            
        return False