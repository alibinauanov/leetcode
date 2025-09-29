class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        hashTable = Counter(word)
        for i in set(word):
            hashTable[i] -= 1
            if hashTable[i] == 0:
                del hashTable[i]
            vals = list(hashTable.values())
            if len(set(vals)) == 1:
                return True
            hashTable[i] = hashTable.get(i, 0) + 1
        return False