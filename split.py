__author__ = 'alex'

#export contacts from google, convert file to 1251 codepage and reference it in command below
f = open('F:\\My\\Split_VCF_file\\contacts2.vcf', 'r')
line = f.readline()
print line
#f.read()
#print f
record=""
name=1
while len(line)>0:
    if line[0:6] == "BEGIN:":
        record = line
    elif line[0:4] == "END:":
        record += line
        print "Result:", record
        f_n = "output\\"+str(name)+".vcf"
        print f_n
        f_out = open(f_n, 'w')
        f_out.write(record)
        f_out.close()
        name+=1
    elif line[0:3] == "TEL":
        line =line.replace(" ", "")
        line =line.replace("-", "")
        record += line
#    elif line[0:3] == "FN:": # name
#        name =line[3:]
    else:
        record += line
    line = f.readline()
    print line

f.close()
