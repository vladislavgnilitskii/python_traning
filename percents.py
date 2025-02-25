def percents(x, y):
    """ What percentage of x is y"""
    one_percents = x / 100
    result = y / one_percents
    print(str(y) + " is " + str(result) + " percents of " + str(x))

percents(200, 50)
