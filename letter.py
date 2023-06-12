#Bibliotecas
import requests
import discord
from discord.ext import commands, tasks
from bs4 import BeautifulSoup
#Bibliotecas

#Formatações e definição de cliente
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents)
client = commands.Bot(command_prefix='?', intents=intents)
#Formatações e definição de cliente

#Informa no prompt que o bot esta pronto
@bot.event
async def on_ready():
    print(f'Bot está pronto! Conectado como {bot.user}')
#Informa no prompt que o bot esta pronto



#FUTEBOL

#API de futebol para saber o jogos do dia comando ?jogos 
@bot.command()
async def jogos(ctx):
    headers = {
        'X-Auth-Token': 'c7c0c6a2ffc74bef852db478c9b34b1f'
    }
    url = 'http://api.football-data.org/v4/matches'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        matches = data['matches']
        for match in matches:
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']
            result = match['score']['fullTime']
            result_text = f"{result['home']} - {result['away']}"
            await ctx.send(f"{home_team} vs {away_team}: {result_text}")
    else:
        await ctx.send('Comando inválido! Parece que você tropeçou na bola. Dê outro toque e tente novamente!')
#API de futebol para saber o jogos do dia comando ?jogos 



#API de futebol para saber o id das ligas comando ?ligaid
@bot.command()
async def ligaid(ctx):
    headers = {
        'X-Auth-Token': 'c7c0c6a2ffc74bef852db478c9b34b1f'
    }
    url = 'http://api.football-data.org/v4/competitions/'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        competitions = data['competitions']
        for competition in competitions:
            competition_id = competition['id']
            competition_name = competition['name']
            await ctx.send(f"Liga: {competition_name}, ID: {competition_id}")
    else:
        await ctx.send('Eu entendo que o futebol pode ser confuso às vezes, mas esse comando está fora de campo. Tente outro!')
#API de futebol para saber o id das ligas comando ?ligaid


#API de futebol para pesquisar o id das ligas comando ?liga (mais o id do comando ?ligaid)
@bot.command()
async def liga(ctx, competition_id):
    headers = {
        'X-Auth-Token': 'c7c0c6a2ffc74bef852db478c9b34b1f'
    }
    url = f'http://api.football-data.org/v4/competitions/{competition_id}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        competition_name = data['name']
        emblem_url = data['emblem']
        current_season = data['currentSeason']
        current_matchday = current_season['currentMatchday']
        winner = current_season['winner']
        
        message = f"Liga: {competition_name}\n"
        message += f"Emblema: {emblem_url}\n"
        message += f"Rodada atual: {current_matchday}\n"
        
        if winner is not None:
            winner_name = winner['name']
            winner_crest = winner['crest']
            message += f"Vencedor da temporada anterior: {winner_name}\n"
            message += f"Emblema do vencedor: {winner_crest}"
        
        await ctx.send(message)
    else:
        await ctx.send('Pra fora! Esse comando foi para a arquibancada, não para o campo. Vamos tentar um válido!')
#API de futebol para pesquisar o id das ligas comando ?liga (mais o id do comando ?ligaid)


#API de futebol para saber o id dos times comando ?timeid
@bot.command()
async def timeid(ctx):
    headers = {
        'X-Auth-Token': 'c7c0c6a2ffc74bef852db478c9b34b1f'
    }
    url = 'http://api.football-data.org/v4/teams'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        teams = data['teams']
        for team in teams:
            team_id = team['id']
            team_name = team['name']
            await ctx.send(f"Time: {team_name}, ID: {team_id}")
    else:
        await ctx.send('Parece que você cometeu uma falta com esse comando. Vamos jogar limpo e tentar um válido!')
#API de futebol para saber o id dos times comando ?timeid


#API de futebol para pesquisar o id dos times comando ?time (mais o id do comando ?timeid)
@bot.command()
async def time(ctx, team_id):
    headers = {
        'X-Auth-Token': 'c7c0c6a2ffc74bef852db478c9b34b1f'
    }
    url = f'http://api.football-data.org/v4/teams/{team_id}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        team_name = data['name']
        team_short_name = data['shortName']
        team_tla = data['tla']
        team_crest = data['crest']
        team_address = data['address']
        team_website = data['website']
        team_founded = data['founded']
        team_colors = data['clubColors']
        team_venue = data['venue']
        await ctx.send(f"Nome: {team_name}\nNome abreviado: {team_short_name}\nTLA: {team_tla}\nBrasão: {team_crest}\nEndereço: {team_address}\nWebsite: {team_website}\nFundado em: {team_founded}\nCores do clube: {team_colors}\nEstádio: {team_venue}")
    else:
        await ctx.send('Esse comando está mais perdido do que o juiz apitando os jogos do seu time. Tente outro, por favor!')
#API de futebol para pesquisar o id dos times comando ?time (mais o id do comando ?timeid)


#API de futebol para saber as partidas dos times comando ?time (mais o id do comando ?timeid)
@bot.command()
async def partidas(ctx, team_id):
    headers = {
        'X-Auth-Token': 'seu_token_da_API_da_Football_Data'
    }
    url = f'http://api.football-data.org/v4/teams/{team_id}/matches'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        matches = data['matches']
        for match in matches:
            home_team = match['homeTeam']['name']
            away_team = match['awayTeam']['name']
            utc_date = match['utcDate']
            status = match['status']
            venue = match.get('venue', 'Informação do local não disponível')
            await ctx.send(f"Data: {utc_date}\nCasa: {home_team}\nVisitante: {away_team}\nLocal: {venue}\nStatus: {status}\n")
    else:
        await ctx.send('Impedimento! Esse comando está além da linha de impedimento. Tente novamente jogando dentro das regras!')
#API de futebol para saber as partidas dos times comando ?time (mais o id do comando ?timeid)

#FUTEBOL

#CARTOLA


@bot.command()
async def atletascartola(ctx, query):
    url = 'https://api.cartola.globo.com/atletas/mercado'
    response = requests.get(url)
    data = response.json()

    jogadores = data['atletas']
    message = ""

    if query.isdigit():
        # Pesquisar por atleta_id
        jogador = next((j for j in jogadores if j['atleta_id'] == int(query)), None)
        if jogador:
            atleta_info = format_atleta_info(jogador)
            message += atleta_info + "\n---\n"
    else:
        # Pesquisar por clube_id
        clube_id = int(query)
        jogadores_clube = [j for j in jogadores if j.get('clube_id') == clube_id]
        if jogadores_clube:
            for jogador in jogadores_clube:
                atleta_info = format_atleta_info(jogador)
                message += atleta_info + "\n---\n"

    if message:
        embed = discord.Embed(title='Informações dos Jogadores', description=message, color=discord.Color.green())
        await ctx.send(embed=embed)
    else:
        await ctx.send("Nenhum jogador encontrado.")

def format_atleta_info(atleta):
    atleta_id = atleta['atleta_id']
    clube_id = atleta['clube_id']
    nome = atleta['nome']
    apelido = atleta['apelido']
    preco = atleta['preco_num']

    return f"**Nome:** {nome}\n**Apelido:** {apelido}\n**ID do Atleta:** {atleta_id}\n**ID do Clube:** {clube_id}\n**Preço:** R${preco}"

@bot.command()
async def timescartola(ctx, clube_id: int):
    url = 'https://api.cartola.globo.com/atletas/mercado'
    response = requests.get(url)
    data = response.json()

    jogadores = data['atletas']
    message = ""

    jogadores_clube = [j for j in jogadores if j.get('clube_id') == clube_id]
    if jogadores_clube:
        for jogador in jogadores_clube:
            atleta_info = format_atleta_info(jogador)
            message += atleta_info + "\n---\n"

    if message:
        embed = discord.Embed(title='Jogadores do Time', description=message, color=discord.Color.green())
        await ctx.send(embed=embed)
    else:
        await ctx.send("Nenhum jogador encontrado para esse clube.")

def format_atleta_info(atleta):
    atleta_id = atleta['atleta_id']
    nome = atleta['nome']
    apelido = atleta['apelido']
    preco = atleta['preco_num']

    return f"**Nome:** {nome}\n**Apelido:** {apelido}\n**ID do Atleta:** {atleta_id}\n**Preço:** R${preco}"

@bot.command()
async def selecaocartola(ctx):
    response = requests.get('https://api.cartola.globo.com/mercado/destaques')
    data = response.json()

    embed = discord.Embed(title='Melhores do Cartola', color=discord.Color.green())

    for jogador in data:
        posicao = jogador['posicao']
        clube = jogador['clube_nome']
        nome = jogador['Atleta']['nome']
        apelido = jogador['Atleta']['apelido']
        preco = jogador['Atleta']['preco_editorial']
        foto = jogador['Atleta']['foto']

        embed.add_field(name=f'{posicao} - {clube}', value=f'{nome} ({apelido}) - R${preco}', inline=False)
        embed.set_thumbnail(url=foto)

    await ctx.send(embed=embed)
#CARTOLA

#API de clima para saber a previsao do tempo no Brasil




@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == 'rildo':
        await message.channel.send('Gomes')

    await bot.process_commands(message)


@bot.command()
async def send_to_all(ctx, message):
    for guild in bot.guilds:
        for channel in guild.text_channels:
            try:
                await channel.send(message)
            except Exception as e:
                print(f"Erro ao enviar mensagem para o servidor {guild.name}: {e}")
    await ctx.send("Mensagem enviada para todos os servidores!")

#TOKEN DO BOT
bot.run("MTExMjgxNzU4MTQ1MjE3NzUzOQ.GLGBuJ.fC4-CXaE3N3IQOmlhsjn1qDc7dFUuhxSKejilU")
#TOKEN DO BOT
