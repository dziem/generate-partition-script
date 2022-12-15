databaseName = 'NBFI'
yearStart = 2021
yearEnd = 2024
partitionName = "PS_MonthWise"
partitionAlias = "PF_MonthlyPartition"
tableName = "table1"

f = open("ps.txt", "w")

f.write("USE " + databaseName)
f.write("\n")
f.write("GO")
f.write("\n")
f.write("CREATE PARTITION SCHEME " + partitionName)
f.write("\n")
f.write("AS PARTITION " + partitionAlias)
f.write("\n")
f.write("TO")
f.write("\n")
f.write("(")
f.write("\n")

for j in range(yearStart, yearEnd + 1):
    counter = 0
    f.write("\t")
    for k in range (1, 13):
        counter += 1
        groupName = tableName + "_" + str(k).zfill(2) + str(j)
        f.write("'" + groupName + "',")
        if counter == 3:
            counter = 0
            f.write("\n")
            f.write("\t")
    f.write("\n")

f.write("\t")
f.write("'Primary'")
f.write("\n")
f.write(");")

f.close()
