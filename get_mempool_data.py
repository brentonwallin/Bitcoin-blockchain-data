import requests
import json

#get mempool transactions
def get_mempool_transactions():
    # Mempool Space API endpoint for getting mempool transactions
    url = "https://mempool.space/api/mempool"
    # Returns current mempool backlog statistics.
    try:
        # Send a GET request
        response = requests.get(url)
        
        # If the request was successful, the status code will be 200
        if response.status_code == 200:
            # Get the response data
            data = response.json()
            
            # Print the transactions
            print("Mempool Transactions:")
            for tx in data:
                print(tx)
        else:
            print("Failed to retrieve transactions. Status code: ", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred: ", e)

if __name__ == "__main__":
    get_mempool_transactions()
