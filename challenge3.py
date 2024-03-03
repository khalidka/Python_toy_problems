# Write a function solution that, given an integer N, returns a string of length N containing as many different lower-case letters ('a'-'z') as possible, in which each letter occurs an equal number of times.

def solution(N):
    # Determine the number of times to repeat the sequence
    num_repeats = (N + 25) // 26      # 26 represent the letters in the alphabet

    # Generate the repeated sequence of lowercase letters
    repeated_letters = ''.join(chr(ord('a') + i % 26) for i in range(num_repeats * 26))

    # Trim the sequence to the desired length N
    result = repeated_letters[:N]