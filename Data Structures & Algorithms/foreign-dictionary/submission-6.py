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
            idx = self.findDifference(word1, word2)
            if (idx == len(word1) or idx == len(word2)):
                continue
            char1, char2 = word1[idx], word2[idx]
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

    
    def findDifference(self, word1: str, word2: str) -> int:
        idx = 0

        while (idx < len(word1) and idx < len(word2)):
            if (word1[idx] == word2[idx]):
                idx+=1
            else:
                break
        return idx