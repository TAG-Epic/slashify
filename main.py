from discord.ext.commands import Bot
from slashify import Slashify, Choices, Optional
from discord import Role
from color_format import basicConfig
from logging import getLogger, DEBUG

basicConfig(getLogger())
getLogger("slashify").setLevel(DEBUG)

bot = Bot("h")
slashify = Slashify(bot)


@bot.command()
async def test(ctx, text, role: Role, choices: Choices(((1, 1), (2, 2)), int), optional: Optional(str) = None):
    await ctx.send(f"Yo this works btw!\nText: {text}\nRole: {role}\nChoices: {choices}\nOptional: {optional}")


@bot.command()
async def roletest(ctx, role: Role):
    await ctx.send(role.id)


@bot.command()
async def yes(ctx):
    await ctx.send(ctx.command)


bot.run("Nzg5OTAwMTc5MDY3MjQwNDQ4.X94x3g.iLyL5883yQMZA3eqGW2T8iuTLDU")
