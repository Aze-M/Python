import time
import tracemalloc

tracemalloc.start()

def duplicates_set(_in_str: str) -> bool:  
    global set_alloc_tracked, max_set_alloc
    set_letters = {}

    for letter in _in_str:
        if letter in set_letters:
            if set_alloc_tracked == False:
                max_set_alloc = tracemalloc.take_snapshot()
                set_alloc_tracked = True
            return True
        set_letters[letter] = True

    return False

def duplicates_lst(_in_str: str) -> bool:
    global vec_alloc_tracked, max_vec_alloc
    list_letters = []

    for letter in _in_str:
        if letter in list_letters:
            if  vec_alloc_tracked == False:
                max_vec_alloc = tracemalloc.take_snapshot()
                vec_alloc_tracked = True
            return True
        list_letters.append(letter)

    return False

max_set_alloc: tracemalloc.Snapshot
set_alloc_tracked = False
max_vec_alloc: tracemalloc.Snapshot
vec_alloc_tracked = False
teststring = "abcdefghijklmnopqrstuvwxyzz"

now = time.perf_counter()

for _ in range(10):
    duplicates_lst(teststring)

print(time.perf_counter() - now)

now = time.perf_counter()

for _ in range(10):
    duplicates_set(teststring)

print(time.perf_counter() - now)
tracemalloc.stop()

stats_set: tracemalloc.Statistic = max_set_alloc.statistics('traceback')
stats_vec: tracemalloc.Statistic = max_vec_alloc.statistics('traceback')

for list in stats_set[:5]:
    print("%s memory blocks: %.1f KiB" % (list.count, list.size / 1024))
    for line in list.traceback.format():
        print(line)

for list in stats_vec[:5]:
    for line in list.traceback.format():
        print(line)