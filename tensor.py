#!/usr/bin/python3

import numpy as np
import os

def concatenateTensor(folder):
    """
    Function creates one tensor for all files in folder
    folder: str
    """
    files = os.listdir(folder)
    tensors = []  # array of each tensor per filename
    idx_2_filename = {}
    filename_2_idx = {}
    idx = 0
    for filename in os.listdir(folder):
        tensors.append(generateTensor(folder + "/" + filename))
        idx_2_filename[idx] = filename
        filename_2_idx[filename] = idx
        idx += 1
    y = list(range(0,idx))
    x = np.concatenate(tensors)
    return x, idx_2_filename, filename_2_idx, y


def generateTensor(filename):
    """
    Function to generate tensor per file
    filename: str
    """
    f = open(filename, "r")
    data = f.readlines()

    # source: https://en.wikipedia.org/wiki/Nucleotide
    nucleotideWeights = {"A":[1, 0, 0, 0],
                         "C":[0, 1, 0, 0],
                         "G":[0, 0, 1, 0],
                         "T":[0, 0, 0, 1],
                         "U":[0, 0, 0, 1],
                         "W":[0.5, 0, 0, 0.5],
                         "S":[0, 0.5, 0.5, 0],
                         "M":[0.5, 0.5, 0, 0],
                         "K":[0, 0, 0.5, 0.5],
                         "R":[0.5, 0, 0.5, 0],
                         "Y":[0, 0.5, 0, 0.5],
                         "B":[0, 0.33, 0.33, 0.33],
                         "D":[0.33, 0, 0.33, 0.33],
                         "H":[0.33, 0.33, 0, 0.33],
                         "V":[0.33, 0.33, 0.33, 0],
                         "N":[0.25, 0.25, 0.25, 0.25]}

    height = int(len(data)/2)
    breadth = 4
    length = len(data[1]) - 1  # to exclude "\n"
    t = np.zeros((height, breadth, length))

    # shape = (height, breadth, length) of 3d object
    # height = num of fragments
    # breadth = num of nucleotides
    # length = length of fragment

    i = 0
    for line in data:
        if line[0] == ">" or line == "\n":
            continue
        else:
            k = 0
            for n in line:
                if n in nucleotideWeights:
                    for j in range(len(nucleotideWeights[n])):
                        t[i, j, k] = nucleotideWeights[n][j]
                k += 1
            i += 1


    return t
x, i2f, f2i, y = concatenateTensor("tensorDir")
print(x)
print(i2f)
print(f2i)
print(y)
