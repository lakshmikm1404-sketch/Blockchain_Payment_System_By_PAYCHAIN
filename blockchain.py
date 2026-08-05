from web3 import Web3

RPC_URL = "https://polygon-rpc.com"

web3 = Web3(
    Web3.HTTPProvider(RPC_URL)
)

def wallet_balance(address):
    balance = web3.eth.get_balance(address)

    return web3.from_wei(
        balance,
        "ether"
    )
