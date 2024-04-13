from selectAgent import v
def system_preference():
    v.preference = {
        'pearl': ['harbor','phoenix','breach'],
        'breeze':['viper','phoenix','breach'],
        'ascent':['omen','phoenix','breach'],
        'sunset':['omen','phoenix','breach'],
        'haven': ['omen','phoenix','breach'], 
        'lotus': ['omen','phoenix','breach'],
        'split': ['omen','phoenix','breach' ],
        'bind': ['omen','phoenix','breach'],
        'icebox': ['omen','phoenix','breach'], 
        'fracture': ['omen','breach','omen']
    }
    v.preference = {
        'breeze':['neon','phoenix','breach'],
        'ascent':['raze','phoenix','breach'],
        'sunset':['pheonix','phoenix','breach'],
        'haven': ['pheonix','phoenix','breach'], 
        'lotus': ['pheonix','phoenix','breach'],
        'split': ['pheonix','phoenix','breach' ],
        'bind': ['pheonix','phoenix','breach'],
        'icebox': ['omen','phoenix','breach'], 
        'pearl': ['harbor','phoenix','breach'],
        'fracture': ['omen','breach','omen']
    }
    v.preference = {
        'breeze':['neon','phoenix','breach'],
        'ascent':['yoru','phoenix','breach'],
        'sunset':['yoru','phoenix','breach'],
        'haven': ['yoru','phoenix','breach'], 
        'lotus': ['yoru','phoenix','breach'],
        'split': ['yoru','phoenix','breach' ],
        'bind': ['yoru','phoenix','breach'],
        'icebox': ['omen','phoenix','breach'], 
        'pearl': ['harbor','phoenix','breach'],
        'fracture': ['omen','breach','omen']
    }
    """  """
    v.preference = ['chamber', 'omen', 'phoenix']
    v.preference = ['raze', 'reyna', 'phoenix']
    v.preference = ['brimstone', 'sage', 'phoenix']
    v.preference = ['gekko', 'phoenix', 'jett']  
    v.preference = ['jett', 'reyna', 'phoenix']
    v.preference = ['omen', 'sage', 'jett']
    v.preference = ['skye', 'jett', 'phoenix']
    v.preference = ['reyna', 'jett', 'phoenix']
    v.preference = ['gekko', 'yoru', 'omen']
    v.preference = ['phoenix', 'jett', 'sage'] #basic
    v.preference = ['yoru', 'gekko', 'omen']
    v.preference = ['iso', 'yoru', 'jett']
    v.preference = ['sage', 'phoenix', 'omen']
    """  """
    v.account = v.wonna6
    v.account = v.wonna7
    v.account = v.wonna
    v.account = v.wonna3
    v.account = v.wonna5
    v.account = v.wonna4
    """  """
    v.game_mode = 'swiftplay'
    v.game_mode = 'spike_rush' 
    v.game_mode = 'unrated' 
    v.game_mode = 'competitive'
    """"""
if __name__ == "__main__":
    v = v()
    # afk(drop=0,shield=0,abilties=1)
    # testing()
    system_preference()
    v.hold()