import urllib.request
from flags import flags
import time
import os

timeStart, cpuStart = time.time(), time.process_time()
numBytes = 0
for flagCode in flags:
    i = 0
    flagFile = flagCode + "-lgflag.gif"
    url = "https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/" + flagFile
    # Download all flag files into a directory named flags
    urllib.request.urlretrieve(url, "flags/" + flagFile)
    numBytes += os.path.getsize("flags/" + flagFile)
    # print(flagFile)
    i += 1

timeStop, cpuStop = time.time(), time.process_time()
totalTime = (timeStop - timeStart)
cpuTotal = (cpuStop - cpuStart)

f = open("seq.txt", "w")

# Report the number of bytes downloaded, execution time, and CPU time of the script
f.write("Bytes downloaded %s bytes\n"
        "Time: %s seconds\n"
        "CPU Time: %s seconds"
        % (numBytes, format(totalTime, '.2f'), format(cpuTotal, '.2f')))

f.close()
