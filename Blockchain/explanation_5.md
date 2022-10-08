
# Runtime complexity;
#In this problem I used and modified your template.
#There is Block class and Blockchain class. This performs like a linked list. There is add and print functions for blockchain linled list.
#add function appends block to the end. Big O is O(n)
#print_blockchain function prints all elements one by one big O is O(n)
#Big O of this problem is O(n)


# Space complexity is;
# we can add n blocks and each blocks contains 5 attributes(timestamp, data, previous_hash, next)
# so complexity is O(n*5)-->O(n)