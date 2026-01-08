from bridges.bridges import *
from bridges.data_src_dependent.data_source import *
import sys
import random
dct = {}
uniquewords = []
i = 0
def getFrequency(work):
    if not work:
        return dct
    if work[0] not in dct.keys(): #checks if key exists and initilizes to a frequency of 1
        dct[work[0]] = 1
    else:
        dct[work[0]] = dct[work[0]] + 1 #if it finds it again it will add 1 to the frequeency
        del work[0] #gets rid of it to update the list for recursion
        return getFrequency(work) #recursion part here
def main():
# create the Bridges object, set credentials
    bridges = Bridges(2, "yhanafi2023", "486838682931")
# get the shakespeare data
    my_list = get_shakespeare_data() #IMPORTed frmo the bridges api
# pick a work at random
    work1 = my_list[random.randrange(len(my_list))]
    work = work1.text.split()
    for i in work1.text:
        i.strip('\n')
        index1=0
    for i in work:
        for letter in i:
            if letter == '.' or letter == ',' or letter == '"' or letter == "'" or letter == ";" or letter == "!" or letter
== "?" or letter == ":":
                i = i.replace(letter, "") #gets rid of punctuation and the newlines
        work[index1] = i
        index1= index1+1
    work = [i.lower() for i in work] #makes lowercase so words dont get counted separetly
    freqdct = getFrequency(work) #makes a dictionary for us to use
    freqdctorder = {w: f for w,f in sorted(freqdct.items(), key=lambda i:i[1], reverse=True)} #uses
#lambda to get the dictionary in order of frequency, descending order
    for i in range(len(freqdctorder.keys())): #iterates the loop for how ever many words there were
#that were unique
        print(f'Word: {list(freqdctorder.keys())[i]} has a frequency of
{freqdctorder[list(freqdctorder.keys())[i]]}')
