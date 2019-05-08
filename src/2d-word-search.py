class TrieNode:
    def __init__(self):
        self.leaf = False
        self.nxt = None




class Solution:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, root, word):
        cur = root
        for c in word:
            index = ord(c)-ord('a')
            if not cur.nxt:
                cur.nxt = [None]*26
            if not cur.nxt[index]:
                cur.nxt[index] = TrieNode()
            cur = cur.nxt[index]    
        if cur != root:
            cur.leaf = True 
            
            
    def trie_search(self, board, i,j, root, visited, st, lt):
        if not root:
            return
        
        if root.leaf:
            if st not in lt:
                lt.append(st)
 
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]):
            return

        if visited[i][j] :
            return

        index = ord(board[i][j])-ord('a')
        if not root.nxt or not root.nxt[index]:
            return

        root = root.nxt[index]
        st +=board[i][j]
        visited[i][j]=True
        self.trie_search(board, i-1, j, root, visited, st, lt)
        self.trie_search(board, i+1, j, root, visited,st,lt)
        self.trie_search(board, i, j-1, root, visited,st, lt)
        self.trie_search(board, i, j+1, root, visited,st,lt)
 
        visited[i][j] = False

        return                   
    
    
    def search(self, board, word, i, j, r, c):
        print("searching at %d %d" %(i,j))
        index = 0

        if board[i][j] != word[index]:
            return False
        
        st = list()
        visited = list()
        for k in range(r):
            tmp = [False]*c
            visited.append(tmp)
        st.append((i, j, index))
        visited[i][j] = True          
        highindex = index

        while any(st):
             (i,j,index)=st.pop()
             index +=1
             if index > highindex:
                 highindex = index
             if index == len(word):
                 return True
             for k in [-1, 0, 1]:
                 for l in [-1,0,1]:
                     if i+k < r and i+k >= 0 and j+l < c and j+l >= 0:
                         n = i+k
                         m = j+l
                         if (abs(n-i) == abs(m-j)):
                               continue
                         
                         if not visited[n][m] and board[n][m] == word[index]:
                             print("index %d %d matched till %s" %(i+k,j+l, word[:index+1]))
                             st.append((n, m, index))
                             visited[n][m] = True
                         else:
                             visited[n][m] = False   
        
        print("matched till :%s" %(word[:highindex]) )
        return False

    def dfs(self, board, i, j,  word, index, visited ):
        if index ==len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
            return False
        if visited[i][j]:
            return False
        if board[i][j] != word[index]:
            return False
        visited[i][j]= True
        flag = (self.dfs(board, i-1, j, word, index+1, visited) or 
               self.dfs(board, i+1, j, word, index+1, visited) or
               self.dfs(board, i, j+1, word, index+1, visited) or
               self.dfs(board, i, j-1, word, index+1, visited))
        visited[i][j] = False
        return flag            
    
    def dfs_search(self, board, word, i, j, r, c):
        print("searching at %d %d" %(i,j))
        st = list()
        index = 0
        size = len(word)
        visited = list()
        for k in range(r):
            tmp = [0]*c
            visited.append(tmp)
        st.append((i, j, index))
        visited[i][j] = 1            
        lastindex = 0
        while any(st):
            (i,j,index)=st.pop()
            index +=1
            
            if visited[i][j] == 1 and index < len(word) and board[i][j] == word[index]:
                print("index %d %d matched till %s" %(i,j, word[:index+1]))
                visited[i][j] = 2
                index+=1
                if index > lastindex:
                    lastindex = index
                if index == len(word):
                    return True
                
                if i < r-1 and visited[i+1][j] == 0:
                    st.append((i+1, j,index))
                    visited[i+1][j] = 1
                if j < c-1 and visited[i][j+1] == 0:
                    st.append((i, j+1,index))
                    visited[i][j+1] = 1
                if i > 0 and visited[i-1][j] == 0:
                    st.append((i-1, j,index))
                    visited[i-1][j] = 1
                    
                if j > 0 and visited[i][j-1] == 0:
                    st.append((i, j-1,index))
                    visited[i][j-1] = 1
            else:
                visited[i][j] = 0        

        
        print("matched till :%s" %(word[:lastindex]) )
        return False
                    
    def search_singleword(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] :
                    if self.search(board, word, i,j, len(board),len(board[i])):
                       return True
        return False    
    
    def search_singleword_1(self, board, word):
        visited = list()
        for k in range(len(board)):
            tmp = [False]*len(board[k])
            visited.append(tmp)        
        for i in range(len(board)):
            for j in range(len(board[i])):
                    if self.dfs(board, i, j, word, 0, visited):
                        return True
        return False        
    
    def findWords1(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        lt = list()
        for word in words:
            if self.search_singleword_1(board, word):
                lt.append(word)
        tmp = list()            
        for i in range(len(lt)-1, -1,-1):
            if lt[i] not in tmp:
                tmp.append(lt[i])
        return tmp 

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        lt = list()
        for word in words:
            self.insert(self.root, word)
        visited = list() 
        for k in range(len(board)):
            tmp = [False]*len(board[k])
            visited.append(tmp)    
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                st=list()
                self.trie_search(board, i, j, self.root, visited, "", st)
                if any(st):
                    print("found : " ,end="")
                    print(st)                    
                    lt.extend(st)
  
        tmp = list()            
        for i in range(len(lt)-1, -1,-1):
            if lt[i] not in tmp:
                tmp.append(lt[i])
        return tmp     
    
    
    
if __name__=="__main__":
    print("Python program for 2D map search")
    board = [["b","a","a","b","a","b"],
             ["a","b","a","a","a","a"],
             ["a","b","a","a","a","b"],
             ["a","b","a","b","b","a"],
             ["a","a","b","b","a","b"],
             ["a","a","b","b","b","a"],
             ["a","a","b","a","a","b"]]
    words = ["aabbbbabbaababaaaabababbaaba"]
#    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
#    words = ["oath"]    
    
#    board = [["a","b"],["c","d"]]
#    words = ["abcd"]
   
#    board = [["a","a"]]
#    words = ["aaa"]  
 
#    board = [["a","b"],["c","d"]]
#    words = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]    
#    words = ["ab", "cb","ad", "bd","ac"] 
#    board = [["a"]]
#    words =[["a"]]

#    board = [["a","b"],["a","a"]]
#    words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]

    print(board)
    print(words)
    obj =  Solution()
    lt = obj.findWords(board,words)
    print(lt)
    

    
    
    