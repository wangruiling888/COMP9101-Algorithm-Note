'''Given a sequence of n real numbers A[1..n], determine a subsequence
(must contiguous) of maximum length in which the values in the subsequence are strictly
increasing.'''

# solution - dynamic program
A = [1,2,3,5,3,4,7,8,9,3,5,7,0,1,23,5,7,9]
sequence = [A[1]]
length = 1
max_length = 0
max_sequence = []

for i in range(2, len(A)):
    if (A[i] > A[i-1]):
        sequence.append(A[i])
        length += 1
    else:
        sequence = [A[i]]
        length = 1
    max_sequence = sequence if length > max_length else max_sequence
    max_length = length if length > max_length else max_length

print("max length is:", max_length)
print("max increasing sequence is:", max_sequence)
