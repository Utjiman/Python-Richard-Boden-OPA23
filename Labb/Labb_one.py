import matplotlib as plt
import numpy as np

test_points = "C:/Users/utjis/OneDrive - Handelsakademin/Python-Github/Python-Richard-Boden-OPA23/Data/test_points.txt"
pikachu = "C:/Users/utjis/OneDrive - Handelsakademin/Python-Github/Python-Richard-Boden-OPA23/Data/pikachu.txt"
pichu = "C:/Users/utjis/OneDrive - Handelsakademin/Python-Github/Python-Richard-Boden-OPA23/Data/pichu.txt"



def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file]
    return lines


test_points_data = read_file(test_points)
pikachu_data = read_file(pikachu)
pichu_data = read_file(pichu)
print(test_points_data)
print(pikachu_data)
print(pichu_data)