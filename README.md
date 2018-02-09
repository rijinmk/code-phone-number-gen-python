# Phone number generator

## Introduction 
This python code can be called in the command line with the correct arguments to generate all the phone-numbers. 

### Usage
```bash
phno-gen.py [-h] [--file FILE] [--prefix PREFIX] [--start START] [--end END] digits
````
`digits` are the only mandatory argument. 

### Positional Argument
```bash
  digits           Number of digits
````

### Optional Argument
```bash
  -h, --help       show this help message and exit
  --file FILE      File name
  --prefix PREFIX  The number prefixes, If there are more than one seperate
                   them with a comma, Like this: 050, 056, 052
  --start START    Starting number
  --end END        Ending number
````
