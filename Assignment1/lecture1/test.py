def print_lst(lst, n=0):
    if n < len(lst):
        print(lst[n])
        print_lst(lst,n + 1)

def print_lst_back(lst, n=0):
    if n < len(lst):
        print_lst_back(lst, n + 1)
        print(lst[n])


lst = [5 ,2 ,1 ,2, 3, 4, 7,34,21]
print(print_lst(lst))
print(print_lst_back(lst))
