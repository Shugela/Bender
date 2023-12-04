import discord
from discord import app_commands

class gameDropdown(discord.ui.Select):
    
    def __init__(self):
        options = [
            discord.SelectOption(label="Don't Tap It!", description="test")
        ]
        super().__init__(
            placeholder='Select the game you want to play!',
            options=options
        )

        async def callback(self, interaction):
            await interaction.response.send_message("Don't tap It!") # will send the link to the user


class GamesView(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.add_item(gameDropdown())