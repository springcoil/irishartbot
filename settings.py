# Twitter Keys
import os
from pathlib import Path

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')



BASE_URL= "https://www.wikiart.org/"
STYLE_URL = "en/paintings-by-style/magic-realism?json=2"
PAGINATION_URL = "page="
#timeout for WikiArt
# SEE https://github.com/lucasdavid/wikiart/blob/master/wikiart/settings.py
METADATA_REQUEST_TIMEOUT = 2 * 60
PAINTINGS_REQUEST_TIMEOUT = 5 * 60

#Local filepaths
TOP_LEVEL_PATH = Path('/Users/peadarcoyle/irishartbot/')
ASSET_PATH = TOP_LEVEL_PATH/ 'assets'

# Metadata filename

METADATA_FILENAME = 'art_metadata.json'
METADATA_FILE = ASSET_PATH.joinpath(METADATA_FILENAME)

#AWS Locations

BASE_BUCKET  = 'irish-art-bot'
