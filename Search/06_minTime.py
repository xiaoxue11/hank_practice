"""
Created on :  12:23 AM
Author : Xue Zhang
"""


def min_time1(machines, goal):
	cost = 0
	count = 0
	days = min(machines)
	new_ms = machines 
	while cost < goal:
		print(days)
		new_ms = sorted(new_ms)
		print(new_ms)
		count = new_ms.count(new_ms[0])
		cost = sum([days // i for i in machines ])
		for _ in range(count):
			new_ms.append(2 * new_ms[0])
			new_ms.pop(0)
		days += 1
		print(cost)
		print('*'*20)
	return days - 1


def min_time2(machines, goal):
	cost = 0
	machines = sorted(machines)
	d_ms = {k: v for k, v in enumerate(machines)}
	days = machines[0]
	while cost < goal:
		new_ms = {k: v for k, v in d_ms.items() if v <= days}
		for k, v in new_ms.items():
			cost += days // v
			d_ms[k] = v + machines[k]
		days += 1
		# print(cost)
		# print('*'*20)
	return days - 1


def min_time(machines, goal):
	per_rate = sum([1 / i for i in machines])
	low = int(goal / per_rate)
	print(low)
	high = min(machines) * goal
	print(high)
	while low <= high:
		days = low + (high - low) // 2
		total = get_num_count(machines, goal, days)
		if total < goal:
			low = days + 1
		else:
			high = days -1
	return low



def get_num_count(machines, goal, num_days):
    total = 0
    for machine in machines:
        total += (num_days // machine)
    return total


if __name__ == '__main__':
    a = [2, 3]
    target = 5
    ans = min_time(a, target)
    print(ans)
