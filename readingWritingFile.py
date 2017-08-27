fw = open('myFirstFile.txt', 'w')
fw.write('Hi, This my first file created in python\n')
fw.write('Here i am writing a last line in my file\n')
fw.close()


fcsv = open('try.csv', 'w')
fcsv.write('Name, Age, DOB, marks\n')
fcsv.write('Satish, 24, 20011993, 86\n')
fcsv.write('netra, 23, 28081994, 90\n')
fcsv.close()


##############################################################
#Reading File
##############################################################

fr = open('myFirstFile.txt', 'r')
textData = fr.read()
print(textData)
print(textData.find('last'))
fr.close()