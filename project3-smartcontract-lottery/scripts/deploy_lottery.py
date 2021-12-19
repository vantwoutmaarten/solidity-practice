from scripts.helpful_scripts import get_account
from brownie import Lottery


def deploy_lottery():
    account = get_account(id="soliditypractice-account")
    lottery = Lottery.deploy(
        
    )

def main():
    deploy_lottery()
