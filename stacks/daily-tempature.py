# input [73, 74, 75, 71, 69, 72, 76, 73]
# output [1, 1, 4, 2, 1, 1, 0, 0]
# hint find the next greater elements

# input [55,38,53,81,61,93,97,32,43,78]
# output [3,1,1,2,1,1,0,1,1,0]

class Solution(object):
    # not enougth time
    # def dailyTemperatures(self, T):
    #     """
    #     :type T: List[int]
    #     :rtype: List[int]
    #     """
    #     if len(T) == 0: 
    #         return []
    #     result = []
    #     while len(T) != 0:
    #         cur_temp = T.pop(0)
            
    #         if len(T) == 0:
    #             result.append(0)

    #         for index, temp in enumerate(T, start=0):
    #             if temp > cur_temp:
    #                 result.append(index + 1)
    #                 break
    #             elif (temp <= cur_temp and index + 1 == len(T)):
    #                 result.append(0)
    #     return result
    
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        result = [0] * len(T)
        stack = []

        for index in range(len(T) - 1, -1, -1):
            while stack and T[stack[-1]] <= T[index]:
                stack.pop()
            if stack:
                result[index] = stack[-1] - index
            else:
                result[index] = 0
            stack.append(index)
        return result

print(Solution().dailyTemperatures([55,38,53,81,61,93,97,32,43,78]))