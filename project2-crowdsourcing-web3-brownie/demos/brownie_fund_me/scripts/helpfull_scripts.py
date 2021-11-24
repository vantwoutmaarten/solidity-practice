from brownie import network, config, accounts

# Using this function this file can be used on local development networks, or on defined persisstent networks such as rinkeby in this case.
def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])