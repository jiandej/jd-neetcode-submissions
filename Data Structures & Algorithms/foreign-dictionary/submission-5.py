class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        result = ""
        graph = {}
        indegree = {}

        for word in words:
            for c in word:
                if (c not in graph):
                    graph[c] = set()
                    indegree[c] = 0

        # build graph
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            if (len(word1) > len(word2) and word1[:len(word2)] == word2):
                return ""
            char1, char2 = self.findDifference(word1, word2)
            if (char1 == None):
                continue
            if (char2 not in graph[char1]):
                graph[char1].add(char2)
                indegree[char2]+=1
        
        # sort
        queue = collections.deque()
        for key in indegree.keys():
            if (indegree[key] == 0):
                queue.append(key)
        
        while (len(queue) != 0):
            char = queue.popleft()
            result += char
            for next_char in graph[char]:
                indegree[next_char] -= 1
                if (indegree[next_char] == 0):
                    queue.append(next_char)
        
        return result if len(result) == len(graph) else ""

    
    def findDifference(self, word1: str, word2: str) -> tuple[str, str]:
        idx1, idx2 = 0, 0

        while (idx1 < len(word1) and idx2 < len(word2)):
            if (word1[idx1] == word2[idx2]):
                idx1 += 1
                idx2 += 1
            else:
                break
        
        if (idx1 == len(word1) or idx2 == len(word2)):
            return (None, None)
        
        return (word1[idx1],  word2[idx2])