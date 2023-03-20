while True:
    searchingVenue = venueList[count%len(venueList)]
    # print(searchingVenue)
    try:
        x, y = pyautogui.locateCenterOnScreen(v.screenshotPath+searchingVenue, region = (715,0,1100,1440), confidence=0.8)
        if x is not None:
            v.status+=1
            venue = searchingVenue.replace("venue_", "")
            venue = venue[:int(venue.find('.'))]
            if v.status%2 ==0:
                v.stateReport(1,f'found {venue}')
                v.selectAgent(preference, venue, agentXYposition)
            else:
                v.stateReport(1,f'exiting {venue}')
                while True:
                    try:
                        x = pyautogui.locateCenterOnScreen(v.screenshotPath+searchingVenue, region = (0,0,2500,1440), confidence=0.85)
                        if x is None:
                            v.stateReport(0,f'REqueuing')
                            break
                    except:
                        pass
    except:
        count+=1
    x= v.tryAndSearch('inGame.png')
    if x is not None:
        click()
        time.sleep(0.5)
        click()
        time.sleep(0.5)
        click()
        time.sleep(0.25)
        click()
        v.stateReport(5, 'in game, have fun.')
        return
    else:
        pass