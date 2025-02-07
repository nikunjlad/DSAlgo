"""
Given an array of integers, find the second largest element in the array.

"""

# BRUTE FORCE:
# Time Complexity: O(Nlog(N) + N). Sorting takes O(Nlog(N)) time and traversing backwards can take worst case O(N) time.
# Space Complexity: O(3). Since sorting takes about O(1) and other 2 taken by place holder variables
# def secondLargestElement(arr: list, n: int) -> int:

#     # initialize secondLargest element
#     secondLargest = -1

#     # sort array in ascending order
#     arr.sort()

#     # get the largest element
#     largestElement = arr[n-1]

#     # traverse backwards and find second largest element
#     for i in range(n-1,-1,-1):
#         if arr[i] < largestElement:
#             secondLargest = arr[i]
#             break

#     return secondLargest

# BETTER SOLUTION:
# Time Complexity: O(2N) , since we are looping through the array twice
# Space Complexity:
# def secondLargestElement(arr: list, n: int) -> int:

#     # define largest element
#     largestElement = arr[0]

#     for i in range(1, n):
#         if arr[i] > largestElement:
#             largestElement = arr[i]

#     # define secondLargest Element
#     secondLargest = -1

#     for i in range(n):
#         if arr[i] > secondLargest and arr[i] != largestElement:
#             secondLargest = arr[i]

#     return secondLargest

# OPTIMAL:
# Time Complexity: O(2N) , since we are looping through the array twice
# Space Complexity:
def secondLargestElement(arr: list, n: int) -> int:

    secondLargest = -1
    largestElement = arr[0]

    for i in range(1, n):
        if arr[i] > largestElement:
            secondLargest = largestElement
            largestElement = arr[i]
        elif arr[i] < largestElement and arr[i] > secondLargest:
            secondLargest = arr[i]

    return secondLargest


if __name__ == "__main__":
    a = [12,35,1,10,34,1]
    b = [10,5,10]
    c = [10,10,10]
    print(secondLargestElement(c, len(c)))
