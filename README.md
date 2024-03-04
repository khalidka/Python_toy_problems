<ins>Phase-3 Toy-Problems</ins>

## Challenge 1

## Overview
-Problem Statement:
Given an array A of N integers representing the number of bricks in each box, determine the minimum number of moves needed to ensure that every box contains exactly 10 bricks. In one move, you can take one brick from a box and move it to a box next to it (on the left or right). If it's impossible to achieve the goal, return -1.

## Functionality:
-Iterate through each box in the array.
-For each box, determine the number of bricks required to reach 10 bricks.
-Adjust the neighboring box(es) accordingly to equalize the bricks.
-Track the number of moves required to equalize the bricks.
-If it's impossible to equalize the bricks in every box, it returns -1.

[x]Examples:

print(solution([7, 15, 10, 8]))   # return: 7
print(solution([11, 10, 8, 12, 8, 10, 11]))   # return: 6
print(solution([7, 14, 10]))   # return: -1

## Explanation:
 -For the first example, it takes 7 moves to equalize the boxes:
    -Move 3 bricks from box 1 to box 0.
    -Move 2 bricks from box 1 to box 2.
    -Move 2 bricks from box 2 to box 3.
 -For the second example, it takes 6 moves to equalize the boxes.
 -For the third example, it's impossible to equalize the boxes to have exactly 10 bricks in each box.

[x]The function efficiently determines the minimum number of moves needed to equalize the number of bricks in each box.


## Challenge 2

## Overview
-Given an array A of N integers, determine the maximum sum of two numbers whose digits add up to an equal sum. If there are no two numbers whose digits have an equal sum, it returns -1.

## Functionality:
-Set the max sum to -1.
-Iterate through each pair of numbers in the list.
-For each pair of numbers, calculate the sum of the digits for both numbers.
-If the sum of digits is equal for both numbers, update the max sum if the current sum is greater.
-Return the max sum found.

[x] Examples:
-print(solution([51, 71, 17, 42]))   # return: 93
-print(solution([42, 33, 60]))   # return: 102
-print(solution([51, 32, 43]))   # return: -1

## Explanation:
-For the first example, the pair of numbers with digits summing up to an equal sum is (51, 42), resulting in a maximum sum of 93.
-For the second example, the pair of numbers with digits summing up to an equal sum is (42, 60), resulting in a maximum sum of 102.
-For the third example, no two numbers have digits with an equal sum, so the function returns -1.

[x] This function efficiently determines the maximum sum of two numbers with equal digit sums in the given array.

## Challenge 3

## Overview
-The function, solution(N), generates a string of length N containing repeated lowercase letters from 'a' to 'z'. It ensures that each letter occurs an equal number of times and that the resulting string has exactly N characters.

## Functionality:
-Determine the number of times to repeat the sequence of lowercase letters to cover the desired length N.
-Generate a repeated sequence of lowercase letters using modular arithmetic.
-Trim the sequence to the desired length N.
-Return the resulting string.

[x] Example
print(solution(10))   # result: 'abcdefghij'

## Explanation:
For N = 10, the function generates a string containing all lowercase letters from 'a' to 'z' with equal distribution, resulting in 'abcdefghij'.

[x] This function efficiently generates strings with equal distribution of lowercase letters.

[x] License

> This project is licensed under the MIT License - see the LICENSE file for details.

**By: `KHALID SHEIKH ABDIRAHMAN MURSAL`**