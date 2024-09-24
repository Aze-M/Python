import threading;
import os;
import sys;

def find_file_threaded(name : str, start_dir: str) -> list:
    work_list = []
    out_list = []
    threads = []
    lock = threading.Lock()

    try:
        dirs = os.scandir(start_dir)
    except FileNotFoundError:
        print("No directory, Exiting!")
        return []
    
    for dir in os.scandir(start_dir):
        if dir.is_dir() and dir.name != "scripts": # skip starting directory
            work_list.append(dir)
        if dir.is_file() and dir.name.find(name) != -1:
            out_list.append(dir.path)

    for i in range(os.cpu_count()):
        thread = threading.Thread(target=find_file_thread, args=(name, work_list, out_list, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return out_list

def find_file_thread(name: str, work_list: list, out_list: list, lock : threading.Lock):
    while len(work_list) > 0 :

        with lock:
            work_path = work_list.pop()
        
        for dir in os.scandir(work_path):
            if dir.is_dir() and dir.name != "scripts": # skip starting directory
                work_list.append(dir)
            if dir.is_file() and dir.name.find(name) != -1:
                out_list.append(dir.path)
        
path = ".\\scripts"
try:
    search = sys.argv[1].split(" ")[0]
except ValueError or IndexError:
    print("No arguments given, Exiting!")
    exit()

out = find_file_threaded(search, path)

for line in out:
    print(line)