import pandas as pd 


df = pd.read_table("tables.csv", sep=";", keep_default_na=False)
size = len(df)
f = open("query.txt", "w")
for i, d in enumerate(df.values):
    f.write("CREATE INDEX [IX_" + str(d[0]) + "_Satu]")
    f.write("\n")
    f.write("ON [NBFI_ALK].[Datamart].["+ str(d[0]) +"] ([Periode],[EntityID])")
    f.write("\n")
    f.write("\n")
f.close()

'''


'''
