# def binary_search(numbers, target):
#     numbers.sort()
#     start = 0
#     end = len(numbers) - 1

#     while start <= end:
#         mid = (start + end) // 2

#         if numbers[mid] == target:
#             return target

#         if target < numbers[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1

#     return False


def find_duplicate(nums):
    if type(nums) != list or len(nums) <= 1:
        return False
    nums.sort()
    for i, n in enumerate(nums[:-1]):
        if type(n) == str or n < 0:
            return False
        if n == nums[i + 1]:
            return n

    return False
