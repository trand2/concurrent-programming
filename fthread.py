import urllib.request
from flags import flags
import concurrent.futures
import time
import os

def downloadImages(flagCode):
    numBytes = []
    i = 0
    flagFile = flagCode + "-lgflag.gif"
    url = "https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/" + flagFile
    # Download all flag files into a directory named flags
    urllib.request.urlretrieve(url, "flags/" + flagFile)
    numBytes.append(os.path.getsize("flags/" + flagFile))
    i += 1
    print(flagFile)
    return numBytes


if __name__ == '__main__':
    res = []
    timeStart, cpuStart = time.time(), time.process_time()
    n = 100000
    args = (flagCode for flagCode in flags)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for numbytes in executor.map(downloadImages, args):
            res.extend(numbytes)

    f = open("fthread.txt", "w")

    totalBytes = sum(res)
    totalTime = (time.time() - timeStart)
    cpuTotal = (time.process_time() - cpuStart)

    # Report the number of bytes downloaded, execution time, and CPU time of the script
    f.write("Bytes downloaded %s bytes\n"
            "Time: %s seconds\n"
            "CPU Time: %s seconds"
            % (totalBytes, format(totalTime, '.2f'), format(cpuTotal, '.2f')))

    f.close()
