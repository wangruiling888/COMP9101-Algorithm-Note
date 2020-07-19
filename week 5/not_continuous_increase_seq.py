'''Given a sequence of n real numbers A[1..n], determine a subsequence
(no need to contiguous) of maximum length in which the values in the subsequence are strictly
increasing.'''

# solution - dynamic program
A = [1,2,3,5,3,4,7,8,9,3,5,7,0,1,23,5,7,2]
max_len = [A[0]]
sequence = [A[0]]
max_length = 1
max_seq = []
max_seq.append([A[0]])
for i in range(1, len(A)):
    max_len_sub = 0
    max_seq_sub = [A[i]]
    for k in range(0, i):
        cur_len = 0
        if (A[i] > A[k]):
            cur_len = max_len[k] + 1
        else:
            cur_len = 1
        if cur_len > max_len_sub:
            max_len_sub = cur_len
            max_seq_sub = max_seq[k] + [A[i]]

    max_len.append(max_len_sub)
    max_seq.append(max_seq_sub)
i = max_len.index(max(max_len))
print("max length is:", max_len)
print("the corresponding sequence is:", max_seq[i])


