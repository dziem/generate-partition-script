databaseName = 'NBFI'
tables = ['table1', 'table2']
yearStart = 2021
yearEnd = 2024
directory = "E:\\Microsoft SQL Server\\MSSQL11.IJKDB01\\MSSQL\\DATA\\IFUA_BALANCES\\"

f = open("file.txt", "w")

for i in tables:
    for j in range(yearStart, yearEnd + 1):
        for k in range (1, 13):
            groupName = i + "_" + str(j) + str(k).zfill(2)
            f.write("ALTER DATABASE " + databaseName)
            f.write("\n")
            f.write("ADD FILE")
            f.write("\n")
            f.write("(")
            f.write("\n")
            f.write("\tNAME = [" + groupName + "],")
            f.write("\n")
            f.write("\tFILENAME = '" + directory + groupName + ".ndf',")
            f.write("\n")
            f.write("\tSIZE = 512 KB,")
            f.write("\n")
            f.write("\tMAXSIZE = UNLIMITED,")
            f.write("\n")
            f.write("\tFILEGROWTH = 10000 MB")
            f.write("\n")
            f.write(") TO FILEGROUP " + groupName)
            f.write("\n")
            f.write("GO")
            f.write("\n")
        f.write("\n")
            
f.close()
