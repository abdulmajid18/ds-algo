A = [1,2,2,3]

def remove_duplicate(A):
    length = len(A)
    if length < 2:
        return length
    i, j = 0, 1
    while j < length:
        if A[j] != A[i]:
            i += 1 
            A[i] = A[j]
        j += 1
    print(A)
    return j + 1

ans = remove_duplicate(A)
print(ans)


A = [2, 3, 5, 5, 7, 11, 11, 11, 13]


def removeDuplicateBruteForce(A):
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                A[j] = A[-1]
    print(A)
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                A = A[:j]
                print(A)
                return A
removeDuplicateBruteForce(A)

def removeDuplicateHash(A):
    unique = []
    helper = set()
    for i in A:
        if i not in helper:
            unique.append(i)
            helper.add(i)
    return unique, helper

#  [1,1,2]
def removeDuplicateSort(A):
    A.sort()
    j = 0
    for i in range(1, len(A)):
        if (A[j] != A[i]):
            j += 1
            A[j] = A[i]
    print(A[:j+1])


def removeDuplicateHashB(A):
    unique = []
    table = {}
    for i in A:
        if i in table:
            pass
        elif i != "":
            table[i] = 1
            unique.append(i)
        else:
            table[i] = 0

    print(unique)
# removeDuplicateHashB(A)


def deleteDuplicate(A):
    if not A:
        return 0
    write_index = 0
    for i in range(1, len(A)):
        if A[write_index] != A[i]:
            # A[write_index] = A[i]
            write_index += 1
    return write_index


# x = deleteDuplicate(A)
# print(x)
# x, y = removeDuplicateHash(A)

# N = int(input())
# arr = input().split()

# arr = [int(i) for i in arr]
# arr.sort()

# highestCount = 0
# highestItem = 0

# for item in arr:
#     if arr.count(item) >= highestCount:
#         highestItem = item
#         highestCount = arr.count(item)
# print(highestItem)
# print(highestCount)