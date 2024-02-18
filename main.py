import os, time, random, sys, json
import discord
import json
from colorama import Fore, init
import datetime
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System 
from functools import wraps
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System 
from discord.ext.commands import Bot
from discord.ext import commands
import requests
import logging





intents = discord.Intents.default()
intents.members = True
bot = discord.Bot()
settings = json.load(open("settings.json", encoding="utf-8"))
status = settings["status"]

class LoggingFormatter(logging.Formatter):
    # Colors
    black = "\x1b[30m"
    red = "\x1b[31m"
    green = "\x1b[32m"
    yellow = "\x1b[33m"
    blue = "\x1b[34m"
    gray = "\x1b[38m"
    # Styles
    reset = "\x1b[0m"
    bold = "\x1b[1m"

    COLORS = {
        logging.DEBUG: gray + bold,
        logging.INFO: blue + bold,
        logging.WARNING: yellow + bold,
        logging.ERROR: red,
        logging.CRITICAL: red + bold,
    }

    def format(self, record):
        log_color = self.COLORS[record.levelno]
        format = "(black){asctime}(reset) (levelcolor){levelname:<8}(reset)(green){name} (reset){message}"
        format = format.replace("(black)", self.black + self.bold)
        format = format.replace("(reset)", self.reset)
        format = format.replace("(levelcolor)", log_color)
        format = format.replace("(green)", self.green + self.bold)
        formatter = logging.Formatter(format, "%Y-%m-%d %H:%M:%S", style="{")
        return formatter.format(record)


logger = logging.getLogger("[+]")
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(LoggingFormatter())
# File handler
file_handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
file_handler_formatter = logging.Formatter(
    "[{asctime}] [{levelname:<8}]", "%Y-%m-%d %H:%M:%S", style="{"
)
file_handler.setFormatter(file_handler_formatter)

# Add the handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)
bot.logger = logger

        


@bot.event
async def on_ready() -> None:
    bot.logger.info(f"Logged in as {bot.user.name}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{status}"))


### BTC PAY
class MobileCopybtc(discord.ui.View):
    def __init__(self, link: str):
        super().__init__()
        link = "https://chart.googleapis.com/chart?chs=300x300&cht=qr&chl=bitcoin:"
        self.add_item(discord.ui.Button(label="QR Code", url=link))

    @discord.ui.button(label="📱 Mobile Copy", style=discord.ButtonStyle.blurple)
    async def Mobilecopylite(self, button: discord.ui.Button, interacton: discord.Interaction, ):
        await interacton.response.send_message("", ephemeral=True)

@bot.command(description="Use this to send user an invoice paying with Bitcoin")
@commands.has_role('queue perms')
async def paybtc(ctx, price):

        link = "https://chart.googleapis.com/chart?chs=300x300&cht=qr&chl=bitcoin:"
        embed=discord.Embed(title=f"Bitcoin Payment", description=F"", color=0x4598d2)
        embed.add_field(name=f"**Seller**: ", value=f"<@{ctx.author.id}>", inline=False)
        embed.add_field(name=f"**Amount**: ", value=f"${price}", inline=False)
        embed.add_field(name=f"**BTC Wallet**: ", value=" ", inline=False)
        embed.set_image(url="")
        await ctx.respond(embed=embed, view=MobileCopybtc(str(link)))
        
### LTC PAY
class MobileCopylite(discord.ui.View):
    def __init__(self, link: str):
        super().__init__()
        link = "https://chart.googleapis.com/chart?chs=300x300&cht=qr&chl=litecoin:"
        self.add_item(discord.ui.Button(label="QR Code", url=link))

    @discord.ui.button(label="📱 Mobile Copy", style=discord.ButtonStyle.blurple)
    async def Mobilecopylite(self, button: discord.ui.Button, interacton: discord.Interaction, ):
        await interacton.response.send_message("", ephemeral=True)


@bot.command(description="Use this to send user an invoice paying with litecoin")
@commands.has_role('queue perms')
async def payltc(ctx, price):
        
        link = "https://chart.googleapis.com/chart?chs=300x300&cht=qr&chl=litecoin:"
        embed=discord.Embed(title=f"Litecoin Payment", description=F"", color=0x4598d2)
        embed.add_field(name=f"**Seller**: ", value=f"<@{ctx.author.id}>", inline=False)
        embed.add_field(name=f"**Amount**: ", value=f"${price}", inline=False)
        embed.add_field(name=f"**LTC Wallet**: ", value="", inline=False)
        embed.set_image(url="")
        await ctx.respond(embed=embed, view=MobileCopylite(str(link)))


### ETH PAY
class MobileCopyETH(discord.ui.View):
    def __init__(self, link: str):
        super().__init__()
        link = "https://chart.googleapis.com/chart?chs=300x300&cht=qr&chl=ethereum:"
        self.add_item(discord.ui.Button(label="QR Code", url=link))

    @discord.ui.button(label="📱 Mobile Copy", style=discord.ButtonStyle.blurple)
    async def Mobilecopylite(self, button: discord.ui.Button, interacton: discord.Interaction, ):
        await interacton.response.send_message("", ephemeral=True)


@bot.command(description="Use this to send user an invoice paying with Ethereum")
@commands.has_role('queue perms')
async def payeth(ctx, price):
        
        link = "https://chart.googleapis.com/chart?chs=300x300&cht=qr&chl=Ethereum:"
        embed=discord.Embed(title=f"Ethereum Payment", description=F"", color=0x4598d2)
        embed.add_field(name=f"**Seller**: ", value=f"<@{ctx.author.id}>", inline=False)
        embed.add_field(name=f"**Amount**: ", value=f"${price}", inline=False)
        embed.add_field(name=f"**ETH Wallet**: ", value="", inline=False)
        embed.set_image(url="")
        await ctx.respond(embed=embed, view=MobileCopyETH(str(link)))

### PAYPAL PAY
class MobileCopyPaypal(discord.ui.View):
    def __init__(self, link: str):
        super().__init__()
        link = "https://www.paypal.com/paypalme/"
        self.add_item(discord.ui.Button(label="Paypal Link", url=link))

    @discord.ui.button(label="📱 Mobile Copy", style=discord.ButtonStyle.blurple)
    async def MobileCopylite(self, button: discord.ui.Button, interacton: discord.Interaction, ):
        await interacton.response.send_message("", ephemeral=True)


@bot.command(description="Use this to send user an invoice paying with Paypal")
@commands.has_role('queue perms')
async def paypaypal(ctx, price):
        
        link = "https://www.paypal.com/paypalme/"
        embed=discord.Embed(title=f"Paypal Payment", description=F"", color=0x4598d2)
        embed.add_field(name=f"**Seller**: ", value=f"<@{ctx.author.id}>", inline=False)
        embed.add_field(name=f"**Amount**: ", value=f"${price}", inline=False)
        embed.add_field(name=f"**Link**: ", value="https://www.paypal.com/paypalme/", inline=False)
        embed.set_image(url="")
        await ctx.respond(embed=embed, view=MobileCopyPaypal(str(link)))

### CASHAPP PAY
class MobileCopyCASH(discord.ui.View):
    def __init__(self, link: str):
        super().__init__()
        link = "https://cash.app/£caidencl"
        self.add_item(discord.ui.Button(label="Cashapp Link", url=link))

    @discord.ui.button(label="📱 Mobile Copy", style=discord.ButtonStyle.blurple)
    async def Mobilecopylite(self, button: discord.ui.Button, interacton: discord.Interaction, ):
        await interacton.response.send_message("£caidencl", ephemeral=True)


@bot.command(description="Use this to send user an invoice paying with Cashapp")
async def paycashapp(ctx, price):
        
        link = "https://cash.app/£caidencl"
        embed=discord.Embed(title=f"Cashapp Payment", description=F"", color=0x0000ff)
        embed.add_field(name=f"**Seller**: ", value=f"<@{ctx.author.id}>", inline=False)
        embed.add_field(name=f"**Amount**: ", value=f"${price}", inline=False)
        embed.add_field(name=f"**CashTag**: ", value="£caidencl", inline=False)
        embed.set_image(url="")
        await ctx.respond(embed=embed, view=MobileCopyCASH(str(link)))

@bot.command(description="This is a help menu")
async def help(ctx):
        
        embed=discord.Embed(title=f"Industry Markets Support Menu", description=F"", color=0x4598d2)
        embed.add_field(name=f"**/paycashapp**: ", value="``allows you to show a cashapp payment``", inline=False)
        embed.add_field(name=f"**/payeth**: ", value=f"``allows you to show a ethereum payment``", inline=False)
        embed.add_field(name=f"**/payltc**: ", value=f"``allows you to show a litecoin payment``", inline=False)
        embed.add_field(name=f"**/paybtc**: ", value="``allows you to show a bitcoin payment``", inline=False)
        embed.add_field(name=f"**/paypaypal**: ", value="``allows you to show a paypal payment``", inline=False)
        embed.set_image(url="")
        await ctx.respond(embed=embed)

bot.run(settings["botToken"])
