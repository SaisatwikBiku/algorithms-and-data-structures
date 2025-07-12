class Solution(object):
    def plusOne(self, digits):
        int_result = int(''.join(map(str, digits)))
        num_result = int_result + 1
        num_list = list(map(int, str(num_result)))

        return num_list
        