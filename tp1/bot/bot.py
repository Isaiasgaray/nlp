from dotenv import load_dotenv
from utils import col_to_snake_case, serie_to_str
import telebot
import pandas as pd
import os
import sys

# Cargamos el token
load_dotenv()

# Cargamos y preparamos el dataset
PATH_DATASET = '../datasets/lacapital.csv'
MIN_NOTICIAS = 10

df = pd.read_csv(PATH_DATASET)
df['categoria'] = col_to_snake_case(df['categoria'])

categorias_conteo  = df['categoria'].value_counts()
categorias_validas = categorias_conteo >= MIN_NOTICIAS

categorias = list(categorias_conteo[categorias_validas].index)
categorias_num = list(categorias_conteo[categorias_validas].values)

# Creación del bot
bot = telebot.TeleBot(os.environ.get('TOKEN', ''))

# Constantes del bot
SALUDO = 'Hola!\nLas categorías y cantidad de noticias son las siguientes:\n' \
    + '\n'.join(f'/{cate} {str(num)}' for (cate, num) 
                  in zip(categorias, categorias_num))
ID_REGEX = r'^\/(\d+)$'

# Handlers del bot
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, SALUDO)

@bot.message_handler(commands=categorias)
def handle_category(message):
    categoria = message.text[1:]

    df_noticias = df[df['categoria'] == categoria].sample(5)

    respuesta = serie_to_str(df_noticias['titulo'])
    bot.send_message(message.chat.id, respuesta)

@bot.message_handler(regexp=ID_REGEX)
def handle_id(message):
    idx = int(message.text[1:])

    try:
        titulo = df.loc[idx]['titulo']
    except:
        titulo = str()

    if not titulo:
        respuesta = f'El índice {idx} no está en el dataset.'
    else:
        url = df.loc[idx]['url']
        respuesta = f'{titulo}\n{url}'

    bot.send_message(message.chat.id, respuesta)

@bot.message_handler(func=lambda m: True)
def handle_search(message):

    df_bool = df['titulo'].str.contains(message.text, case=False)

    if df[df_bool].empty:
        respuesta = 'No encontré títulos con ese texto.'
    else:
        respuesta = serie_to_str(df[df_bool][:5]['titulo'])

    bot.send_message(message.chat.id, respuesta)

# Corremos el bot
try:
    bot_info = bot.get_me()

    if bot_info:
         print('Iniciando bot')
         bot.infinity_polling()

except Exception as e:
    print(f'Error -> {e}', file=sys.stderr)
    sys.exit(1)
