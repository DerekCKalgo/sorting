#A function can have multiple return statements. When any of them is executed, the function terminates.
#Selectin sort-Going thru a list, find the smallest number and place on the 0 index of the list.
#Next, find the second smallest number and place on the first index of the list.
#Continue until the list is sorted from smallest to largest.
#Algorithm works by setting the first for loop to set the index to be compared to.
#Then the second for loop goes thru the whole index to compare each index after to the index set at the first for loop.
#If any number at the ongoing index is smaller than the first index, the min_index will be set that ongoing index until the loop finishes.
#Then a swap happens where the first index is replaced with the number at the min_index.
#And the number at the first index replaces the number at the min_index.
#Then goes back to the first for loop and sets the comparison index to the second index.  Scennario starts again.


def select_sort(list):
    for j in range (len(list)-1):
        min_index=j
        for x in range (j+1, len(list)):
            if list[x]<list[min_index]:
                min_index=x
        temp=list[j]
        list[j]=list[min_index]
        list[min_index]=temp
    return list
             
a=select_sort([9, 3, 6, 4, 2, 1, 10,20, 50, -2, 101, -4])
print(a)
