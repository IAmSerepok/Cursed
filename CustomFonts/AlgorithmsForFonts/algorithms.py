import collections
import random


def first_algorithm(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        first_algorithm(left)
        first_algorithm(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            

def second_algorithm(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


def sub_func(array, start, end):
    if start >= end:
        return

    p = second_algorithm(array, start, end)
    sub_func(array, start, p - 1)
    sub_func(array, p + 1, end)


def third_algorithm(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def fourth_algorithm(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


def fifth_algorithm(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        fifth_algorithm(graph, next, visited)
    return visited


def sixth_algorithm(list_num, first_index, last_index, to_search):
    if last_index >= first_index:

        mid_index = (first_index + last_index) // 2
        mid_element = list_num[mid_index]

        if mid_element == to_search:
            return f"{mid_element} occurs in position {mid_index}"

        elif mid_element > to_search:
            new_position = mid_index - 1
            # new last index is the new position
            return sixth_algorithm(list_num, first_index, new_position, to_search)

        elif mid_element < to_search:
            new_position = mid_index + 1
            # new first index is the new position
            return sixth_algorithm(list_num, new_position, last_index, to_search)

    else:
        return "Does not appear in the list"


def seventh_algorithm(list_num, to_search):
    first_index = 0
    size = len(list_num)
    last_index = size - 1
    mid_index = (first_index + last_index) // 2
    mid_element = list_num[mid_index]
    is_found = True
    while is_found:
        if first_index == last_index:
            if mid_element != to_search:
                return " Does not appear in the list"
        elif mid_element == to_search:
            return f"{mid_element} occurs in position {mid_index}"
        elif mid_element > to_search:
            new_position = mid_index - 1
            last_index = new_position
            mid_index = (first_index + last_index) // 2
            mid_element = list_num[mid_index]
            if mid_element == to_search:
                return f"{mid_element} occurs in position {mid_index}"
        elif mid_element < to_search:
            new_position = mid_index + 1
            first_index = new_position
            last_index = size - 1
            mid_index = (first_index + last_index) // 2
            mid_element = list_num[mid_index]
            if mid_element == to_search:
                return f"{mid_element} occurs in position {mid_index}"


def eighth_algorithm(a):
    while is_sorted(a) is False:
        shuffle(a)


def is_sorted(a):
    n = len(a)
    for i in range(0, n-1):
        if a[i] > a[i+1]:
            return False
    return True


def shuffle(a):
    n = len(a)
    for i in range(0, n):
        r = random.randint(0, n-1)
        a[i], a[r] = a[r], a[i]


def ninth_algorithm():
    dist = [None] * len(nodes)
    for i in range(len(dist)):
        dist[i] = [float("inf")]
        dist[i].append([nodes[nodenum]])

    dist[nodenum][0] = 0
    queue = [i for i in range(len(nodes))]
    seen = set()
    while len(queue) > 0:
        min_dist = float("inf")
        min_node = None
        for n in queue:
            if dist[n][0] < min_dist and n not in seen:
                min_dist = dist[n][0]
                min_node = n
        queue.remove(min_node)
        seen.add(min_node)
        connections = connections_from(min_node)
        for (node, weight) in connections:
            tot_dist = weight + min_dist
            if tot_dist < dist[node.index][0]:
                dist[node.index][0] = tot_dist
                dist[node.index][1] = list(dist[min_node][1])
                dist[node.index][1].append(node)
    return dist


def tenth_algorithm(self, src):
    dist = [float("Inf")] * self.V
    dist[src] = 0

    for i in range(self.V - 1):

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in self.graph:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return

    self.printArr(dist)
