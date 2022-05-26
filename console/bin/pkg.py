from multiprocessing import connection
import os
import urllib3
import shutil
import zipfile
import tmp
from lib.console.tools import search_util
def install_package(package_url):
    connect = urllib3.PoolManager()
    out_path = tmp.PATH
    try:
        if os.path.exists(package_url):
            pass
        else:
            file =  os.path.basename(package_url)
            file_and_path = os.path.join(out_path, file)
            with open(file_and_path, "wb") as out_file, connect.request('GET',package_url, preload_content=False) as resp:
                shutil.copyfileobj(resp, out_file)
    except:
        pass

def main(args):
    if "install" in args:
        install_package(args[search_util.search_index(args,"install")])
