#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a
#list of words using the split() function.
#The program should build a list of words.
#For each word on each line check to see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

fname = raw_input("Enter file name: ")
fhand = None
try:
    fhand = open(fname)
except:
    print 'File cannot be opened.', fname
    exit()

#list constructor
lst = []
read_file = fhand.read().strip()


while ( False ):
    listwords = read_file.split()
    listwords in lst
    lst.append(listwords)
print lst

#for line in read_file:
#    listwords = read_file.split()
#
#    if listwords in lst == False:
#    lst.append(listwords)


#for line in fh

#    sline = split()
#    lst.append(sline)


#lst.append(b_words)





#while
#    lst.append()

#for line in fh:
#print line.rstrip()