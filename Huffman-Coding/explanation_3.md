#Runtime complexity;
# I created a node class
# make_frequency_dict(text) function cretes a dictionary which holds the frequencies of characters in the given text
# make_heap_node(freq_dict) function creates nodes from dict and appens them to the min heap
# merge_nodes() function builds tree with nodes. takes n elements from dict and uses heappop() funk. n times. So Big O is --> nlog(n)
# encode_helper function traverses recursively and assigns a unic code for each character --> O(n)
# huffman_decoding function iterates the encodes data and looks if code is exists in codes dict. I used two for loops so big O is --> n^2
# shortly encoding is n + nlog(n) = O(nlogn), decoding is O(n^2)


# Space complexity is;
# Build tree is O(n)
# encode text from tree is O(n)
# decode encoded text from edcoded data is O(n)
# space complexity is O(n)