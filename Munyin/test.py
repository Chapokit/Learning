nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

a = m - 1
b = n - 1
write_index = m + n - 1

# Merge nums1 and nums2 from the back to avoid overwriting
while a >= 0 and b >= 0:
    if nums1[a] > nums2[b]:
        nums1[write_index] = nums1[a]
        a -= 1
    else:
        nums1[write_index] = nums2[b]
        b -= 1
    write_index -= 1

# If there are remaining elements in nums2, copy them
while b >= 0:
    nums1[write_index] = nums2[b]
    b -= 1
    write_index -= 1

print(nums1)
