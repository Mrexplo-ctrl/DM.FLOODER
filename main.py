#Fatto da saalamon
#Questa modalità è solo per EDUCAZIONE
#Trovi l'ultima versione a 
import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.(all)

async def start_bot(token)
   bot = commands.Bot(command_prefix='!', intents=intents)

   @bot.event
   async def on_ready():
       print(f'{bot.user} è online!')

   @bot.command()
   async def dm(ctx, user_id: int, *, message):
       user = bot.get_user(user_id)
       if user
          await ctx.send(f"Quante volte vuoi mandare il messaggio a {user}?")

          def check(m):
              return m.author == ctx.author and m.channel == ctx.channel and m.content.isdigi

          try:
            response = await bot.wait_for('message', check=check, timeout=30)
            message_count = int(response.content)

            for _ in range(message_count):
                await user.send(message)

            await ctx.send(f'Successo!Inviati {message_count} messaggi a {user}!")

          except asyncio.TimeoutError
              await ctx.send("Non hai risposto in tempo il comando si è cancellato coglione.")

      else:
          await ctx.send("User non trovato")

  await bot.start(token)
  
async def main():
    with open ('tokens.txt', 'r') as file:
        tokens = file.readlines(=

    tokens = [token.strip() for token in tokens if token.strip()]

    await asyncio.gather(*(start_bot(token) for token in tokens

if __name__ == "__main__":
    asyncio.run(main())

