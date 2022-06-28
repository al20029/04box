
import os
 
for curDir, dirs, files in os.walk("test"):
    for file in files:
        print(os.path.join(curDir, file))