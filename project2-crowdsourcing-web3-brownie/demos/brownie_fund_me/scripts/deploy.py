from brownie import FundMe, network, config
from scripts.helpfull_scripts import get_account


def deploy_fund_me():
    account = get_account()
    # if we are on persistent network like rinkeby, use the associated address
    # Otherwise, deploy mocks to simulate the price feed on a local network
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        # deploy mock
        price_feed_address = 


    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=True,
    )
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
