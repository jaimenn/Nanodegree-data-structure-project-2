
# Runtime complexity is;
# I created find_files function which takes suffix and path as argument. In this function I used a helper function. which performs the real part of work.
# This helper function takes path and controls it if there is file which ends with given suffix. if there is a folder in, helper function controls each folder recursively. Big O is O(n^2)
# if function finds the right file it adds path name in file_list set. Then converts to list and sorts. Big O of sorted() is nlog(n)
# Big o is n^2 + nlog(n) = O(n^2)


# Space complexity is;
# O(n^n) because n files may contain n directories,files and they can contain n directories,files