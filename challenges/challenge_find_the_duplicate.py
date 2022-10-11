def find_duplicate(nums):
    """Faça o código aqui."""
    if type(nums) != list or len(nums) <= 1 or nums == str:
        return False
    for num in nums:
        if type(num) == str or num < 0:
            return False
        if nums.count(num) > 1:
            return num
    return False
