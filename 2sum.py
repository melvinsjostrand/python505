import random

def sum(lst, sum=10):
    unique_sum = set()
    new_lst = sorted(lst)


    fp,lp = 0, len(new_lst) -1
    print(new_lst)
    print(new_lst[fp], new_lst[lp])
    while fp < lp:
        p = new_lst[fp] + new_lst[lp]
        if p == sum:
            unique_sum.add((new_lst[fp], new_lst[lp]))
            fp += 1
        elif p < sum:
            fp += 1
        else:
            lp -= 1

    return list(unique_sum)



def random_lst():
    lst = []
    for i in range(30):
        r = random.randint(-20,20)
        lst.append(r)

    return lst

lst = random_lst()
print(sum(lst))