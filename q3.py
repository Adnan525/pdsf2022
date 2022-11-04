def read_ellipse_file(filename):
    dataset = []

    f = None
    try:
        f = open(filename, 'r')
        while True:
            line = f.readline()
            if len(line) == 0:  # end of file
                break
            line = line.replace('\n', '')
            xystring = line.split(' ')
            dataset.append((float(xystring[0]), float(xystring[1])))
    except Exception as ex:
        print(ex.args)
    finally:
        if f:
            f.close()
    return dataset
# end of function

data = read_ellipse_file('ellipse2a.txt')
print(data)