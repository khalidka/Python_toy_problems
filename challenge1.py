# There are N boxes (numbered from 0 to N−1) arranged in a row. The K-th box contains A[K] bricks. In one move you can take one brick from some box and move it to a box next to it (on the left or on the right). What is the minimum number of moves needed to end up with exactly 10 bricks in every box?


# Write a function:

# function solution(A);

# that, given an array A of N integers, returns the minimum number of moves needed to end up with exactly 10 bricks in every box. If this is not possible, the function should return −1.

def solution(A):
    steps = 0
    for box in A:
        index = A.index(box)
        if index == len(A) - 1:
            # Return -1 if it's the last box and the bricks cannot be adjusted
            return -1  

        next_index = index + 1
        next_box = A[next_index]

        # check If the current box has more than 10 bricks
        if box > 10:
            #  Get the difference
            difference = box - 10
            A[index] = 10
            #  Add the difference to the next element
            A[next_index] = next_box + difference
            steps += difference
        # check If the current box has fewer than 10 bricks
        elif box < 10:
            difference = 10 - box
            A[index] = 10
            A[next_index] = next_box - difference
            steps += difference
        # If the current box has exactly 10 bricks, no adjustments needed

    return steps

# Test purpose
print(solution([7, 15, 10, 8])) 
print(solution([11, 10, 8, 12, 8, 10, 11])) 
print(solution([7, 14, 10])) 