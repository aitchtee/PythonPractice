'''
На этот раз вам известно число выборщиков от каждого штата США и
результаты голосования каждого гражданина США (а также в каком штате проживает этот гражданин)
Вам необходимо подвести результаты голосования: сначала определить результаты голосования в каждом штате и определить,
за какого из кандидатов отданы голоса выборщиков данного штата.
Далее необходимо подвести резултаты голосования выборщиков по всем штатам.
'''


def get_key(dictionary, val):
    for key, value in dictionary.items():
        if val == value:
            return key


f = open('second.txt')
stateNum = f.readline()
stateVoicesDict = {}
statesVoteCountDict = {}
for i in range(int(stateNum)):
    line = f.readline()
    stateVoicesDict[line.split()[0]] = line.split()[1]
    statesVoteCountDict[line.split()[0]] = {}
votes = f.readlines()
f.close()

# делаем красиво
newVotes = []
for vote in votes:
    newVotes.append(vote.rstrip())
del votes

# словарь штат и его кандидаты и их кол-во голосов
for line in newVotes:
    if line.split()[1] not in statesVoteCountDict[line.split()[0]]:
        statesVoteCountDict[line.split()[0]][line.split()[1]] = 0
# print('old', statesVoteCountDict)

# обновляем словарь. записываем кол-во голосов каждого кандидата в штате
for line in newVotes:
    statesVoteCountDict[line.split()[0]][line.split()[1]] += 1
print('new', statesVoteCountDict)

# переопределяем значение для штата именем победителя
valDict = statesVoteCountDict.values()
keyDict = statesVoteCountDict.keys()

# сортировка словаря и поиск кандидата, набравшего наибольшее кол-во очков
for i in range(len(list(valDict))):
    sortedList = list(list(valDict)[i].keys())
    sorD = {}
    for j in range(len(sortedList)):
        sorD[sorted(sortedList, reverse=True)[j]] = list(valDict)[i].get(sorted(sortedList, reverse=True)[j])
    winner = max(list(sorD.values()))
    statesVoteCountDict[list(statesVoteCountDict.keys())[i]] = get_key(sorD, winner)
# print('res', statesVoteCountDict)

# подсчет результата
resDict = {}
for i in range(int(stateNum)):
    if not list(statesVoteCountDict.values())[i] in resDict:
        curState = list(statesVoteCountDict.keys())[i]
        voices = stateVoicesDict[curState]
        resDict[list(statesVoteCountDict.values())[i]] = voices
    else:
        curState = list(statesVoteCountDict.keys())[i]
        voices = stateVoicesDict[curState]
        resDict[list(statesVoteCountDict.values())[i]] = int(resDict.get(list(statesVoteCountDict.values())[i])) + int(voices)
print(resDict)
