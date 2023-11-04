agentList = ['fade','deadlock','iso','astra','breach','brimstone','chamber',
                    'cypher','gekko','jett','kayo','killjoy',
                    'neon','omen','phoenix','raze','reyna','sage',
                    'skye','sova','viper','yoru','harbor']
columns_position = ["123","2","33","44","55","66","77","88","99"]
rows_position = ["123","2","33"]
def getAgentCoordinates(agentList):
    rows = 3
    columns = 9
    agentList.sort()
    selectedAgent = list()
    for agentName in agentList:
        iIndex = agentList.index(agentName)
        # Calculate the row and column
        row = (iIndex) // columns
        column = (iIndex) % columns
        if (row > rows):
            print('something went wrong')
            exit()
        Xposition = rows_position[row]
        Yposition = columns_position[column]
        selectedAgent.append({'Agent': agentName, 'Xposition':Xposition,'Yposition':Yposition})
    """ example {'Date': '20230709', 'Account': 'FatherSun', 'Agent': 'astra', 'Xposition': '710', 'Yposition': '1233'}"""
    print(selectedAgent)
print(len(agentList))
getAgentCoordinates(agentList)