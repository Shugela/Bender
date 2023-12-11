import discord
from discord import app_commands
import requests
import json

class gameDropdown(discord.ui.Select):
    
    def __init__(self):
        options = [
            discord.SelectOption(label="Don't Tap It!", description="Click on the black squares as quick as you can to get the maximum amount of points !")
        ]
        super().__init__(   
            placeholder='Select the game you want to play!',
            options=options,
            min_values=1,
            max_values=1
        )
    async def callback(self, interaction):
        # POST data to server
        url = 'http://127.0.0.1:5000/donttapit'
        data =  {'game': 'donttypeit'}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, 
                                 json=data,
                                 headers=headers)

        # Response URL from server
        print(response.status_code)
        print(response.text)
        print(response.json()['url'])
        url = response.json()['url']

        await interaction.response.send_message(url) # will send the link to the users

class GamesView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=60)
        self.add_item(gameDropdown())
    
   