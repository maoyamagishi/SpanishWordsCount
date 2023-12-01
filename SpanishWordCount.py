with open('textdata.txt',encoding='utf-8') as f:
    # ファイルの内容の読み出し
    data = f.read()  
    data = data.lower()  # 小文字にする

goodbyeList = ['.',',','-','_','\n',':','   ','¿','¡','?','!',';','0','1','2','3','4','5','6','7','8','9','[',']','(',')']
wordList = []
Count = []
lst1 = data.split(' ')
wordList.append(['estar','estoy', 'estás','está','estamos','estáis','están'])
wordList.append(['ser', 'soy','eres','es','somos','sois','son'])
wordList.append(["tener","tengo","teneis","tiene","tenemos","tenéis","tienen"])
wordList.append(["ir","voy","vas","va","vamos","vais","van"])
wordList.append(["querer","quiero","quieres","quiere","queremos","queréis","quieren"])
wordList.append(["poder","puedo","puedes","puede","podemos","podéis","pueden"])
wordList.append(["servir","sirvo","sirves","sirve","servimos","servís","sirven"])
wordList.append(["vengo","vienes","viene","vinimos","venís","vienen"])
wordList.append(["decir","digo","dices","dice","decimos","decís","dicen"])
wordList.append(["dar","doy","das","da","damos","dais","dan"])
wordList.append(["oír","oigo","oyes","oye","oímos","oís","oyen"])
wordList.append(["ver","veo","ves","ve","vemos","veis","ven"])
wordList.append(["hacer","hago","haces","hace","hacemos","hacéis","hacen"])
wordList.append(["pongo","pones","pone","ponemos","ponéis","ponen"])
#----------------------------------------------------------------以下規則動詞
wordList.append(["estudiar","estudio","estudias","estudia","estudiamos","estudiáis","estudian"])
wordList.append(["tomar","tomo","tomas","toma","tomamos","tomáis","toman"])
wordList.append(["hablar","hablo","hablas","habla","hablamos","habláis","hablan"])
wordList.append(["comer","como","comes","come","comemos","coméis","comen"])
wordList.append(["vivir","vivo","vives","vive","vivimos","vivís","viven"])
wordList.append(["vender","vendo","vendes","vende","vendemos","vendéis","venden"])
wordList.append(["abrir","abro","abres","abre","abrimos","abrís","abren"])
wordList.append(["aprender","aprendo","aprendes","aprende","aprendemos","aprendéis","aprenden"])
wordList.append(["entrar","entraro","entras","entra","entramos","entráis","entran"])
wordList.append(["mirar","miro","miras","mira","miramos","miráis","miran"])
wordList.append(["lavar","lavo","lavas","lava","lavamos","laváis","lavan"])
wordList.append(["gustar","gusto","gustas","gusta","gustamos","gustáis","gustan"])
wordList.append(["llamar","llamo","llamas","llama","llamamos","llamáis","llaman"])
wordList.append(["usar","uso","usas","usa","usamos","usáis","usan"])
wordList.append(["leer","leo","lees","lee","leemos","leéis","leen"])
wordList.append(["correr","corro","corres","corre","corremos","corréis","corren"])
wordList.append(["permitir","permito","permites","permite","permitimos","permitís","permiten"])
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

