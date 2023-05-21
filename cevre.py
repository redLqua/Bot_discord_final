import discord
from discord.ext import commands

from kirlilik_fonksiyonlari import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def cop(ctx, arg1):
    await ctx.send(cop_ayristirma(arg1))


bot.run('TOKEN BURAYA GELCEK')




def cop_ayristirma(cop_turu):
    geri_donusebilen = ['kağıt', 'plastik şişe', 'karton','şişe kapağı','gazeteler']
    geri_donusemeyen = ['Strafor Köpük', 'Çeşitli Cam Ürünler', 'plastik poşetler','Floresan Lambalar','Oyuncaklar']
    

    
    if cop_turu.lower() in geri_donusebilen:
        return 'Geri donusebilen'
    elif cop_turu.lower() in geri_donusemeyen:
        return 'Geri donusemeyen'
    else:
        return 'Bilemedim \U0001F92F'
