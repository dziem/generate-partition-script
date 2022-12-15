databaseName = 'NBFI'
tables = ['table1', 'table2']
yearStart = 2021
yearEnd = 2024

f = open("filegroup.txt", "w")

for i in tables:
    for j in range(yearStart, yearEnd + 1):
        for k in range (1, 13):
            f.write("ALTER DATABASE " + databaseName)
            f.write("\n")
            f.write("ADD FILEGROUP " + i + "_" + str(j) + str(k).zfill(2))
            f.write("\n")
            f.write("GO")
            f.write("\n")
        f.write("\n")
            
f.close()
