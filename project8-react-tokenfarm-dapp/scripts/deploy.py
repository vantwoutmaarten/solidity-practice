from scripts.helpful_scripts import get_account, get_contract
from web3 import Web3

from brownie import DappToken, TokenFarm, network, config

KEPT_BALANCE = Web3.toWei(100, "ether")

def deploy_token_farm_and_dapp_token():
    account = get_account()
    dapp_token = DappToken.deploy({"from": account}, publish_source=config["networks"][network.show_active()]["verify"],)
    token_farm = TokenFarm.deploy(dapp_token.address, {"from": account})

    tx = dapp_token.transfer(token_farm.address, dapp_token.totalSupply() - KEPT_BALANCE, {"from": account})
    tx.wait()

    weth_token = get_contract("weth_token")
    fau_token = get_contract("fau_token")
    dict_of_allowed_tokens = {
        dapp_token: get_contract("dai_usd_price_feed"),
        fau_token:  get_contract("dai_usd_price_feed"),
        weth_token: get_contract("eth_usd_price_feed"),
    }

    add_allowed_tokens(token_farm, dict_of_allowed_tokens, account)
    return token_farm, dapp_token

    

def add_allowed_tokens(token_farm, dict_of_allowed_tokens, account):
    for token in dict_of_allowed_tokens:
        add_tx = token_farm.addAllowedTokens(token.address, {"from": account})
        add_tx.wait(1)
        setFeed_tx = token_farm.setPriceFeedContract(token.address, dict_of_allowed_tokens[token], {"from": account})
        setFeed_tx.wait(1)
    return token_farm

# dapp_token, weth_token, fau_token
def add_allowed_tokens(token_farm, dict_of_allowed_tokens, account):


def main():
    deploy_token_farm_and_dapp_token()
