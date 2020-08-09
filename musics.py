import requests
import re
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

base_url = 'https://api.deezer.com'

def get_topmusics():
    #endpoint = ''
    #choice = query

    #if choice == 'Faixas'.upper():
    #    endpoint = '/chart/0/tracks'
    #else:
    #    endpoint = '/chart/0/albums'
    endpoint = '/chart/0/tracks'
    
    final_url = base_url + endpoint

    response = requests.get(final_url).json()

    return [music['title'] for music in response['data']]

def search_musics(query):
    
    endpoint = '/search'
    artista = re.sub("[ ]", "&", query)
    
    parameters = '?' + 'q=artist:' + artista

    final_url = base_url + endpoint + parameters
    print(final_url)
    response = requests.get(final_url).json()
    
    return [music['title'] for music in response['data']]
