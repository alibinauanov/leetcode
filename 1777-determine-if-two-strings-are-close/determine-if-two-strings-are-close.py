class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # Step 1: Check if both words have the same unique characters
        if set(word1) != set(word2):
            return False

        # Step 2: Count frequencies of characters in both words
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        # Step 3: Check if the sorted frequency lists match
        return sorted(freq1.values()) == sorted(freq2.values())