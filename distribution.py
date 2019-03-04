"""
distribution.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:
Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.
Output of your program should look like this:
Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r
Notice about this example:
* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string
text=input("Please enter a string of text(the bigger the better): ")
dilatoryintroduction=("The distribution of characters in "'"{0}"'" is:")
print(dilatoryintroduction.format(text))
list1=list(text)
#print(list1)
list3s = []
list2s = []
for x in string.ascii_lowercase:
    list3s.append(list1.count(x))
    list2s.append(list1)
    #print(list2s)
    print(list3s)
    list4=zip(list1,list3s)
    print(list4)
    #list4=zip(list3,list2)
    #print(list4)
    
    
