#https://github.com/rijinmk/code-phone-number-gen-python

import argparse
import time
import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("digits",help="Number of digits")
parser.add_argument("--file",help="File name")
parser.add_argument("--prefix",help="The number prefixes, If there are more than one seperate them with a comma, Like this: 050, 056, 052")
parser.add_argument("--start",help="Starting number")
parser.add_argument("--end",help="Ending number")
args = parser.parse_args()

# print args 

digits = int(args.digits)

file_name = str(time.time())+'.txt'; 
prefix = ['']
start = 0
end = int('9' * int(args.digits))

if(args.file):
    file_name = args.file

if(args.prefix):
    prefix = (args.prefix).split(',')

if(args.start):
    start = int(args.start)    

if(args.end):
    end = int(args.end)

f = open(file_name, 'w')

for p in prefix:
    print start
    if(args.prefix):
        print 'Current prefix: ', (p + ('X' * digits))
    for i in tqdm.tqdm(range(start, end, 1)): 
        number = p.strip()
        number += '0' * (digits-len(str(i)))
        number += str(i)
        f.write(number + '\n')

f.close()
print 'File ', file_name, ' created. This file contains all your numbers'
        