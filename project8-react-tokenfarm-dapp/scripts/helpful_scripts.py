from brownie import accounts, network, config, Contract, MockV3Aggregator, MockDAI, MockWETH
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache", "mainnet-fork"]
NON_FORKED_LOCAL_BLOCKCHAINS = ["mainnet-fork"]
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"

INITIAL_PRICE_FEED_VALUE = Web3.toWei(2000, "ether")
DECIMALS = 18

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])


contract_to_mock = {
    "eth_usd_price_feed": MockV3Aggregator,
    "dai_usd_price_feed": MockV3Aggregator,
    "fau_token": MockDAI,
    "weth_token": MockWETH
}


def get_contract(contract_name):
    """ "This  function will grab the contract addresses from the brownie config
    if defined, otherwise, it will deploy a mock version of that contract and return that mock contract.

        Args:
            contract_name (string)

        Returns:
            brownie.network.contract.ProjectContract: The most recently deployed version of the contract
    """
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(contract_type) <= 0:
            # MockV3Aggregator.length
            deploy_mocks()
        contract = contract_type[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        # Address
        # ABI
        contract = Contract.from_abi(
            contract_type._name, contract_address, contract_type.abi
        )
    return contract


def deploy_mocks():
    """
    Use this script if you want to deploy mocks to a testnet
    """
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    account = get_account()

    print("Deploying Mock Price Feed...")
    decimals = DECIMALS
    initialAnswer = INITIAL_PRICE_FEED_VALUE
    mock_price_feed = MockV3Aggregator.deploy(decimals, initialAnswer,
        {"from": account}
    )
    print(f"Deployed to {mock_price_feed.address}")

    print("Deploying Mock DAI...")
    dai_token = MockDAI.deploy({"from":account})
    print(f"Deployed to {dai_token.address}")

    print("Deploying Mock DAI...")
    weth_token = MockWETH.deploy({"from":account})
    print(f"Deployed to {dai_token.address}")

def fund_with_link(
    contract_address, account=None, link_token=None, amount=Web3.toWei(0.3, "ether")
):  # 0.1 Link
    account = account if account else get_account()
    link_token = link_token if link_token else get_contract("link_token")

    tx = link_token.transfer(contract_address, amount, {"from": account})
    tx.wait(1)
    print(f"funded contract {contract_address} !")
    return tx


BREED_MAPPING = {0: "HAPPY_PUG", 1: "SHIBA_INU", 2: "ST_BERNARD"}


def get_breed(breed_number):
    return BREED_MAPPING[breed_number]
