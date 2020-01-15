#+======================================================================================+
# |Author           : Kolli Hrudhay
# |Package          : Library Books
# |Module           : readingFun.py
# |Language         : Python 3.7
# |Description      : This module when called by the Assignment_code.py module, 
#                     will return the command provided by the later module 
#                     (from the files inputPS6.txt,promptsPS6.txt files) in the 
#                     required and proper format (without extra spaces,symbols etc) 
#                     for the Assignment_code.py module to correctly identify 
#                     and execute the function.
#
#+======================================================================================+



def readingFun(func):
    ''' This function read values from the input provided by the Assignment_code.py module and return the command
        in the right/required format. 
    ''' 
    elements = []
    with open(func, 'r') as file1:
        for f1 in file1:
            if len(f1)>1:
                if ',' in f1:
                    temp = f1.split(',')

                elif ':' in f1:
                    temp = f1.split(':')

                else:
                    temp=[f1]

                for i in range(len(temp)):
                    temp[i] = temp[i].strip()
           
                elements.append(temp)

    return elements
