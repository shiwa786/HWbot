"""
MIT License

Copyright (c) 2022 Arsh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open('{}/Himawari/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]

class Config(object):

    ##dont change
    LOGGER=True
    ALLOW_CHATS=True
    ALLOW_EXCL=False
    TEMP_DOWNLOAD_DIRECTORY="./"
    DEL_CMDS=False
    BAN_STICKER="kans" 
    CERT_PATH=""
    PORT=8443
    WORKERS=8
    LOAD=""
    NO_LOAD="translation"
    MONGO_DB="Himawari"
    WEBHOOK=False
    BOT_API_URL="https://api.telegram.org/bot"

    #you can change these 
    INFOPIC=True #picture while doing /info
    STRICT_GBAN=True
    API_ID= "4277083" ##api id from my.telegram.org
    APP_ID= "4277083" #same as API_ID
    API_HASH="bb0ddae0921fc020ce61faae2d1261d5" ##api hash from my.telegram.org
    APP_HASH="bb0ddae0921fc020ce61faae2d1261d5" #same as API_HASH
    BL_CHATS=[1] #chats to be blacklisted
    MONGO_DB_URL="mongodb+srv://Alexabot:Alexabotdb@cluster0.6m9qtav.mongodb.net/?retryWrites=true&w=majority" ##mongo database link (necessary)
    DB_URL2="mongodb+srv://meowhisswswuj7.mongodb.net/?retryWrites=true&w=majority" #mongo db (not necessary)
    DB_URL="postgresql://qrfbmoajhwilxm:f715cae74cee67099feb4ba5dfc521fa5d6abd3f91c7c27712f39587397a73f0@ec2-3-222-74-92.compute-1.amazonaws.com:5432/dddifat23mf6tb" #postgres sql database link
    REDIS_URL="redis://ok:Da%4012345@redis-15098.c56.east-us.azure.cloud.redislabs.com:15098" #redis database url from redislabs.com
    TOKEN="5643681960:AAHwNOqT9DFsxYDvCudTe2IOAkwjA_RghQQ" #bot token from @BotFather
    DEV_USERS=[5306064258] #developers id
    DRAGONS=[9656] #sudo users id
    DEMONS=[1909] #support user ids
    TIGERS=[1] #commas for multiple ids
    WOLVES=[2112, 1212] #commas for multiple ids 
    DONATION_LINK="https://www.paypal.me/PaulSonOfLars" #u can change with yours
    EVENT_LOGS=-1001747540803 #channel id for gban logs
    JOIN_LOGGER=-1001747540803  #log channel/group id
    OWNER_ID=5497627952 #owner id in integer
    ERROR_LOGS=-1001747540803 #support group id
    BOT_NAME="elisa" #your bot name
    ARQ_API_KEY="SLSFXSsdUXNSMH-ARQ" #ARQ api key from @ARQRobot
    ARQ_API_URL="arq.hamker.dev" #arq link
    SUPPORT_CHAT="elisha_support" #support group username without @
    OWNER_USERNAME="denvil_xdd" #owner username without @
    UPDATES_CHANNEL="denvil_bots" #Updates/News Channel username without @
    BOT_USERNAME="miselisarobot" #bot username without @
    REM_BG_API_KEY="K2dsdsYma6cZx" #not necessary
    GENIUS_API_TOKEN="e-8UdRQNrIssPyM" # api token from genius.com (not necessary)
    TIME_API_KEY="QLLLDV7SWFD3" #not necessary
    SPAMWATCH_API="J968E_20LgxrKjsdN24cqYtD~gNRTbU" #spamwatch api token from @SpamWatchBot
    WALL_API="6950f5ds6a3" #wall api (not necessary)
    BOT_ID = ""
    HEROKU_APP_NAME = ""
    HEROKU_API_KEY = ""
 


class Production(Config):
    LOGGER=True


class Development(Config):
    LOGGER=True
