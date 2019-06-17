import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import scipy.io as sio
import cv2
import random
import glob
import pyedflib


class Solution:
    def maxSubArray(self, nums):
        begin_idx = 0
        max_value = nums[0]
        while (begin_idx < (len(nums) - 1)):
            max_part_val = nums[begin_idx]
            part_sum = 0
            for count, value in enumerate(nums[begin_idx:]):
                part_sum += value
                if part_sum > max_part_val:
                    max_part_val = part_sum
            if max_part_val > max_value:
                max_value = max_part_val
            if nums[-1] > max_value:
                max_value = nums[-1]
            begin_idx += 1

        return max_value



if __name__ == '__main__':
    res0 = Solution()
    result = res0.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])

    print(result)
























