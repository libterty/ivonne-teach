from collections import deque

class Solution(object):
    def __init__(self):
      self.move = [1, 10, 100, 1000]
      self.start = int("0000")
      self.step = 0

    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        # create a collection to store
        deads = set(int(x) for x in deadends)
        goal = int(target)
        # if current move in deads means lock is locked
        if self.start in deads: return -1
        # if current move eq target finished
        if self.start == goal: return 0
        q = deque([(self.start, 0)])
        # Start at the first point of the lock
        visited = set([self.start])
        while q:
            # start from left
            node, self.step = q.popleft()
            for i in range(0, 4):
                round = (node // self.move[i]) % 10
                for j in [-1, 1]:
                    next = node + ((round + j + 10) % 10 - round) * self.move[i]
                    if next == goal:
                        return self.step + 1
                    if next in deads or next in visited: 
                        continue
                    q.append((next, self.step + 1))
                    visited.add(next)
        return -1

print(Solution().openLock(['1212', '2002', '0102', '0101', '0201'], "0202"))
print(Solution().openLock(["8888"], "0009"))
print(Solution().openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))
print(Solution().openLock(["0000"], "8888"))
print(Solution().openLock(["0201","0101","0102","1212","2002"], "0000"))