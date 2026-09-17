class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        numbers = sorted(numbers)
        p = [0,0]
        while (p1 < p2 and p2 < len(numbers)):
            if  (numbers[p1] + numbers[p2]) < target:
                p1 = p1 + 1
            elif (numbers[p1] + numbers[p2]) > target:
                p2 = p2 - 1
            else:
                p[0] = p1+1
                p[1] = p2+1
                return p
            