import discord
from discord.ext import commands
import time

intents = discord.Intents.default()
intents.message_content = True
ids = []
bot = commands.Bot(command_prefix='.kako.', intents=intents)

f = open(r"discord ids.txt")

for line in f:
    strippedLine = line.strip()
    print(strippedLine)
    ids.append(strippedLine[-19:-1])
print(ids)


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print(f'{message.author} in the discord {message.guild} in channel {message.channel} :{message.content}')
        # print(message.content)
        prefix = ".kako."
        if '<@152170780006940672>' in message.content:  # dont ping me
            if str(message.author.id) != '1012376097855373414':
                await message.channel.send(f"pong <@!{message.author.id}>")  # <@!id>

        if message.content.startswith(prefix):
            command = message.content[len(prefix):]
            is_admin = [role.name == 'Outfit Wars Leader' or role.name == 'Outfit Wars Orga' or role.name == 'admin' for
                        role in message.author.roles]  # admin roles

            if command == 'help':
                await message.channel.send("'''\n"
                                           "Commands:\n"
                                           "help- this help message\n"
                                           "stats- this is the stats message\n"
                                           "'''")
            if command[0:4] == 'ping':
                details = command[4:-1:]
                print(message.author.id)
                if command == 'ping <@152170780006940672>':  # dont ping me with command
                    await message.channel.send(f'nonono')
                else:
                    await message.channel.send(f"pong {details}>")  # <@!id>, pong u back

            if command == 'stats':
                if True in is_admin:
                    await message.channel.send("stats")
                else:
                    await message.channel.send("no stats for u")

            if command[0:2] == 'dm':
                if True in is_admin:
                    msg = command[3:]
                    for user_id in ids:
                        user = await client.fetch_user(int(user_id))
                        user_name = user.name
                        # await user.send(f'Hey {user_name},
                        # Outfit Wars matches are starting soon, would be great if u can
                        # make sure the server Euphoria Discovered isnt muted so you know when signups are there!\n'
                        #     f'We know we ping a shit ton but we really need you to be there for us :)')
                        time.sleep(3)
                        await user.send(f'Hey {user_name}\n'
                                        f'' + msg)
                else:
                    await message.channel.send("ur not an admin")
            # else:
            #     await message.channel.send("this command doesnt exist")


client = MyClient(intents=intents)
client.run('My_Token')
