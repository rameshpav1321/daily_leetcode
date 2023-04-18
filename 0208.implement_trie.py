class TrieNode:
    def __init__(self,char):
        self.char=char
        self.is_end=False
        self.children={}

class Trie:
    def __init__(self):
        self.root=TrieNode('')
        
    def insert(self, word: str) -> None:
        crawl_node=self.root
        for char in word:
            if char in crawl_node.children:
                crawl_node=crawl_node.children[char]
            else:
                new_node=TrieNode(char)
                crawl_node.children[char]=new_node
                crawl_node=new_node
        crawl_node.is_end=True
        
    def search(self, word: str) -> bool:
        crawl_node=self.root
        for char in word:
            if char in crawl_node.children:
                crawl_node=crawl_node.children[char]
            else:
                return False
        return crawl_node.is_end
        
    def startsWith(self, prefix: str) -> bool:
        crawl_node=self.root
        for char in prefix:
            if char in crawl_node.children:
                print(char)
                crawl_node=crawl_node.children[char]
            else:
                return False
        return True
        