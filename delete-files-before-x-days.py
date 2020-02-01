# Delete files older tha x days
# Author: Bairaktaris Emmanuel
# Date  : December 12, 2019
# Link  : http://repairmypc.net

import os, time, sys

folder_path = "//naboo/e$/Mail/Logs"
file_ends_with = ".log"
how_many_days_old_logs_to_remove = 1

now = time.time()
only_files = []

for file in os.listdir(folder_path):
    file_full_path = os.path.join(folder_path,file)
    if os.path.isfile(file_full_path) and file.endswith(file_ends_with):
        # Delete files older than x days
        if os.stat(file_full_path).st_mtime < now - how_many_days_old_logs_to_remove * 86400: 
             os.remove(file_full_path)
             print("\n File Removed : " , file_full_path)
