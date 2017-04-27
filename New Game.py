import random

import gspread

from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('Sheets_access.json', scope)
client = gspread.authorize(creds)

shFLFL = client.open('Falafel_Sheet')

wsChat = shFLFL.worksheet("Chat")

wsPlayers = shFLFL.worksheet("Players_&_Stats")

wsTurns = shFLFL.worksheet("Turns")



def NewGame(gameTitle, joinKey, Gamemode):

    # May implement new gamemodes in the future

    shFLFL.add_worksheet(gameTitle, 50, 100)

    tF = ShFLFL.worksheet(gameTitle)
    
    # formating the worksheet

    tF.update_cell(1, 1, "Name")
    tF.update_cell(1, 2, "Strength")
    tF.update_cell(1, 3, "Agility")
    tF.update_cell(1, 4, "Perception")
    tF.update_cell(1, 5, "Chakra")
    tF.update_cell(1, 6, "HP")
    
    # Affinity 1 is most like or most affinity for
    
    tF.update_cell(1, 8, "Affinity 1")
    tF.update_cell(1, 9, "Affinity 2")
    tF.update_cell(1, 10, "Affinity 3")
    tF.update_cell(1, 11, "Affinity 4")
    tF.update_cell(1, 12, "Affinity 5")
    
    tF.update_cell(1, 14, "Password")

    tF.update_cell(50, 100, joinKey)

    
    return shFLFL.worksheet(gameTitle)
    # returns the nameof the created game
