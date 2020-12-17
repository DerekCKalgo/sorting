#A function can have multiple return statements. When any of them is executed, the function terminates.
#Bubble sort works by comparing number at index 0 to index 1. If number at index 0 is larger, then the larger number
#is swapped to index 1. And the smaller number is swapped to index 0.
#Next, the numbers at index 1 is compared to index 2. It contines again at index 2 to index 3.
#When the whole list is gone thru, the largest number will be placed at the end.
#The bubble sort starts again from beginning. At this second sort, the second largest number
#will be placed next to the largest number. This continues until the list is sorted resulting in smallest to largest number.
#My algorithm works by setting a while loop first. Inside the while loop, the for loop will go thru the list.
#If index x is larger than index x+1, the number is swapped and the count is added by one.
#The for loop repeats until the list is sorted. At this point, the count becomes zero.
#Count becoming zero means there is no more swapping at the index. This means the list is sorted.
#At this point, since count is no longer larger than 0, the while terminates. The list is returned after function call.


def bubble_sort(list):
    temp=list[0]
    count=1
    count2=0
    while count>0:
        count=0
        for x in range (len(list)-1):
            if list[x]>list[x+1]:
                temp=list[x+1]
                list[x+1]=list[x]
                list[x]=temp
                count += 1
                count2 += 1
    print(count2)
    return list

a=bubble_sort([4, 5, 2, 3, 1, -2, 5, 6, 0, -200, 2, 488, 900, -900, 222])
print(a)
