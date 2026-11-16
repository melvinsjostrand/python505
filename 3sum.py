import random
import time
import matplotlib.pyplot as plt
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

def threesum_brute(lst,sum=0):
    unique_sum = set()
    lst = sorted(lst)
    for i in range(len(lst)-2):
        n1 = lst[i]
        for j in range(i+1,len(lst)-1):
            n2 = lst[j]
            for x in range(j+1,len(lst)):
                n3 = lst[x]
                if n1 + n2 + n3 == sum:
                    p = tuple(sorted((n1,n2,n3)))
                    unique_sum.add(p)
    return list(unique_sum)


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



def random_func(size, width):
    lst = []
    n=size*width
    for i in range(size):
        r = random.randint(-10*n,10*n)
        lst.append(r)
    return lst

def graph(lst):
    print(lst)
    for j in range(3):
        x = []
        y = []
        for run,size,time in lst:
            if run == j:
                x.append(size)
                y.append(time)

        plt.plot(x,y,marker="*", linestyle="None",label=f'Körning{j+1}')
    plt.xlabel("Listans storlek")
    plt.ylabel("Exekveringstid (sekunder)")
    plt.title("Brute Force 3-sum")
    plt.legend()
    plt.grid()
    plt.show()
def main():
    count = 0
    result = []
    for j in range(3):
        count = 0
        for i in range(100,850,50):
            count += 1
            lst = random_func(i,10)
            before = time.time()
        #print(sum)

       # pointer,time_point = threesum_pointer(lst,sum)
            brute = threesum_brute(lst)
            mes_time = time.time() - before
       # cache ,time_cache= threesum_cache(lst,sum)
       # print(sorted(brute))
        #print(time_point)
        #print(sorted(pointer))
        #print(time_brute)
        #print(sorted(cache))
        #print(time_cache)
            
            results = mes_time
            result.append((j,i,round(results,2)))
    graph(result)

main()
