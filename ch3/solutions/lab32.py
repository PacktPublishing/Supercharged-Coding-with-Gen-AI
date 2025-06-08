def get_geometric_mean(*nums):
    if not nums:
        raise ValueError("At least one number is required")
    for num in nums:
        if not isinstance(num, (int, float)):
            raise TypeError("All numbers must be integers or floats")
    product = 1
    for num in nums:
        product *= num
    return pow(product, 1 / len(nums))
