# bot.py
import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('MTA0MTM5ODg1NDg0NDY4MjM3Mg.GcQrXN.b1DQYy01JnKN2wVEjJ1JLJ2OSbi6dBD2WQBeDs')
y = "YOU ARE A LOSER. I DO MORE THINGS IN A DAY THAN WHAT YOU DO IN A LIFETIME. I HAVE WARNED YOU. YOU ARE A GOOD FOR NOTHING LOSER WITH 5 CENTS IN YOUR POCKET. YOU ARE A WAGIE AND GET CONTROLLED BY THE GOVERNMENT. YOU BLIND YOU DONT SEE THE POWER OF SOCAIL MEDIA AND YOUR LITTLE TOYS. GET RID OF YOUR BROKIE SELF AND GET A BUGGATTI. i DONT CARE WHAT YOU ARE FIX YOURSELF. CONVERT TO CHRISTANITY AND BECOME RELIGOUS. FEAR GOD. DONT BE A LOSER. I DONT CARE WHAT YOU HAVE TO SAY. ALL I KNOW IS THAT YOU HAVE 0 LIFE, 0 CARS, 0 HOUSES, 0 THINGS. ALL YOU HAVE IS USELESS THINGS YOU WILL NEVER NEED. "
intents = discord.Intents.default()
intents.message_content=True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Breathe Air',
        'Brokie',
        'Wagie',
        '@AdinRoss',
        '@SNEAKO',
        'What Color is YOUR BUGATTI'
        
    ]

    if message.content == '.fix me':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    if message.content == '.ping':
      await message.channel.send('pong')
    if message.content == '.howsyourday':
      await message.channel.send('busy')
    if message.content == '.yell':
      await message.channel.send(y)
    if message.content == '.vape':
      await message.channel.send('BREATHE AIR')
    if message.content == '.color':
      await message.channel.send('BRONZE GOLD')
    if message.content == '.bugatti':
      await message.channel.send('GET ONE YOU BROKIE')
    if message.content == '.topG':
      await message.channel.send('I AM THE TOP G ')
    if message.content == 'hi':
      await message.channel.send('get a life')
      


      
client.run('MTA0MTM5ODg1NDg0NDY4MjM3Mg.Gs4KXi.r6A17WoxDvJgidOahYlNuDyGHQkq0mA_TpPSIA')
