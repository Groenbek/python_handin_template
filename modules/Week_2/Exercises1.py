import csv

""" Create a python file with 3 functions: """
"""1A that can print content of a csv file to the console"""
def print_file_content(file):
    with open(file) as file_object:
        print(file_object.read())


"""1B that can take a list of tuple and write each element to a new line in file"""
def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as file_object:
        for s in lst:
            for elm in s: 
                file_object.write(elm + '\n')

"""1C that take a csv file and read each row into a list"""
def read_csv(input_file):
    lst = []
    with open(input_file) as file_object:
        reader = csv.reader(file_object)
        header_row = next(reader)

        for row in reader:
            lst.append(row)
    return lst