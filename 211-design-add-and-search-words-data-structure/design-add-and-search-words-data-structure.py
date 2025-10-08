class WordDictionary(object):

    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        # Start the traversal from the root of the trie
        node = self.trie

        for ch in word:
            if not ch in node:
                node[ch] = {}
            # Move to the next node in the trie.
            node = node[ch]
        # After processing all characters, mark the end of a valid word.
        # "$" is a common convention to indicate a word's termination point.
        node["$"] = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def search_in_node(word, node):
            # Iterate through each character of the word with its index.
            for i, ch in enumerate(word):
                # If the current character is not in the current trie node...
                if not ch in node:
                    # ...check if the character is a wildcard '.'
                    if ch == ".":
                        # If it is a wildcard, we must try every possible path from this node.
                        # 'x' will be each character key in the current node's dictionary.
                        for x in node:
                            # We only care about character paths, not the end-of-word marker "$".
                            # Recursively search for the rest of the word (word[i+1:])
                                # starting from the child node (node[x]).
                            if x != "$" and search_in_node(
                                word[i + 1:], node[x]
                            ):
                                return True
                    return False
                # If the character is in the node (and is not a wildcard)...
                else:
                    node = node[ch]
            # After the loop finishes, we have traversed the path for the entire word.
            # We must now check if this path corresponds to a complete word.
            # This is true only if the "$" end-of-word marker exists at the final node.
            return "$" in node
        
        return search_in_node(word, self.trie)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)