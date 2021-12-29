def direction(facing, turn):
    try:
        l = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

        if type(turn) != int: raise Exception('Invalid argument type')
        if -1080 <= turn >= 1080: raise Exception('The argument is out of range')
        if facing not in l: raise Exception('This facing is not correct')

        n = ((turn//45) + l.index(facing))%len(l)
        return l[n]
    except Exception as e:
        print(e)
