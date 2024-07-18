import discord
from bot_logic import gen_pass

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
@bot.command()
async def hello(ctx):
    await ctx.send(f'hii')
@bot.command()
async def bye(ctx):
    await ctx.send(f'goodbye')
@bot.command()
async def password(ctx):
    await ctx.send(f"Твой пароль " + gen_pass(10))
@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)


bot.run("")
