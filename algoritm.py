# numbers = [1, 2, 3, 4]
# number = int(input('Число на проверку в базе данных: '))
# def encode(numbers, number):
#     for n in range(len(numbers)):
#         if numbers[n] == number:
#             print('Да, такое число есть!')
#         else:
#             pass

# encode(numbers, number)



# def binary_search_recursion(data, target):
#     if data == []:
#         return False
#     elif len(data) == 1:
#         return data[0] == target
#     else:
#         half = len(data) // 2
#         if data[half] > target:
#             return binary_search_recursion(data[:half], target)
#         else:
#             return binary_search_recursion(data[half:], target)


# numbs = [75, 26, 45, 74, 63, 85, 65, 43, 59, 64]

# def bubble_sort(data):
#     n = len(data)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if data[j] > data[j+1]:
#                 data[j], data[j+1] = data[j+1], data[j]

# sort_quadratic(numbs)'


# def quick_sort(arr, low, high):
#     if low < high:
#         pivot = partition(arr, low, high)
#         quick_sort(arr, low, pivot - 1)
#         quick_sort(arr, pivot + 1)

# def partition(arr, low, high):
#     i = (low - 1)
#     pivot = arr[high]

#     for j in range(low, high):
#         if arr[j] < pivot:
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i+1], arr[high] = arr[high], arr[i + 1]
    
#     return i + 1


graph = {'start': {'a': 6, 'b': 2}, 'a': {'finish': 1}, 'b' : {'a': 3, 'finish': 5}, 'finish': {}}

infinity = float("inf")
costs = {'a': 6, 'b': 2, 'finish': infinity}

parents = {'a': 'start', 'b': 'start', 'finish': None}

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node

    processed.append(node)
    node = find_lowest_cost_node(costs)

print(costs)
print(parents)