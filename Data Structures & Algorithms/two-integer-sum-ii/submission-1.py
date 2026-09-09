class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        sets = {}

        for index, value in enumerate(numbers):

            if target - value in sets:
                return [sets[target - value]+1, index+1]

            else:
                sets[value] = index