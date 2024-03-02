# There are N boxes (numbered from 0 to N−1) arranged in a row. The K-th box contains A[K] bricks. In one move you can take one brick from some box and move it to a box next to it (on the left or on the right). What is the minimum number of moves needed to end up with exactly 10 bricks in every box?


# Write a function:

# function solution(A);

# that, given an array A of N integers, returns the minimum number of moves needed to end up with exactly 10 bricks in every box. If this is not possible, the function should return −1.

def solution(A):
    target_bricks = 10
    moves_required = 0

    # Iterate through each box except the last one
    for i in range(len(A) -1):
        # Calculate the difference between bricks in the current box and the target
        difference = A[i] - target_bricks

        