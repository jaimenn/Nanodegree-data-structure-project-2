# Runtime complexity;
#I created a Group object that has name, groups, users.
#We can add sub groups and users and names in groups.
#is_user_in_group function check if user in group or in sub groups of this groups.
#This function performs this work by recursively. So big O of this function is O(n^2)



#Space complexity is;
#There may be n groups and n users. 
#This algorithm takes up O(n)+O(n) spaces
#So space complexity is O(n)