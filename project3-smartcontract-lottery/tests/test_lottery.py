from brownie import Lottery, accounts, config, network
from web3 import Web3

# 0.0125
125_000_000_000_000_00


def test_get_entrance_fee():
    account = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_pricefeed"],
        {"from": account},
    )
    assert lottery.getEntranceFee() > Web3.toWei(0.0100, "ether")
    assert lottery.getEntranceFee() < Web3.toWei(0.0150, "ether")
