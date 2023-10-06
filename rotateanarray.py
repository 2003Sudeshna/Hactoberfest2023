def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # In case k is larger than the array length
    return arr[-k:] + arr[:-k]

# Example usage:
original_array = [1, 2, 3, 4, 5]
positions_to_rotate = 2
rotated_array = rotate_array(original_array, positions_to_rotate)
print(rotated_array)  # Output: [4, 5, 1, 2, 3]
