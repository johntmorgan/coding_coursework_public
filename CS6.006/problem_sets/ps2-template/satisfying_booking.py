import copy

def merge_bookings(left, right):
    merge = []
    l_it, r_it = 0, 0
    l_len, r_len = len(left), len(right)
    print(left, right)
    while l_it < l_len or r_it < r_len:
        if r_it == r_len or l_it < l_len and left[l_it][1] <= right[r_it][1]:
            curr_book = left[l_it]
            l_it += 1
        else:
            curr_book = right[r_it]
            r_it += 1
        if len(merge) > 0:
            lb_loc = len(merge) - 1
            last_book = copy.deepcopy(merge[lb_loc])
            # Begins at start and partially overlaps
            if curr_book[1] == last_book[1] and curr_book[2] < last_book[2]:
               merge += [[last_book[0], curr_book[2], last_book[2]]]
               merge[lb_loc][0] = merge[lb_loc][0] + curr_book[0]
               merge[lb_loc][2] = curr_book[2]
            # Begins at start and exactly overlaps
            elif curr_book[1] == last_book[1] and curr_book[2] == last_book[2]:
                merge[lb_loc][0] = merge[lb_loc][0] + curr_book[0]
            # Begins at start and extends beyond
            elif curr_book[1] == last_book[1] and curr_book[2] > last_book[2]:
                merge[lb_loc][0] = merge[lb_loc][0] + curr_book[0]
                merge += [[curr_book[0], last_book[2], curr_book[2]]]
            # Begins in middle and partially overlaps
            elif curr_book[1] < last_book[2] and curr_book[2] < last_book[2]:
                merge[lb_loc][2] = curr_book[1]
                merge += [[last_book[0] + curr_book[0], curr_book[1], curr_book[2]]]
                merge += [[last_book[0], curr_book[2], last_book[2]]]
            # Begins in middle and extends to end
            elif curr_book[1] < last_book[2] and curr_book[2] == last_book[2]:
                merge[lb_loc][2] = curr_book[1]
                merge += [[last_book[0] + curr_book[0], curr_book[1], curr_book[2]]]
            # Begins in middle and extends beyond end
            elif curr_book[1] < last_book[2] and curr_book[2] > last_book[2]:
                merge[lb_loc][2] = curr_book[1]
                merge += [[last_book[0] + curr_book[0], curr_book[1], last_book[2]]]
                merge += [[curr_book[0], last_book[2], curr_book[2]]]
            # Completely off the end time-wise
            else:
                merge += [[curr_book[0], curr_book[1], curr_book[2]]]
            print(merge)
        else:
            merge += [[curr_book[0], curr_book[1], curr_book[2]]]
    # Merge neighboring bookings with exact same room count
    for book_idx in range(len(merge) - 2):
        if merge[book_idx][0] == merge[book_idx + 1][0] and \
            merge[book_idx][2] == merge[book_idx + 1][1]:
            merge = merge[:book_idx] + [[merge[book_idx][0], 
                merge[book_idx][1], merge[book_idx + 1][2]]] + \
                merge[book_idx + 2:]
    return merge

def satisfying_booking(R):
    '''
    Input:  R | Tuple of |R| talk request tuples (s, t)
    Output: B | Tuple of room booking triples (k, s, t)
              | that is the booking schedule that satisfies R
    '''
    if len(R) == 1:
        return ((1, R[0][0], R[0][1]),)
    else:
        mid = len(R) // 2
        first_half = R[:mid]
        second_half = R[mid:]
        left = satisfying_booking(first_half)
        right = satisfying_booking(second_half)
        bookings = merge_bookings(left, right)
        return tuple(bookings)

# requests = ((2, 3),(4, 5))
# print(satisfying_booking(requests))

# requests = ((4, 5),(2, 3))
# print(satisfying_booking(requests))

# requests = ((2, 3),(3, 4))
# print(satisfying_booking(requests))

# requests = ((3, 4),(2, 3))
# print(satisfying_booking(requests))

# requests = ((1, 2),(3, 4),(2, 3))
# print(satisfying_booking(requests))

# requests = ((3, 4),(3, 4))
# print(satisfying_booking(requests))

# requests = ((3, 5),(3, 4))
# print(satisfying_booking(requests))

# requests = ((3, 5),(3, 6))
# print(satisfying_booking(requests))

# requests = ((3, 6),(4, 5))
# print(satisfying_booking(requests))

# requests = ((3, 6),(4, 6))
# print(satisfying_booking(requests))

# requests = ((3, 6),(4, 7))
# print(satisfying_booking(requests))

# requests = ((2, 4),(1, 3))
# print(satisfying_booking(requests))

# requests = ((2, 3),(2, 8))
# print(satisfying_booking(requests))

# requests = ((2, 3),(2, 8),(4, 5))
# print(satisfying_booking(requests))

# requests = ((2, 3),(4, 10))
# print(satisfying_booking(requests))

# requests = (2, 3),(4, 10),(2, 8),(6, 9),(0, 1),(1, 12),(13, 14)
# print(satisfying_booking((requests)))

# requests = ((11, 15),(12, 25))
# print(satisfying_booking((requests)))

# requests = ((2, 19), (17, 18), (12, 25), (5, 15), (9, 11))
# print(satisfying_booking((requests)))

# Scales with time, not quite the specification
# def find_max_time(left, right):
#     max_time = 0
#     for request in left + right:
#         if request[2] > max_time:
#             max_time = request[2]
#     return max_time

# def find_min_time(left, right, max_time):
#     min_time = max_time
#     for request in left + right:
#         if request[1] < min_time:
#             min_time = request[1]
#     return min_time

# def merge_bookings(left, right):
#     merge = []
#     max_time = find_max_time(left, right)
#     min_time = find_min_time(left, right, max_time)
#     curr_time = min_time
#     while curr_time < max_time:
#         book_val = 0
#         for booking in left + right:
#             if booking[1] <= curr_time and booking[2] > curr_time:
#                 book_val += booking[0]
#         if book_val > 0:
#             if len(merge) == 0:
#                 merge += [[book_val, curr_time, curr_time + 1]]
#             elif merge[len(merge) - 1][0] == book_val \
#                 and merge[len(merge) - 1][2] == curr_time:
#                 merge[len(merge) - 1][2] += 1
#             else:
#                 merge += [[book_val, curr_time, curr_time + 1]]
#         curr_time += 1
#     return merge