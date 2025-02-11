import requests

def get_bitcoin_block_height():
    url = 'https://blockchain.info/q/getblockcount'
    response = requests.get(url)
    return response.text

# Get the current block height
block_height = get_bitcoin_block_height()
print("Current Bitcoin Block Height:", block_height)
