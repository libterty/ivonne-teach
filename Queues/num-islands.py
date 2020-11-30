# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # no element
        if not grid: return 0

        m = len(grid)
        n = len(grid[0])
        sum = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == "0":
                    # means here is water
                    continue
                else:
                    sum += 1
                    queue = list()
                    queue.append([i,j])

                    while len(queue) != 0:
                        [p, q] = queue.pop()

                        # check the direction around for up
                        if p >= 1 and grid[p - 1][q] == "1":
                            queue.append([p - 1,q])

                        # check the direction around for down
                        if p < m - 1 and grid[p + 1][q] == "1":
                            queue.append([p + 1,q])

                        # check the direction around for left
                        if q >= 1 and grid[p][q - 1] == "1":
                            queue.append([p, q - 1])

                        # check the direction around for right
                        if q < n - 1 and grid[p][q + 1] == "1":
                            queue.append([p, q + 1])
                        
                        # mark as water
                        grid[p][q] = "0"

        return sum

