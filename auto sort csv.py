import os
from datetime import datetime
import shutil

SourceDir=r"/Users/himshitasingh/testrepo"

def organizecsvbydate(path):
    os.chdir(path)
    files=[f for f in os.listdir() if os.path.isfile(f) and f.endswith('.csv')]

    for file in files:
        timestamp=os.path.getmtime(file)
        date_str=datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

        if not os.path.exists(date_str):
            os.makedirs(date_str)
            print(f"Folder created : {date_str}")


        shutil.move(file,os.path.join(date_str,file))
        print(f"Moved {file} to {date_str}/")



if __name__ == "__main__":
    organizecsvbydate(SourceDir)
    print("All CSVs has been sorted!")