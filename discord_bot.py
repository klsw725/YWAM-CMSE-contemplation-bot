import discord
import asyncio
import crawl_rss as cr
from tokens import Token

client = discord.Client()

token = Token.discord_token

async def my_background_task():
    await client.wait_until_ready()

    channel = client.get_channel(Token.discord_channel)
    await channel.send(cr.messageFormat())
    while not client.is_closed():
      print("I will die")
      await client.close()
    
        
        # await asyncio.sleep(60) # task runs every 60 seconds

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(my_background_task())
client.run(token)

