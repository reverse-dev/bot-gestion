import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="+", intents=intents)

intents.message_content=True
intents.members=True

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot connecté...")
    print("Commandes syncronisée...")
    print("Good")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def lock(ctx):
    embed = discord.Embed(title="Verrouillage du canal", description="Le canal est maintenant verrouillé.", color=0x314fb0)
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_roles=True)
async def unlock(ctx):
    embed = discord.Embed(title="Déverrouillage du canal", description="Le canal est maintenant déverrouillé.", color=0x314fb0)
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def user_info(ctx, user: discord.User):
    embed = discord.Embed(title=f"Informations sur {user.name}", description=f"ID: {user.id}\nRôle(s): {', '.join([role.name for role in user.roles])}", color=0x314fb0)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def role_info(ctx, role: discord.Role):
    embed = discord.Embed(title=f"Informations sur le rôle {role.name}", description=f"ID: {role.id}\nPermissions: {', '.join([perm.name for perm in role.permissions])}", color=0x314fb0)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def ban(ctx, user: discord.User, reason: str):
    await user.ban(reason=reason)
    embed = discord.Embed(title="Ban", description=f"{user.name} a été banni pour la raison: {reason}", color=0x314fb0)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def unban(ctx, user_id: int, reason: str):
    user = await bot.fetch_user(user_id)
    await user.unban(reason=reason)
    embed = discord.Embed(title="Unban", description=f"{user.name} a été débanni pour la raison: {reason}", color=0x314fb0)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def kick(ctx, user: discord.User, reason: str):
    await user.kick(reason=reason)
    embed = discord.Embed(title="Kick", description=f"{user.name} a été kické pour la raison: {reason}", color=0x314fb0)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_roles=True)
async def set_role(ctx, user: discord.User, role: discord.Role):
    await user.add_roles(role)
    embed = discord.Embed(title="Rôle ajouté", description=f"{user.name} a été ajouté au rôle {role.name}", color=0x314fb0)
    await ctx.send(embed=embed)


bot.run("MTMwMjA0NTYzNTgyMTk2NTM5NQ.GJlLDE.aGsoGgP4pArV25UoPhdg-3WpwiuWqHt0z---To")
