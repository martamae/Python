from sys import argv

script, filename = argv

#open file
txt = open(filename)

#print filename
print "Here's your file %r:" % filename

#read file and print
print txt.read()

#get filename again
#prompt
print "Type the filename again:"
#get input
file_again = raw_input("> ")

txt.close()

#open file again
txt_again = open(file_again)

#read and print file again
print txt_again.read()

txt_again.close()