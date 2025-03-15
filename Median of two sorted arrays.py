def find_median_sorted_arrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    mid = len(merged) // 2
    return (merged[mid] + merged[~mid]) / 2

# Example usage
nums1 = [1, 3]
nums2 = [2]
print(find_median_sorted_arrays(nums1, nums2))
