class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Count the frequency of each character in ransomNote and magazine
        ransom_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)
        
        # Check if all characters in ransomNote are available in magazine with sufficient counts
        for char, count in ransom_counts.items():
            if magazine_counts[char] < count:
                return False
        
        return True