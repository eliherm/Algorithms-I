"""
Name: Elikem Hermon
Student Number: 20075527
I certify that this submission contains my own work, except as noted.
"""


def load_code_dictionary(dictionary_path):
    """Loads the code dictionary from a file"""
    codes = {}
    with open(dictionary_path, 'r') as code_dictionary:
        for line in code_dictionary:
            line_elements = line.split(" ")
            codes[int(line_elements[0])] = line_elements[1][:-1]  # Store the ascii value and code string
    return codes


class Encoder:
    def __init__(self, codes, filename):
        self.filename = filename
        self.codes = codes
        self.output = ""

    def encode(self):
        """Encodes a file using the code dictionary"""
        with open(self.filename, 'r') as input_file:
            output_list = []

            # Iterate through each character in the file
            for line in input_file:
                for char in line:
                    output_list.append(self.codes[ord(char)])

            self.output = ''.join(output_list)

    def save_output(self):
        """Outputs the encoded document to a file"""
        with open("./outputs/collection3" + self.filename[18:-4] + "-encoded.txt", 'w') as output_file:
            output_file.write(self.output)


input_files = ["./data/part2-input/EarthASCII.txt", "./data/part2-input/MysteryASCII.txt",
               "./data/part2-input/MythsASCII.txt", "./data/part2-input/SimakASCII.txt",
               "./data/part2-input/WodehouseASCII.txt"]

codes_dict = load_code_dictionary("./outputs/collection3/c3-code-strings.txt")

for file in input_files:
    encoded = Encoder(codes_dict, file)
    encoded.encode()
    encoded.save_output()
