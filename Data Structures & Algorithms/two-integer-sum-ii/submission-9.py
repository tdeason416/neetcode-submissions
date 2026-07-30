class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     numlen = len(numbers)
    #     p1 = 0
    #     p2 = -1
    #     while True:
    #         r = numbers[p1] + numbers[p2]
    #         if r == target:
    #             return [numbers[p1], numbers[p2]]
    #         elif r > target:
    #             p2 -= 1
    #         elif r < target:
    #             p1 += 1
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []
                

        