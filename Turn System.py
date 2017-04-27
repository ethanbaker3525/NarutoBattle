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



def TCycle(ListPlayers):

    PlayerCords = {}

    for a in ListPlayers:

# This ListPlayers is intended to be a list of all player names in this battle
# ListCords is their rows

        playerCell = wsPlayers.find(a)
        PlayerCords[ListPlayers[a]] = playerCell.row

    
