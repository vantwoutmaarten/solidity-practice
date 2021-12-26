from scripts.helpful_scripts import get_account
from brownie import interface, network, config
from web3 import Web3

def main():
    get_weth()

def get_weth():
    """
    Mint WETH in exchange for ETH
    """
    # ABI
    # Address
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth-token"])
    tx = weth.deposit({"from": account, "value": Web3.toWei(0.01, 'ether')})
    tx.wait(1)
    print("Received 0.01 WETH")
    return tx