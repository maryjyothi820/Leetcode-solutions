127.word ladder
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = [(beginWord, 1)]
        
        while queue:
            word, length = queue.pop(0)
            
            if word == endWord:
                return length
            
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + c + word[i+1:]
                    
                    if newWord in wordSet:
                        queue.append((newWord, length + 1))
                        wordSet.remove(newWord)
        
        return 0
126.word ladder 2
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        from collections import defaultdict
        
        parents = defaultdict(list)
        level = {beginWord}
        found = False
        
        while level and not found:
            next_level = set()
            wordSet -= level
            
            for word in level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        
                        if newWord in wordSet:
                            next_level.add(newWord)
                            parents[newWord].append(word)
                            
                            if newWord == endWord:
                                found = True
            
            level = next_level
        
        res = []
        
        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            
            for p in parents[word]:
                dfs(p, path + [p])
        
        if found:
            dfs(endWord, [endWord])
        
        return res