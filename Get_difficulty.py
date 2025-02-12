import requests

def get_bitcoin_difficulty():
    url = 'https://blockchain.info/q/getdifficulty'
    response = requests.get(url)
    return response.text

# Get the current block difficulty
block_difficulty = get_bitcoin_difficulty()
print("Current Bitcoin Difficulty:", block_difficulty)
