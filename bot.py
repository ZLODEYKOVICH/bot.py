import disnake
from disnake.ext import commands
from config import *

bot = commands.Bot(command_prefix='!', help_command=None, intents=disnake.Intents.all(),
                   test_guilds=[905692269225603073])


@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready")


@bot.event
async def on_member_join(member):
    role = disnake.utils.get(member.guild.roles, id=1097453450603802644)
    channel = member.guild.system_channel

    embed = disnake.Embed(
        title="Свежее мясо!",
        description=f"{member.name}, скоро ты пожалеешь о своём присутствии!",
        color=0xffffff
    )

    await member.add_roles(role)
    await channel.send(embed=embed)


@bot.event
async def on_message(message):
    await bot.process_commands(message)

    for content in message.content.split():
        for censored_word in CENSORED_WORDS:
            if content.lower() == censored_word:
                await message.channel.send(f"{message.author.mention}, за языком следи!")
                await message.delete()


@bot.command()
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member: disnake.Member, *, reason="Вас кикнули по причине БЫДЛО."):
    await ctx.send(f"Пшёл отсюда {member.mention}")
    await member.kick(reason=reason)


@bot.command()
@commands.has_permissions(kick_members=True, administrator=True)
async def ban(ctx, member: disnake.Member, *, reason="Вас кикнули по причине БЫДЛО."):
    await ctx.send(f"Так тебе и надо {member.mention}")
    await member.ban(reason=reason)


bot.run(TOKEN)
