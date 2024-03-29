# Write a function:

# function solution(A);

# that, given an array A consisting of N integers, returns the maximum sum of two numbers whose digits add up to an equal sum. If there are no two numbers whose digits have an equal sum, the function should return -1.

def solution(A):
     # Initialize the maximum sum to -1
    max_sum = -1  


   # Iterate through each pair of numbers in the list
    for first_num in A:
        for second_num in A[A.index(first_num) + 1:]:
            # Calculate the sum of digits for both numbers
            first_num_digit_sum = sum(int(digit) for digit in str(first_num))
            second_num_digit_sum = sum(int(digit) for digit in str(second_num))

            # If the sum of digits is equal for both numbers, update the maximum sum
            if first_num_digit_sum == second_num_digit_sum:
                max_sum = max(max_sum, first_num + second_num)
    # Return the maximum sum found
    return max_sum  
    

# Test purpose
print(solution([51, 71, 17, 42])) #should return 93
print(solution([42, 33, 60])) #should return 102
print(solution([51, 32, 43])) #should return -1