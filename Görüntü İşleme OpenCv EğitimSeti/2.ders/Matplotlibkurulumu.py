import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('buraya excel dosya adı', sep=';')



plt.figure(figsize=(12, 6))
# plt.plot(df.ad, df.maas)
# plt.plot(df.ad, df.yas)
# plt.xlabel('İsimler')
# plt.ylabel('Yaşlar')
# plt.title('Ad & Yaş Grafiği')



# plt.subplot(1, 2, 1)
# plt.plot(df.ad, df.maas)
# plt.subplot(1, 2, 2), plt.plot(df.ad, df.yas)




# plt.scatter(df.ad, df.maas)
# plt.scatter(df.ad, df.yas)


# plt.pie(df.maas, label=df.ad)

plt.pie(df.yas, labels=df.ad)


plt.show()