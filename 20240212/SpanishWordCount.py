import csv

with open('DonQuixote.txt',encoding='utf-8') as f:
    # ファイルの内容の読み出し
    data = f.read()  
    data = data.lower()  # 小文字にする

goodbyeList = ['.',',','-','_','\n',':','   ','¿','¡','?','!',';','0','1','2','3','4','5','6','7','8','9','[',']','(',')']
wordList = []
Count = []
data = data.replace('\n',' ')
lst1 = data.split(' ')

with open('wordlistImperfect.csv',encoding='utf-8') as f:
    data = csv.reader(f)
    for row in data:
        wordList.append(row)


for ii in range(len(wordList)):
    Count.append(0)
for ii in range(len(lst1)):
    for jj in range(len(goodbyeList)):
        string = lst1[ii]
        lst1[ii] = string.replace(goodbyeList[jj],'')
        lst1[ii] = lst1[ii].replace(' ','')
    for jj in range(len(Count)):
        if lst1[ii] in wordList[jj]:
            Count[jj] += 1 


for ii in range(len(wordList)):
    print(f"{wordList[ii][0]},{Count[ii]}")

