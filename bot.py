from itertools import chain
import os
import sys
from dotenv import load_dotenv
from twitchio.ext import commands
import irc.bot
import requests

class TwitchQuizBot(irc.bot.SingleServerIRCBot):
    def  __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel


        #get the channel id, needed for v5 api calls
        url = 'https://api.twitch.tv/kraken/users?login' + channel
        headers =  {'Client-ID': client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
        r = requests.get(url, headers=headers).json()
        self.channel_id = r['users'][0]['_id']

        #create the IRC connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        print('Connecting to ') + server + ' on port ' + str(port) + '...'
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:'+token)], username, username)

    def on_welcome(self, c, e):
        print("Joining " + self.channel)

        #gotta request specific capabilities
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)









def main():
    load_dotenv()

    username = os.getenv('USERNAME')
    token=os.getenv('TOKEN')
    client_id=os.getenv('CLIENT_ID')
    prefix=os.getenv('BOT_PREFIX')
    channel=os.getenv('CHANNEL')

    bot = TwitchQuizBot(username, client_id, token, channel)
    bot.start()




if __name__ == "__main__":
    main()