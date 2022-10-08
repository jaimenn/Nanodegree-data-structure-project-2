# Runtime complexity is;
#In this solution I used created two diffrent functions as union and intersection.
#union functions takes two linked lists and iterates over all nodes and add values to union_set.
#I used set for avoiding replicates. 
#Then I convertes set to a list and sorted with sorted() func. sorted() funcs big O is O(n^2)
#After this I iterate all list and add all list to a new linked list as union_list big O is O(n^2)
#Total big O is O(nlogn) + O(n^2) = O(n^2)
#In intersection func is same as before. I take two linked list and iterate all nodes of linked lists nodes and add values to set1 and set2 respectively. O(n)
and find intersection set of sets as inter_set.
O(n).
#convert inter_set to list and sort with sorted()
#O(nlogn).
#iterate the list and append all elements to a linked list. O(n^2)
#Big O = O(n) + O(nlogn) + O(n^2) = O(n^2)



#Space complexity is;
#There are two linked lists and each of this lists can take up n elements.
#I used union and intersection sets which can hold n elements. But there is no recursive function and nested loops.
#So space complecity is O(n)