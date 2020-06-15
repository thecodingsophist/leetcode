# Given a non-empty number array with duplicates except for one, find that one non-duplicate
# HINT: Should have linear runtime complexity, try for least memory

# TRY 1: NO NEED TO USE QUEUES
# def single_num(list):
#     # add first two elements to list
#     sorted_list = list.sort()
#     queue = [sorted_list[0], sorted_list[1]]
#     if queue[0] != queue[1]:
#         return queue[0]
#     for i, i+1 in sorted_list[2:]:
#         # if not queue:
#         #     queue.append(i)
#         # queue.popleft()
#         # queue.popleft()
#         # queue.append(i)
#         # queue.append(i+1)
#         # if queue
#         if i != i+1:
#             return i

# CODE WITH WHILE LOOP
def single_num(list):
    list.sort()
    if list[0] != list[1]:
        return list[0]
    else:
        i = 2
        while i+1 < len(list):
            if list[i] != list[i+1]:
                return list[i]
            else:
                i += 2
        return list[-1]


if __name__ == "__main__":
    # why above? name is the 'name' designated for what is equal to the name of what comes after 'python' on the command line
    print(single_num([0,1,1]))
    print(single_num([0,0,1,2,2]))
    print(single_num([1,1,2,2,3]))

# THOUGHTS/NOTES

# Brute force solution: sort, then queue and pop pairs
# Worse solution: sort, compare n, n+1, start at n = 0

# SYNTAX/IDEAS

# 'if not' is used to say if empty, is not used
