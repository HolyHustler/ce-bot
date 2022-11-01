from http.client import responses
import discord
from discord import app_commands
import random
import os
import json
from discord.ui import select, View
from discord.ext import commands, tasks
from discord.utils import get
from typing import Optional
import pytube

from os import environ as env
from dotenv import load_dotenv
load_dotenv()

bot_channel = 1020963659658309705
connexion_channel = 1018992700059566090
globalstatut = "online"
# maintenance, online
listemessagespresence = ('les exécutions du jour.', 'les délibérations du Comité.','un jugement du DJI.', 'le conseil O5.', "le Site-Resh.")

# https://www.youtube.com/c/Digiwind/videos
# https://cog-creators.github.io/discord-embed-sandbox/


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False #we use this so the bot doesn't sync commands more than once
        self.added = False
        

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced 
            await tree.sync() #guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
        
        custompresence.start()
        if globalstatut == "maintenance":
            print("Mode maintenance activé.")
            await client.change_presence(status=discord.Status.idle)
            await client.change_presence(activity=discord.Game(name="être en mode maintenance."))
        else:
            print("Mode production activé.")
            await client.change_presence(status=discord.Status.online)
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(listemessagespresence)))

        print(f"{client.user} est connecté aux serveurs suivants :")
        for guild in client.guilds:
        	print(f"{guild.name}(id: {guild.id})")


client = aclient()
tree = app_commands.CommandTree(client)





@tasks.loop(hours=2)
async def custompresence():
    messagepresence = random.choice(listemessagespresence)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=messagepresence))




@tree.command(name = 'histoire', description='Une petite histoire éthique rien que pour vous.') #guild specific slash command
async def histoire(interaction: discord.Interaction, membre: Optional[discord.Member]):
    if interaction.channel.id == bot_channel  :
        complement1 = ("fait un pot de départ à la retraite", "vole des M&Ms", "réalise son examen obligatoire de la prostate", "bluffe au poker avec une paire de 6 et gagne contre un full", "se fait traiter de feignant", "se demande si la direction d site n'est pas composée d'oligarques", "dénonce le manque d'éthique du Pr. Driessen", "apprend l'histoire de la Shoah à SCP-2006-US", "fait un barbecue avec la tesla", "se plaint du grand remplacement du site", "fait de l'exorcisation", "réalise une action pas très éthique", "se plaint du salaire", "trébuche", "fait une patrouille", "part en expérience", "se fait Agrougrou", "donne des bonbons", "maltraite des enfants", "fait une blackface", "se fait tabasser", "mange un sandwich", "maltraite un mouton", "fait un entretien psychologique avec le Dr. Keller", "s'inscrit sur pôle emploi", "pose des parpaings", "boit de l'eau de javel", "mange un sandwich", "cache un pouf de SCP-999-US", "se fait violenter", "joue aux échecs", "se fait juger par le DJI", "fait de la contrebande")
        complement2 = ("dans le secteur des Classe-D", "dans le secteur de la sécurité", "dans l'enclos à mouton", "dans la salle de conférence en pleine réunion", "dans le vide-ordure", "dans la salle des torpilles d'un sous-marin", "dans les toilettes", "dans la dimension de 106", "dans le porte-hélictopère de la FIM Rhô-27", "dans l'antenne médicale", "dans la salle du dispatch", "dans le bureau du Dr. Keller", "dans une baignoire", "dans le confinement de SCP-062-FR", "dans le bureau du directeur", "dans une armoire", "dans une fourgonette douteuse")
        complement3 = ("avec la tendresse particulière", "sous l'oeil bienveillant", "avec les compliments", "sous les applaudissements", "avec l'admiration", "avec l'aide", "sous les yeux", "en compagnie")
        complement4 = ("d'un membre de la BRAI", "du Dr. Colbet", "d'un Classe-D", "d'un FIM de la Delta-4", "d'un membre du consil O5", "de la dynastie Varsard", "SCP-2006-US", "d'un mexicain", "d'une araignée géante avec un corps de sous-marin", "d'un membre de la Coalition Mondiale Occulte", "d'un inspecteur du Comité Éthique", "d'un membre du Département de la Sécurité Interne", "d'un membre de S.A.P.H.I.R.", "d'un membre de la Main du Serpent", "du Docteur Zemmour", "du vénérable Mr. Roberts", "du respectable Mr. Perkins", " de Dr. Oxana", "de SCP-062-FR", "du directeur", "du DJI")
        if membre == None:
            finalcomplement4 = random.choice(complement4)
        else :
            finalcomplement4 = "de __" + membre.name + "__"
        embed=discord.Embed(title="Histoire Random", description=f"{interaction.user.mention} {random.choice(complement1)} {random.choice(complement2)} {random.choice(complement3)} {finalcomplement4}.", color=0xffffff)
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message(f"Cette commande ne peut être effectué dans que dans le salon bots !", ephemeral = True)

@tree.command(name = 'liens-utiles', description='Touts les liens utiles de la communauté.') #guild specific slash command
async def liens_histoire(interaction: discord.Interaction):
    embed=discord.Embed(title="Liens Utiles", color=0xffffff)
    embed.set_author(name="Site-Resh", icon_url="http://resh.holyhustler.fr/reshblanc.png")
    embed.add_field(name="Connexion Rapide", value="steam://connect/GAME-FR-41.MTXSERV.COM:27100/", inline=False)
    embed.add_field(name="IP du Serveur", value="game-fr-41.mtxserv.com:27100", inline=False)
    embed.add_field(name="Collection", value="https://steamcommunity.com/sharedfiles/filedetails/?id=2646381163", inline=False)
    embed.add_field(name="Discord", value="https://discord.gg/EZYeAWfbTs", inline=True)
    embed.add_field(name="Discord RP", value="https://discord.gg/gvADGVQeTk", inline=True)
    embed.add_field(name="Règlement", value="https://docs.google.com/document/d/1n6CcD6jIeqwQGOVanZWAmid56mKSwAI574z15xsLkX4/edit?usp=sharing", inline=False)
    embed.add_field(name="Chaîne Youtube", value="https://www.youtube.com/channel/UCwU7pYUdpafj7gx8A_kBRlA", inline=False)
    embed.add_field(name="Top-Serveurs", value="https://top-serveurs.net/garrys-mod/vote/le-site-resh-site-sans-lendemain-serious-scp-rp", inline=False)
    embed.add_field(name="Documents RP", value="https://docs.google.com/spreadsheets/d/1-cp_hjLy81J9gWkCjPiAaWs-msWkM1m8bD5qEcGozws/edit?usp=sharing", inline=False)
    embed.add_field(name="Liste des SCP", value="https://docs.google.com/spreadsheets/d/1-cp_hjLy81J9gWkCjPiAaWs-msWkM1m8bD5qEcGozws/edit?usp=sharing", inline=False)
    await interaction.response.send_message(embed=embed) 

@tree.command(name = 'vote', description='Faire un petit vote.') #guild specific slash command
async def vote(interaction: discord.Interaction, string: str):  
    embed=discord.Embed(title="Vote Communautaire", description=string, color=0xffffff)
    embed.set_author(name=interaction.user.name)
    message_vote = await interaction.channel.send(embed=embed) 
    emoji = ['✅', '⬜', '❎']
    for i in emoji:
        await message_vote.add_reaction(i)
    await interaction.response.send_message(f"Le vote à bien été lancé !", ephemeral = True)


# https://stackoverflow.com/questions/65431266/how-to-create-a-rock-paper-scissors-command-in-discord-py
@tree.command(name = 'ciseaux', description='Jouer à pierre, papier, ciseaux.') #guild specific slash command
@app_commands.choices(choices=[
    app_commands.Choice(name="Pierre", value="pierre"),
    app_commands.Choice(name="Papier", value="papier"),
    app_commands.Choice(name="Ciseaux", value="ciseaux"),
])
async def ciseaux(interaction: discord.Interaction, choices: app_commands.Choice[str]):
    choix = ("pierre", "papier", "ciseaux")

    user_choice = choices.value
    comp_choice = random.choice(choix)
    if user_choice == 'pierre':
        if comp_choice == 'pierre':
            embed=discord.Embed(title="Pierre, papier, ciseaux ...", description="Well, that was weird. We tied.", color=0xffffff)
            embed.set_footer(text="Match Nul !")
        elif comp_choice == 'papier':
            embed=discord.Embed(title="Pierre, papier, ciseaux ...", description="Nice try, but I won that time!!", color=0xff0000)
            embed.set_footer(text="Tu as perdu !")
        elif comp_choice == 'ciseaux':
            embed=discord.Embed(title="Pierre, papier, ciseaux ...", description="Aw, you beat me. It won't happen again!", color=0x00ff11)
            embed.set_footer(text="Tu as gagné !")
        embed.add_field(name="Ton choix :", value=user_choice, inline=True)
        embed.add_field(name="Choix du Bot :", value=comp_choice, inline=True)
        await interaction.response.send_message(embed=embed)

    elif user_choice == 'papier':
        if comp_choice == 'pierre':
            embed=discord.Embed(title="Pierre, papier, ciseaux ...", description="The pen beats the sword? More like the paper beats the rock!!", color=0x00ff11)
            embed.set_footer(text="Tu as gagné !")
        elif comp_choice == 'papier':
            embed=discord.Embed(title="Pierre, papier, ciseaux ...", description="Oh, wacky. We just tied. I call a rematch!!", color=0xffffff)
            embed.set_footer(text="Match Nul !")
        elif comp_choice == 'ciseaux':
            embed=discord.Embed(title="Pierre, papier, ciseaux ...", description="Aw man, you actually managed to beat me.", color=0xff0000)
            embed.set_footer(text="Tu as perdu !")
        embed.add_field(name="Ton choix :", value=user_choice, inline=True)
        embed.add_field(name="Choix du Bot :", value=comp_choice, inline=True)
        await interaction.response.send_message(embed=embed)

    elif user_choice == 'ciseaux':
        if comp_choice == 'pierre':
            embed=discord.Embed(title="Pierre, papier, ciseaux ...", description="HAHA!! I JUST CRUSHED YOU!! I rock!!", color=0xff0000)
            embed.set_footer(text="Tu as perdu !")
        elif comp_choice == 'papier':
            embed=discord.Embed(title="Pierre, papier, ciseaux ...", description="Bruh. >:", color=0x00ff11)
            embed.set_footer(text="Tu as gagné !")
        elif comp_choice == 'ciseaux':
            embed=discord.Embed(title="Pierre, papier, ciseaux ...", description="Oh well, we tied.", color=0xffffff)
            embed.set_footer(text="Match Nul !")
        embed.add_field(name="Ton choix :", value=user_choice, inline=True)
        embed.add_field(name="Choix du Bot :", value=comp_choice, inline=True)
        await interaction.response.send_message(embed=embed)


class button_view_mention_joueur(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label = "Mention Joueur", custom_id = ("role_" + "Mention Joueur"), style = discord.ButtonStyle.green)
    async def role_mentionjoueur(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles,name="Mention Joueur")  
        if role not in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"Je t'ai donné le rôle : {role.mention} !", ephemeral = True)
        else: 
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Je t'ai retiré le rôle : {role.mention} !", ephemeral = True)

class button_view_departements(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label = "Département Adminsitratif", custom_id = ("role_" + "Département Adminsitratif"), style = discord.ButtonStyle.green)
    async def role_administratif(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles,name="Département Adminsitratif")  
        if role not in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"Je t'ai donné le rôle : {role.mention} !", ephemeral = True)
        else: 
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Je t'ai retiré le rôle : {role.mention} !", ephemeral = True)

    @discord.ui.button(label = "Département Scientifique", custom_id = ("role_" + "Département Scientifique"), style = discord.ButtonStyle.green)
    async def role_scientifique(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles,name="Département Scientifique")  
        if role not in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"Je t'ai donné le rôle : {role.mention} !", ephemeral = True)
        else: 
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Je t'ai retiré le rôle : {role.mention} !", ephemeral = True)

    @discord.ui.button(label = "Département Sécurité", custom_id = ("role_" + "Département Sécurité"), style = discord.ButtonStyle.green)
    async def role_securite(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles,name="Département Sécurité")  
        if role not in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"Je t'ai donné le rôle : {role.mention} !", ephemeral = True)
        else: 
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Je t'ai retiré le rôle : {role.mention} !", ephemeral = True)

    @discord.ui.button(label = "Département Médical", custom_id = ("role_" + "Département Médical"), style = discord.ButtonStyle.green)
    async def role_medical(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles,name="Département Médical")  
        if role not in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"Je t'ai donné le rôle : {role.mention} !", ephemeral = True)
        else: 
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Je t'ai retiré le rôle : {role.mention} !", ephemeral = True)

    @discord.ui.button(label = "Département DI&ST", custom_id = ("role_" + "Département DI&ST"), style = discord.ButtonStyle.green)
    async def role_dist(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles,name="Département DI&ST")  
        if role not in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"Je t'ai donné le rôle : {role.mention} !", ephemeral = True)
        else: 
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Je t'ai retiré le rôle : {role.mention} !", ephemeral = True)
    
    @discord.ui.button(label = "SCP", custom_id = ("role_" + "SCP"), style = discord.ButtonStyle.green)
    async def role_scp(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles,name="SCP")  
        if role not in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"Je t'ai donné le rôle : {role.mention} !", ephemeral = True)
        else: 
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Je t'ai retiré le rôle : {role.mention} !", ephemeral = True)

class button_view_gaming(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)
        
    @discord.ui.button(label = "Gaming", custom_id = ("role_" + "Gaming"), style = discord.ButtonStyle.grey)
    async def role_gaming(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles,name="Gaming")  
        if role not in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"Je t'ai donné le rôle : {role.mention} !", ephemeral = True)
        else: 
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Je t'ai retiré le rôle : {role.mention} !", ephemeral = True)

    @discord.ui.button(label = "Hearts of Iron IV", custom_id = ("role_" + "Hearts of Iron IV"), style = discord.ButtonStyle.grey)
    async def role_hoi(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles,name="Hearts of Iron IV")  
        if role not in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"Je t'ai donné le rôle : {role.mention} !", ephemeral = True)
        else: 
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Je t'ai retiré le rôle : {role.mention} !", ephemeral = True)

    @discord.ui.button(label = "COH 2", custom_id = ("role_" + "COH 2"), style = discord.ButtonStyle.grey)
    async def role_coh(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles,name="COH 2")  
        if role not in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"Je t'ai donné le rôle : {role.mention} !", ephemeral = True)
        else: 
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Je t'ai retiré le rôle : {role.mention} !", ephemeral = True)

    @discord.ui.button(label = "Barotrauma", custom_id = ("role_" + "Barotrauma"), style = discord.ButtonStyle.grey)
    async def role_barotrauma(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = discord.utils.get(interaction.guild.roles,name="Barotrauma")  
        if role not in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"Je t'ai donné le rôle : {role.mention} !", ephemeral = True)
        else: 
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Je t'ai retiré le rôle : {role.mention} !", ephemeral = True)

        
    

@tree.command(name = 'roles-menu', description='Affiche le menu permettant de sélectionner ses rôles') #guild specific slash command
@commands.has_permissions(manage_roles=True)
async def roles(interaction: discord.Interaction, salon: Optional[discord.TextChannel] = None): 
    if salon == None:
        salon = interaction.channel
    embed_mention=discord.Embed(title="Mention Joueur", description="Obtenez le rôle Mention Joueur pour être mentioner dès qu'une sessin de jeu commence.", color=0xffffff)
    await salon.send(embed=embed_mention, view = button_view_mention_joueur()) 
    embed_departements=discord.Embed(title="Rôle Départements", description="Récupérer les rôles des départements dans lequel vous avez un personnage pour discuter façon hrp des sujets le concernant dans des salons spéciaux.", color=0xffffff)
    await salon.send(embed=embed_departements, view = button_view_departements()) 
    embed_gaming=discord.Embed(title="Rôles Gaming", description="Marre de Garry's Mod ? Prenez les rôles correspondant aux jeux que vous possèdez pour faire une ptite'partie !", color=0xffffff)
    await salon.send(embed=embed_gaming, view = button_view_gaming())
    await interaction.response.send_message(f"Le menu à bien été affiché !", ephemeral = True)



@tree.command(name = 'resh', description='Toutes les informations sur le serveur gmod.') #guild specific slash command
async def serveurgmod(interaction: discord.Interaction):
    if interaction.channel.id == connexion_channel  :
        os.system('gamedig --type "protocol-valve" --host "178.32.105.66" --port "27100" > /home/holyhustler/discord-bot/comite-ethique/gamedig.json')
        json_file_path = "/home/holyhustler/discord-bot/comite-ethique/gamedig.json"

        with open(json_file_path, 'r') as j:
            gamedig = json.loads(j.read())
            await interaction.response.send_message(f"Commane exécuté avec succès !", ephemeral = True)
            if gamedig == "{'error': 'Failed all 1 attempts'}":
                erreur_embed=discord.Embed(title="Serveur injoignable", description="Le serveur est probablement éteint ou en plein redémarrage. Essayez dans quelques secondes !", color=0xff0000)
                await interaction.channel.send(embed=erreur_embed) 
                return
            else:
                infos_embed=discord.Embed(title=gamedig["name"], color=0x00ff04)
                infos_embed.add_field(name="Carte :", value=f'{gamedig["map"]}', inline=False)
                infos_embed.add_field(name="Joueurs :", value=f'{gamedig["raw"]["numplayers"]} / {gamedig["maxplayers"]}', inline=False)
                infos_embed.add_field(name="IP :", value=f'{gamedig["connect"]}', inline=False)
                infos_embed.add_field(name="Ping :", value=f'{gamedig["ping"]}ms', inline=False)
                await interaction.channel.send(embed=infos_embed) 
                joueurs_embed=discord.Embed(title="Joueurs connectés", color=0xffffff)
                for i in range(len(gamedig["players"])):
                    joueurs_embed.add_field(name=f'{gamedig["players"][i]["name"]}', value=f'Score : {gamedig["players"][i]["raw"]["score"]}', inline=False)
                await interaction.channel.send(embed=joueurs_embed) 
    else:
        await interaction.response.send_message(f"Cette commande ne peut être effectué que dans le salon connexions !", ephemeral = True)

class button_view_youtube(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

@tree.command(name = 'youtube', description='Télécharger des vidéos à partir de youtube.') 
@app_commands.choices(type=[
    app_commands.Choice(name="Chaîne Youtube", value="chaîne"),
    app_commands.Choice(name="Vidéo Youtube", value="vidéo"),
    app_commands.Choice(name="Playlist Youtube", value="playlist"),
])
async def dl_youtube(interaction: discord.Interaction, type: app_commands.Choice[str], lien: str):
    embed=discord.Embed(title="Téléchargement en cours ...", url=lien, description="Merci de patienter, le serveur télécharge actuellement votre/vos vidéos.", color=0xf2be31)
    embed.set_footer(text="Suppression des fichiers touts les jours à minuit.")
    await interaction.response.send_message(embed = embed, ephemeral = True)
    cheminutilisateur = "/var/www/html/bot-web/youtube/" + str(interaction.user.id)
    os.system("mkdir" + " " + cheminutilisateur + "/")
    user_choice = type.value
    nomzip = str(random.randint(0,150)) + ".zip"

    if user_choice == 'vidéo':
        video = pytube.YouTube(lien)
        nomfichier = video.title + ".mp4" 
        nomfichier = nomfichier.replace("/","")
        nomfichier = nomfichier.replace("'","")
        nomfichier = nomfichier.replace('"',"")
        video.streams.get_highest_resolution().download(output_path=("/var/www/html/bot-web/youtube/" + str(interaction.user.id)), filename = nomfichier, skip_existing=True)
        os.system("cd" + " " + cheminutilisateur + ";" + " " + "zip" + " " + nomzip + " " + "'" + nomfichier + "'" + ";" + " " + "rm" + " " + "'" + nomfichier + "'")
        embed=discord.Embed(title="Vidéo téléchargé !", url=f"http://51.178.182.136/youtube/{interaction.user.id}/{nomzip}", color=0x59ff00)
        embed.add_field(name="Nom :", value=video.title, inline=True)
        embed.add_field(name="Lien :", value=lien, inline=True)
        embed.add_field(name="Chaîne : ", value=video.channel_url, inline=True)

    if user_choice == 'playlist':
        playlist = pytube.Playlist(lien)
        for video in playlist.videos:
            nomfichier = video.title + ".mp4" 
            nomfichier = nomfichier.replace("/","")
            nomfichier = nomfichier.replace("'","")
            nomfichier = nomfichier.replace('"',"")
            video.streams.get_highest_resolution().download(output_path=("/var/www/html/bot-web/youtube/" + str(interaction.user.id)), filename = nomfichier, skip_existing=True)
            os.system("cd" + " " + cheminutilisateur + ";" + " " + "zip" + " " + nomzip + " " + "'" + nomfichier + "'" + ";" + " " + "rm" + " " + "'" + nomfichier + "'")
        embed=discord.Embed(title="Playlist téléchargé !", url=f"http://51.178.182.136/youtube/{interaction.user.id}/{nomzip}", color=0x59ff00)
        embed.add_field(name="Nom :", value=playlist.title, inline=True)
        embed.add_field(name="Lien :", value=playlist.playlist_url, inline=True)
        embed.add_field(name="Nombre de Vidéos : ", value=playlist.length, inline=True)
        embed.add_field(name="Propriétaire : ", value=playlist.owner, inline=True)
    
    embed.set_footer(text="Suppression des fichiers touts les jours à minuit.")
    view = button_view_youtube()
    view.add_item(discord.ui.Button(label="Téléchargement",style=discord.ButtonStyle.link,url=f"http://51.178.182.136/youtube/{interaction.user.id}/{nomzip}"))
    await interaction.channel.send(f"{interaction.user.mention}", embed=embed, view = view)
    

# @tree.command(name = 'histoire', description='Une petite histoire éthique rien que pour vous.') #guild specific slash command
# async def histoire(interaction: discord.Interaction, string: str):
#     await interaction.response.send_message(f"{string}", ephemeral = False) 


@tree.command(name = 'roll', description='Pour lancer des dés.')
async def roll(interaction: discord.Interaction, valeurmax: Optional[int], bonus: Optional[int], malus: Optional[int], nombred: Optional[int]):
    resultats = []
    resultatsfinaux = []
    if valeurmax == None:
        valeurmax = 100
    if bonus == None:
        bonus = 0
    if malus == None:
        malus = 0
    if nombred == None:
        nombred = 1
    for _ in range(nombred):
        tirage = random.randint(0, valeurmax)
        resultats.append(tirage)
        tirage = tirage + bonus
        tirage = tirage - malus
        resultatsfinaux.append(tirage)


    if len(resultats) > 1:
        await interaction.response.send_message("Tirage en cours !", ephemeral = True)
        for i in range(len(resultats)):
            if resultatsfinaux[i] <= 10:
                conclusion="Échec Critique"
                color = 0xff0000
            elif resultatsfinaux[i] < 50:
                conclusion="Échec"
                color = 0xffae00
            elif resultatsfinaux[i] < 90:
                conclusion="Réussite"
                color = 0xe1ff00
            elif resultatsfinaux[i] >= 90:
                conclusion="Réussite Critique"
                color = 0x2bff00
            else:
                conclusion="Erreur"
                color = 0xff00c8

            embed=discord.Embed(title=f"Tirage de {interaction.user.name}", description=f"Tirage {i+1}/{nombred} dé avec une valeur de {valeurmax}.", color=color)
            embed.add_field(name="Résultat", value=resultats[i], inline=False)
            embed.add_field(name="Bonus", value=bonus, inline=False)
            embed.add_field(name="Malus", value=malus, inline=False)
            embed.add_field(name="Résultat Final", value=resultatsfinaux[i], inline=False)
            embed.add_field(name="Conclusion", value=conclusion, inline=True)
            await interaction.channel.send(interaction.user.mention, embed=embed)
    else:
        if resultatsfinaux[0] <= 10:
            conclusion="Échec Critique"
            color = 0xff0000
        elif resultatsfinaux[0] < 50:
            conclusion="Échec"
            color = 0xffae00
        elif resultatsfinaux[0] < 90:
            conclusion="Réussite"
            color = 0xe1ff00
        elif resultatsfinaux[0] >= 90:
            conclusion="Réussite Critique"
            color = 0x2bff00
        else:
            conclusion="Erreur"
            color = 0xff00c8

        embed=discord.Embed(title=f"Tirage de {interaction.user.name}", description=f"Tirage 1/{nombred} dé avec une valeur de {valeurmax}.", color=color)
        embed.add_field(name="Résultat", value=resultats[0], inline=False)
        embed.add_field(name="Bonus", value=bonus, inline=False)
        embed.add_field(name="Malus", value=malus, inline=False)
        embed.add_field(name="Résultat Final", value=resultatsfinaux[0], inline=False)
        embed.add_field(name="Conclusion", value=conclusion, inline=True)
        await interaction.response.send_message(interaction.user.mention, embed = embed)

client.run(env['TOKEN'])
