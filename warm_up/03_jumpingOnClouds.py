def jumping_on_clouds(c):
    length = len(c)
    i = 0
    step = 0
    while i < length-2:
        if c[i+2] == 0:
            step += 1
            i += 2
        elif c[i+1] == 0:
            step += 1
            i += 1
        else:
            return 'game is over'
    if i == (length - 2):
        return step+1
    else:
        return step


if __name__ == '__main__':
    a = [0, 0, 0, 1, 0, 0]
    print(jumping_on_clouds(a))