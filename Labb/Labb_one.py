import matplotlib.pyplot as plt
import numpy as np

test_points_path = "C:/Users/utjis/OneDrive - Handelsakademin/Python-Github/Python-Richard-Boden-OPA23/Data/test_points.txt"
pikachu_path = "C:/Users/utjis/OneDrive - Handelsakademin/Python-Github/Python-Richard-Boden-OPA23/Data/pikachu.txt"
pichu_path = "C:/Users/utjis/OneDrive - Handelsakademin/Python-Github/Python-Richard-Boden-OPA23/Data/pichu.txt"

def read_and_convert(file_path):
    data = []
    with open(file_path, 'r') as file:
        # Skip first part
        next(file)
        for line in file:
            # Clear parantheses and non-numerical
            cleaned_line = line.strip().replace('(', '').replace(')', '')
            # convert to a list of float
            point = np.fromstring(cleaned_line, dtype=float, sep=',')
            data.append(point)
    return np.array(data)

with open(test_points_path, 'r') as file:
    data_str = file.read()

data_str_cleaned = data_str.replace('(', '').replace(')', '')

test_data_np = np.fromstring(data_str_cleaned, dtype=float, sep=', ')
# reformat to 2d-array
test_data_np = test_data_np.reshape(-1, 2)

pikachu_data_np = read_and_convert(pikachu_path)
pichu_data_np = read_and_convert(pichu_path)


print(pichu_data_np)
print(pikachu_data_np)
print(test_data_np)











'''
# function to read a file and return the content as a list
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file]
    return lines


test_points_data = read_file(test_points)
pikachu_data = read_file(pikachu)
pichu_data = read_file(pichu)
'''