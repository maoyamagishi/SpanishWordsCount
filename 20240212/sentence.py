import csv

def existChecker(countlst,word):
    exst = False
    place = 0
    for ii in range(len(countlst)):
        if countlst[ii][0] == word:
            exst = True
            place = ii
            break
    return exst,place

def AddOrApend(Count,disAssembry,pp):
    res = existChecker(Count,disAssembry[pp])
    if res[0]:
        Count[res[1]][1] +=1                       
    else:
        Count.append([disAssembry[pp],1])
        if disAssembry[pp] == '':
            print(disAssembry)


with open('DonQuixote.txt',encoding='utf-8') as f:
    # ファイルの内容の読み出し
    data = f.read()  
    data = data.lower()  # 小文字にする

goodbyeList = [',','-','_','\n',':','   ','¿','¡',';','0','1','2','3','4','5','6','7','8','9','[',']','(',')','«','»','(p','—']
Count = []
data = data.replace('\n','')
data = data.replace('!','.')
data = data.replace('?','.')

for ii in range(len(goodbyeList)):
    data = data.replace(goodbyeList[ii],'')
lst1 = data.split('.')

wordMat = []
with open('ver.csv',encoding='utf-8') as f:
    data = csv.reader(f)
    for row in data:
        wordMat.append(row)

kywLst = []
for ii in range(len(wordMat)):
    for jj in range(len(wordMat[ii])):
        kywLst.append(wordMat[ii][jj])


for kk in range(len(kywLst)):
    for ii in range(len(lst1)):
        keyword = kywLst[kk]
        if(keyword in lst1[ii]):
            disAssembry = lst1[ii].split(' ')
            while True:
                try:
                   disAssembry.remove('')
                except:
                    break 
            for jj in range(len(disAssembry)):
                if len(disAssembry) == 1:
                    continue
                if disAssembry[jj] == keyword:
                    if jj == 0:
                        AddOrApend(Count,disAssembry,jj + 1)
            
                    elif jj == len(disAssembry) -1:
                        AddOrApend(Count,disAssembry,jj -1)

                    else:
                        AddOrApend(Count,disAssembry,jj + 1)
                        AddOrApend(Count,disAssembry,jj - 1)
                
for ii in range(len(Count)):
    if Count[ii][1] > 5:
       print(Count[ii][0],",",Count[ii][1])

