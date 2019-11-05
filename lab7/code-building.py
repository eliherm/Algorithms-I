"""
Name: Elikem Hermon
Student Number: 20075527
I certify that this submission contains my own work, except as noted.
"""

import heapq


class Node:
    """Binary tree used to store code strings"""
    def __init__(self, ascii_val, frequency):
        self.ascii_val = ascii_val
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


class CodeBuilder:
    def __init__(self, documents):
        self.documents = documents
        self.frequencies = {}   # Stores the frequency of each printable ASCII character
        self.code_strings = {}  # Stores the code string for each ascii value

    def generate_frequencies(self):
        """Generates the frequency of characters in a list of cannonical documents"""
        # Initialize the frequencies
        self.frequencies[10] = 0
        for i in range(32, 127):
            self.frequencies[i] = 0

        # Iterate through each of the documents
        for filename in self.documents:
            # Open the file
            with open(filename, 'r') as input_file:
                # Iterate through each character in the file
                for line in input_file:
                    for char in line:
                        self.frequencies[ord(char)] += 1  # Update the frequency count

    def generate_code(self, root, code_string):
        """Traverses a binary tree to retrieve code strings"""
        # Check if the current node is a leaf
        if root.ascii_val is not None:
            self.code_strings[root.ascii_val] = code_string  # Add the code string to the dictionary
            return

        # Traverse the tree recursively
        self.generate_code(root.left, code_string + "0")
        self.generate_code(root.right, code_string + "1")

    def huffman_algorithm(self):
        """Computes code strings for a list of character frequencies"""
        heap = []   # Stores character nodes in ascending order of frequency

        for char in self.frequencies:
            char_node = Node(char, self.frequencies[char])   # Create node for the character
            heapq.heappush(heap, char_node)  # Insert node into the heap

        while len(heap) > 1:
            # Pop two characters with the smallest frequencies
            left_node = heapq.heappop(heap)
            right_node = heapq.heappop(heap)

            # Create parent node of the left and right nodes
            parent_node = Node(None, left_node.frequency + right_node.frequency)
            parent_node.left = left_node
            parent_node.right = right_node

            heapq.heappush(heap, parent_node)  # Insert node back into the heap

        root = heapq.heappop(heap)  # Retrieve the root nde from the heap
        self.generate_code(root, "")

    def output_codes(self):
        """Outputs the code dictionary to a file"""
        with open('./outputs/collection3/c3-code-strings.txt', 'w') as output_file:
            for char in self.code_strings:
                output_file.write(str(char) + " " + self.code_strings[char] + "\n")


# canonical_documents = ["./data/words1ASCII.txt"]
# canonical_documents = ["./data/collection2/Short Text " + str(i) + "ASCII.txt" for i in range(1, 11)]
canonical_documents = ["./data/collection3/ChestertonASCII.txt", "./data/collection3/DickensASCII.txt"]
builder = CodeBuilder(canonical_documents)
builder.generate_frequencies()
builder.huffman_algorithm()
builder.output_codes()
