"""
Given an array of integers, find the largest element in the array.

"""

# BRUTE FORCE:
# Time Complexity: O(nlog(n)) - since sorting takes at best O(nlog(n)) time
# Space Complexity: O(1)
def largestElement(arr: list, arr_len: list) -> int:

    # sort an array from ascending to descending order
    arr.sort()
    return arr[arr_len - 1]


# OPTIMAL SOLUTION:
# Time Complexity: O(n) - since we are only looping over the array once
# Space Complexity: O(1) - since that's the space consumed by the variables
# def largestElement(arr: list, arr_len: int) -> int:

#     largest = arr[0]
#     for index in range(arr_len):
#         if arr[index] > largest:
#             largest = arr[index]

#     return largest


if __name__ == "__main__":
    a = [1, 8, 7, 56, 90]
    b = [5, 5, 5, 5]
    c = [10]
    print(largestElement(a, len(a)))