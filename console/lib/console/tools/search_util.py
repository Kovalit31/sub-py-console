import os

def search_index(array, need_to_search):
    for x in range(len(array)):
        if array[x] == need_to_search:
            return x + 1
    return -1

def search_bin_file(dir, file):
    if os.path.exists(os.path.join(dir, file)):
        return True
    return False