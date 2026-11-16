import random

lst = []
size = 100
for _ in range(size):
    lst.append(random.randint(-size,size))

def radix(lst):
    if not lst:
        return lst
    neg = [-x for x in lst if x < 0]
    pos = [x for x in lst if x >= 0]

    def radix_sort_pos(arr):
        if not arr:
            return arr
        max_value = max(arr)
        exp = 1
        while max_value // exp > 0:
            arr = sort_by_dig(arr, exp)
            exp *= 10

        return arr

    def radix_sort_neg(arr):
        if not arr:
            return arr
        max_value = max(arr)
        exp = 1
        while max_value // exp > 0:
            arr = sort_by_dig(arr, exp)
            exp *= 10
        return arr

    def sort_by_dig(arr,exp):
        buckets = [[]  for _ in range(10)]
        for num in arr:
            index = (num // exp) % 10
            buckets[index].append(num)

        new_lst = []
        for bucket in buckets:
            for num in bucket:
                new_lst.append(num)
        return new_lst
    
    sorted_neg = radix_sort_neg(neg)
    sorted_pos = radix_sort_pos(pos)

    return [-x for x in reversed(sorted_neg)] + sorted_pos






print(radix(lst))