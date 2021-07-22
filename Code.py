import csv
import fileinput
from os import write
import shutil 
import re
import sys
import tracemalloc
tracemalloc.start()
def translate(input,search,replace) :
    count =0
    for line in input:
        if search in line:
            count+= (line.lower()).count(search)
            sys.stdout.write(re.sub(search,replace,line,flags=re.IGNORECASE))
            # count+= line.count(replace)

        else:
            print(line, end ='')
    return count

shutil.copy('code\\t8.shakespeare.txt', 'code\BackupInputFile.txt')

with open('code\\french_dictionary.csv', 'r')as csvfile,\
        open('code\\frequency.csv','w',newline='')as csvWriteFile:
    csvFile = csv.reader(csvfile)
    csvWriteFile = csv.writer(csvWriteFile)
    csvWriteFile.writerow(['English word','French word','Frequency'])
    for row in csvFile:
        search = row[0]
        replace = row[1]
        print(search,replace)
        inputFile =fileinput.FileInput("code\\t8.shakespeare.txt", inplace=True)       
        
        freq = translate(inputFile,search,replace)
        row.append(freq)
        csvWriteFile.writerow(row)
       


print(tracemalloc.get_traced_memory()) 

        


