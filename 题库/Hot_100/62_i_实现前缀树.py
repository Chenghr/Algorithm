"""
    题目描述:
        Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，
        用于高效地存储和检索字符串数据集中的键。
        这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

        请你实现 Trie 类：
            - Trie() 初始化前缀树对象。
            - void insert(String word) 
                向前缀树中插入字符串 word 。
            - boolean search(String word) 
                如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；
                否则，返回 false 。
            - boolean startsWith(String prefix) 
                如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；
                否则，返回 false 。

    链接: https://leetcode-cn.com/problems/implement-trie-prefix-tree
"""

class TrieNode:
    """
        - 指向子节点的指针数组 children；数组长度为 26，即小写英文字母的数量，对应小写字母。
        - isEnd，表示该节点是否为字符串的结尾。
    """
    def __init__(self):
        self.isEnd = False
        self.next = [None] * 26

class Trie:
    """
        有根树，每个节点包含以下字段
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """向前缀树中插入字符串 word"""
        node = self.root

        for ch in word:
            index = ord(ch) - ord('a')

            if not node.next[index]:
                node.next[index] = TrieNode()

            node = node.next[index]
        
        node.isEnd = True

    def search(self, word: str) -> bool:
        """如果字符串 word 在前缀树中，且结尾为叶节点, 返回 True"""
        node = self.root

        for ch in word:
            index = ord(ch) - ord('a')

            if not node.next[index]:
                return False
            
            node = node.next[index]
        
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for ch in prefix:
            index = ord(ch) - ord('a')

            if not node.next[index]:
                return False
            
            node = node.next[index]
        
        return True

