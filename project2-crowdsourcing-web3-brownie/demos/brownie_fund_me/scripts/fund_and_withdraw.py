from brownie import FundMe
from brownie.network import account
from brownie.network.web3 import _expand_environment_vars
from scripts.helpfull_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")

    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})
    print("it is wi")


def main():
    fund()
    withdraw()
