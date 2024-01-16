def tri_bulle(seq):
    if len(seq) == 0 :
        return seq
    else :
        n = len(seq)
        for j in range(n-1,0,-1):
            for i in range(j):
                if seq[i] > seq[i+1]:
                    a = seq[i]
                    b = seq[i+1]
                    seq = seq[:i]+seq[i+1]+seq[i]+seq[i+2:]
        return seq

print(tri_bulle('emeline'))