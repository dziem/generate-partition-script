databaseName = 'NBFI'
yearStart = 2021
yearEnd = 2024
functionName = "PF_MonthlyPartition"
dataType = "DATE"

f = open("pf.txt", "w")

f.write("USE " + databaseName)
f.write("\n")
f.write("GO")
f.write("\n")
f.write("CREATE PARTITION FUNCTION [" + functionName + "] (" + dataType + ")")
f.write("\n")
f.write("AS RANGE RIGHT FOR VALUES ")
f.write("\n")
f.write("(")
f.write("\n")

for j in range(yearStart, yearEnd + 1):
    counter = 0
    f.write("\t")
    for k in range (1, 13):
        counter += 1
        if j != yearStart or k != 1:
            f.write("'" + str(j) + str(k).zfill(2) + "01',")
        if counter == 3:
            counter = 0
            f.write("\n")
            f.write("\t")
    f.write("\n")

f.write("\t")
f.write("'" + str(yearEnd + 1) + "0101'")
f.write("\n")
f.write(");")

f.close()
