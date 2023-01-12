A = [1,2,3,4,5,6,6,7,6]

def removeElement(A, e):
    n =  len(A)
    j = 0
    for i in range(n):
        if A[i] != e:
            A[j] = A[i]
            j += 1
    print(f"New Array: {A}")
    return i



ans = removeElement(A, 6)
print(ans)     
