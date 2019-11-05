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
            codes[line_elements[1][:-1]] = int(line_elements[0])  # Store the ascii value and code string
    return codes


class Decoder:
    def __init__(self, codes, filename):
        self.filename = filename
        self.codes = codes
        self.output = ""

    def decode(self):
        """Decodes a file using the code dictionary"""
        with open(self.filename, 'r') as input_file:
            curr_char = ""  # Holds the current code string from the input file
            output_list = []

            # Iterate through each character in the file
            for line in input_file:
                for char in line:
                    curr_char += char
                    if curr_char in self.codes:
                        output_list.append(chr(self.codes[curr_char]))  # Convert the ascii number into a character
                        curr_char = ""  # Reset the current code string

            self.output = ''.join(output_list)

    def save_output(self):
        """Outputs the decoded document to a file"""
        with open("./outputs/collection3" + self.filename[21:-12] + "-decoded.txt", 'w') as output_file:
            output_file.write(self.output)


input_files = ["./outputs/collection3/EarthASCII-encoded.txt", "./outputs/collection3/MysteryASCII-encoded.txt",
               "./outputs/collection3/MythsASCII-encoded.txt", "./outputs/collection3/SimakASCII-encoded.txt",
               "./outputs/collection3/WodehouseASCII-encoded.txt"]

codes_dict = load_code_dictionary("./outputs/collection3/c3-code-strings.txt")

for file in input_files:
    decoded = Decoder(codes_dict, file)
    decoded.decode()
    decoded.save_output()
