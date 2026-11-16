import random
import time
def threesum_pointer(lst, sum):
    unique_sum = set()
    new_lst = sorted(lst)
    before = time.time()
    for i in range(len(new_lst)-2):
        n1 = new_lst[i]
        fp = i+1
        lp = len(new_lst) -1
        while fp < lp:
            p = new_lst[fp] + new_lst[lp] + n1
            if p == sum:
                unique_sum.add((n1, new_lst[fp], new_lst[lp]))
                fp += 1
            elif p < sum:
                fp += 1
            else:
                lp -= 1

    measured_time = time.time() - before
    return list(unique_sum), measured_time

def threesum_brute(lst,sum):
    unique_sum = set()
    lst = sorted(lst)
    before = time.time()
    for i in range(len(lst)-2):
        n1 = lst[i]
        for j in range(i+1,len(lst)-1):
            n2 = lst[j]
            for x in range(j+1,len(lst)):
                n3 = lst[x]
                if n1 + n2 + n3 == sum:
                    p = tuple(sorted((n1,n2,n3)))
                    unique_sum.add(p)
    measured_time = time.time() - before
    return list(unique_sum), measured_time


def threesum_cache(lst,sum):
    unique_sum = set()
    lst = sorted(lst)
    before = time.time()
    for i in range(len(lst)-2):
        n1 = lst[i]
        cache = set()
        for j in range(i+1, len(lst)):
            n2 = lst[j]
            n3 = sum - (n1 + n2) 
            if n3 in cache:
                if n3 < n2:
                    n2,n3 = n3,n2
                unique_sum.add((n1,n2,n3))
            else:
                cache.add(n2)
                
    measured_time = time.time() - before
    return list(unique_sum), measured_time



def random_func(size):
    lst = []
    for i in range(size):
        r = random.randint(-20,20)
        lst.append(r)
    sum = random.randint(0,10)
    return lst,sum

def plot(size,results):
    print(size)
    print(results)
    for name, label in [("brute", "Brute force"), ("pointer", "Two pointer", ("cache", "Cache set"))]

def main():
    repeat = 5
    size = [50, 100, 150, 200, 250, 300]
    for i in range(repeat):
        lst,sum = random_func(size[i])

        #print(sum)

        pointer,time_point = threesum_pointer(lst,sum)
        brute,time_brute = threesum_brute(lst,sum)
        cache ,time_cache= threesum_cache(lst,sum)
       # print(sorted(brute))
        #print(time_point)
        #print(sorted(pointer))
        #print(time_brute)
        #print(sorted(cache))
        #print(time_cache)
        results = time_brute,time_point,time_cache
        plot(size[i], results)


main()
