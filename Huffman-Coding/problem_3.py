import sys
import heapq
import collections
import operator


class Node:

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.right = None
        self.left = None

    def __lt__(self, other):
        return other.freq > self.freq


# make frequency dictionaries with sorted value from low to high
def make_frequency_dict(text):

    counted = dict(collections.Counter(text))
    sort = collections.OrderedDict(
        sorted(
            counted.items(),
            key=operator.itemgetter(1),
            reverse=False))

    return sort


# make a heap queue from node
def make_heap_node(freq_dict):

    for key in freq_dict:
        anode = Node(key, freq_dict[key])
        heap.append(anode)


# build tree
def merge_nodes():

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merge = Node(None, node1.freq + node2.freq)
        merge.left = node1
        merge.right = node2
        heapq.heappush(heap, merge)


# actual coding happens here
def encode_helper(root, current_code):

    if root is None:
        return

    if root.char is not None:
        codes[root.char] = current_code
        return

    encode_helper(root.left, current_code + "0")
    encode_helper(root.right, current_code + "1")


def get_encoded_text(text):

    encoded_text = ""

    # check the hole text is single charcter
    if len(codes) == 1:
        for char in codes:
            # change if codes[char] is ""
            codes[char] = "0"

    for char in text:
        encoded_text += codes[char]

    return encoded_text


def huffman_encoding(data):

    freq_dict = make_frequency_dict(data)

    make_heap_node(freq_dict)
    merge_nodes()

    root = heapq.heappop(heap)
    current_code = ""
    encode_helper(root, current_code)
    encoded_text = get_encoded_text(data)

    return encoded_text


def huffman_decoding(encoded_text):
    if encoded_text == "":
        return ""

    current_code = ""
    decoded_text = ""

    for bit in encoded_text:
        current_code += bit
        if current_code in codes.values():
            for key in codes:
                if current_code == codes[key]:
                    decoded_text += key
                    current_code = ""

    return decoded_text


def huffman_testing(test_text):

    if test_text != "":

        print("The size of the data is: {}\n".format(
            sys.getsizeof(test_text)))
        print("The content of the data is: {}\n".format(test_text))

        encoded_data = huffman_encoding(test_text)

        print("The size of the encoded data is: {}\n".format(
            sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))
        decoded_data = huffman_decoding(encoded_data)

        print("The size of the decoded data is: {}\n".format(
            sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))

    else:
        print("Your string is empty!")

    print("--------------------------------")

if __name__ == "__main__":
    codes = {}
    heap = []
    # test with different texts
    huffman_testing("aaaa")
    codes = {}
    heap = []
    huffman_testing("The bird is the word")
    codes = {}
    heap = []
    huffman_testing("")
