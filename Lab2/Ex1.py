from random import randint
import timeit
import matplotlib.pyplot as plt

def selection_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]
    return array

def quick_sort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return array

lenghts = [100, 200, 300, 400, 500, 600, 700, 800, 900]
time_rand = [[], []]
time_sort = [[], []]
time_rev = [[], []]

for i in lenghts:
    lst = [randint(0, 100) for _ in range(i)]
    sort_lst = [_ for _ in range(i)]
    reverse_lst = [_ for _ in range(i, 0, -1)]
    time_rand[0].append(timeit.timeit(f"selection_sort({lst})", number=1, globals=globals()))
    time_rand[1].append(timeit.timeit(f"quick_sort({lst})", number=1, globals=globals()))
    time_sort[0].append(timeit.timeit(f"selection_sort({sort_lst})", number=1, globals=globals()))
    time_sort[1].append(timeit.timeit(f"quick_sort({sort_lst})", number=1, globals=globals()))
    time_rev[0].append(timeit.timeit(f"selection_sort({reverse_lst})", number=1, globals=globals()))
    time_rev[1].append(timeit.timeit(f"quick_sort({reverse_lst})", number=1, globals=globals()))

fig = plt.figure()
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0])
ax1 = fig.add_axes([0.0, 1.2, 1.0, 1.0])
ax2 = fig.add_axes([0.0, 2.4, 1.0, 1.0])

ax.plot(lenghts, time_rand[0], label="selection_sort")
ax.plot(lenghts, time_rand[1], label="quick_sort")
ax.legend(("Selection sort", "Quick sort"))
ax.text(500, 0.05, "Random List", fontsize=16, horizontalalignment = "center")

ax1.plot(lenghts, time_sort[0], label="selection_sort")
ax1.plot(lenghts, time_sort[1], label="quick_sort")
ax1.legend(("Selection sort", "Quick sort"))
ax1.text(500, 0.05, "Sorted List", fontsize=16, horizontalalignment = "center")

ax2.plot(lenghts, time_rev[0], label="selection_sort")
ax2.plot(lenghts, time_rev[1], label="quick_sort")
ax2.legend(("Selection sort", "Quick sort"))
ax2.text(500, 0.05, "Reverse List", fontsize=16, horizontalalignment = "center")

plt.show()
