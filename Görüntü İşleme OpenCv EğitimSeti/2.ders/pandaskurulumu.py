import pandas as pd


personel_list = {'ad':  ['burak', 'gamze', 'asli', 'önder', 'eylül', 'ozan'],
                 'yas': [29, 20, 27, 25, 20, 24],
                 'maas':[5000, 4000, 1000, 4000, 9000, 6000]}




print(type(personel_list))

df = pd.DataFrame(personel_list)


# excel'den veri çekme

# df = pd.read_csv("dosya adı")



print(df.head(3))  #belirtilen sayiya kadar veri çekme



#print(df.columns) #tüm kolanların isimleri alma



#print(df.describe())  #kaç sayısal verisi var gösteriyor


#print(df.dtypes)
#print(df.tail(2))
#print(df.shape)
# print(df[df['maas'] > 4000])
# print(df.sum())  #toplama 
#print(df['maas'].sum())