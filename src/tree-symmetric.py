# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    
    def check_palindrome(self, lt):
        i = 0
        n = len(lt)-1
        if n == 0:
            return True
        while i < n:
            if lt[i].val != lt[n].val:
                return False
            i +=1
            n -=1
        return True    
    
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        qu = list()
        tmp = list()
        tmp.append(root)
        qu.append(tmp)
        index = 0
        while index < len(qu):
            if self.check_palindrome(qu[index]):
                tmp = list()
                for node in qu[index]:
                    if node.left:
                        tmp.append(node.left)
                    if node.right:
                        tmp.append(node.right)
                if any(tmp):        
                   qu.append(tmp)
            else:
                return False
            index+=1
        return True

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line);
            
            ret = Solution().isSymmetric(root)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()