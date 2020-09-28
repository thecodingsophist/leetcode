'''
    Given an array of nums, return all triplets (nonduplicate) that add up to 0
'''

'''
    HINT: choose one number, and then search using two sum
'''

def two_sum(A, k):
    list = []
    for i in A:
        for j in A[i:]:
            if i + j == k:
                list.append([i, j])
    return list

def three_sum(A):
    list = []
    i = 0
    while i < len(A):
        if i == 0:
            B = A[1:]
        else:
            B = A[:i]
            B.extend(A[i+1:])
            # print("B: " + str(B))
        answers = two_sum(B, -i)
        # print("answers: " + str(answers))
        if answers:
            for j in answers:
                j.append(i)
                print("j: " + str(j))
                list.append(j)
        i += 1
    return list

if __name__ == "__main__":
    print(two_sum([1,2,3], 5))
    print(three_sum([-2,-1,0,1,2]))
