databaseName = 'NBFI_RAW'
tables = ['PMV_Rincian','PP_RincianPembiayaan','PP_RincianLainya']
yearStart = 2020
yearEnd = 2035

f = open("resizeRAW.txt", "w")

for i in tables:
    for j in range(yearStart, yearEnd + 1):
        for k in range (1, 13):
            f.write("USE [" + databaseName + "]")
            f.write("\n")
            f.write("GO")
            f.write("\n")
            f.write("ALTER DATABASE [" + databaseName + "]")
            f.write("\n")
            f.write("MODIFY FILE ( NAME = N' " + i + "_" + str(j) + str(k).zfill(2) + "', FILEGROWTH = 1000MB )")
            f.write("\n")
            f.write("GO")
            f.write("\n")
        f.write("\n")
            
f.close()

'''
USE [NBFI_ALK]
GO
ALTER DATABASE [NBFI_ALK]
MODIFY FILE ( NAME = N'DataMart_Asuransi_202111', FILEGROWTH = 1000MB )
'''