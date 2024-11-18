
class Solution:
    def peakElement(self, arr):
        # Set the left and right pointers
        left = 0
        right = len(arr) - 1

        # Apply binary search to find the peak element
        while left < right:
            mid = left + (right - left) // 2

            # If middle element is greater than the next, move the right pointer
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                # Otherwise, move the left pointer
                left = mid + 1
        
        # Return the index of the peak element
        return left

    






#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        arr = list(map(int, input().split()))
        # Create a Solution object and calculate the result

        index = Solution().peakElement(arr)
        n = len(arr)
        flag = False
        if index < 0 or index >= n:
            flag = False
        else:
            if index == 0 and n == 1:
                flag = True
            elif index == 0 and arr[index] >= arr[index + 1]:
                flag = True
            elif index == n - 1 and arr[index] >= arr[index - 1]:
                flag = True
            elif arr[index - 1] <= arr[index] and arr[index] >= arr[index + 1]:
                flag = True
            else:
                flag = False

        if flag:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends