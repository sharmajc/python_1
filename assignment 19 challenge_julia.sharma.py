#Challenge: Implement the sorting algorithm without using any built-in sorting functions.
#Description: Develop a function called sort_list that takes a list of numbers as input and returns a new list containing the same elements sorted in ascending order.
...

def sort_list(list1):
    #copies sort_list to modify
    ascending = list1.copy()
    n = len(ascending)

    #loop through list multiple times
    for i in range(n-1):
        #compare each pair of numbers
        for j in range(n-i-1):
            #if numbers on left is bigger, swap them
            if ascending[j] > ascending[j+1]:
                ascending[j], ascending[j+1] = ascending[j+1], ascending[j]
    return ascending

lista = [5,3,7,1,9]
result = sort_list(lista)

print("List in ascending order: ", result)




