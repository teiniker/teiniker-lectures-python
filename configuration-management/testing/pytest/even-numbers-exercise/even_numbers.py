def even_numbers(nums):
    if nums is None:
        raise ValueError("Input list cannot be None")

    result = []
    for n in nums:
        if n % 2 == 0:
            # Bug: result = n
            result.append(n)
    return result
