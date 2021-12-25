from brownie import AmsterdamToken
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")

# why is the initial supply in Ether

def main():
    account = get_account()
    our_token = AmsterdamToken.deploy(initial_supply, {"from": account})
    print(our_token._name)