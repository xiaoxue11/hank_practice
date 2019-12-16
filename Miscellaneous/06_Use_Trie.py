"""
Created on :  10:22 AM
Author : Xue Zhang
"""


class Trie:
    def __init__(self):
        """Initialize the data structure"""
        self.root = {}
        self.end = -1

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur_node = self.root
        for c in word:
            if c not in cur_node:
                cur_node[c] = {}
            cur_node = cur_node[c]
        cur_node[self.end] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur_node = self.root
        for c in word:
            if c not in cur_node:
                return False
            curNode = cur_node[c]

        if self.end not in cur_node:
            return False
        return True


if __name__ == '__main__':
    t = Trie()
    t.insert('abcd')
    t.insert('aabd')
    param = t.search('abcd')
    print(param)




