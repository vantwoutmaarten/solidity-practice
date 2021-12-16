from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3


DECIMALS = 8
STARTING_PRICE = 2000_000_000_00
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local2"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})

