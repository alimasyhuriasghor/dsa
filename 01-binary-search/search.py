def simple_search(nums: list, target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

def binary_search(nums: list, target: int) -> int:
    # At the begining, this is the entire array
    low = 0
    high = len(nums) - 1

    # Loop over the list from the first index until it reaches the highest index
    while low <= high:
        # Each time, check the middle element:
        mid = (low + high) // 2
        guess = nums[mid]

        # If the guess is found, which is the middle number, then return it:
        if guess == target:
            return mid
        
        # If the guess is too low, we update the low accordingly:
        elif guess < target:
            low = mid + 1

        # If the guess is too high, we update high
        else:
            high = mid - 1

    # Return -1 to indicate the value wasn't found in the list
    return -1