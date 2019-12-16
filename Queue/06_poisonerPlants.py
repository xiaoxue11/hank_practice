def poisonous_plants(p):
    n = len(p)
    days = [0]* n 
    s = [0]
    max_days = 0
    min_value = p[0]

    for i in range(1, n):
        min_value = min(min_value, p[i])
        if p[i] > p[i-1]:
            days[i] = 1 
        while s and p[s[-1]] >= p[i]:
            if p[i] > min_value:
                days[i] = max(days[i], days[s[-1]] + 1)
            s.pop()
        max_days = max(max_days, days[i])
        s += [i]

    return max_days



if __name__ == '__main__':
    plants = [6, 5, 8, 4, 7, 10, 9]
    result = poisonous_plants(plants)
    print(result)
