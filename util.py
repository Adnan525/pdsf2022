# a few functions have been taken from nearest neighbour assignment
from typing import List


# reading the data by file name
def read_multi_dim_data(filename):
    dataset = []
    with open(filename, "r") as f:
        for line in f:
            dataset.append(line)

    return dataset


# takes a list where even is x, odd is y
# returns list[list[float]]
def genCoord(li):
    coordinates = []
    for line in li:
        # get rid of the new line char
        # last line won't have the \n character
        targetLine = line[0:len(line)] if line == li[len(li) - 1] else line[0:len(line) - 1]
        tempString = targetLine.split(" ")
        tempList = []
        for val in tempString:
            co = float(val)
            tempList.append(co)
        coordinates.append(tempList)
    return coordinates


# will generate x, y value
# slightly redundant since could do all this while reading the data
def helper(li: List[List[float]]):
    x = []
    y = []
    for i in li:
        x.append(i[0])
        y.append(i[1])
    return x, y


# plotting function
def plotInFig(x, y, fig, canvas):
    # this will clear canvas everytime the function gets called
    # so no overlapping
    canvas.figure.clear()
    fig.add_subplot(111).scatter(x, y, color="red")
    canvas.draw()
