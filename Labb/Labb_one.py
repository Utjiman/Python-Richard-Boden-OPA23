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

# Scatter plots
# ..._data_np[:, 0] x-values (width)
# ... data_np[:, 1] y-values (lenght)
# color='' sets color to the dots
# label= set the "name" of the plots
plt.scatter(pichu_data_np[:, 0], pichu_data_np[:, 1], color='black', label='pichu')
plt.scatter(pikachu_data_np[:, 0], pikachu_data_np[:, 1], color='yellow', label='pikachu')
plt.scatter(test_data_np[:, 0], test_data_np[:, 1], color='blue', label='test points')

plt.xlabel('Width (cm)')
plt.ylabel('Lenght (cm)')
plt.title('Pichu vs Pikachu')
plt.legend()
plt.show()































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