from brownie import SimpleStorage, accounts, config, network


def read_contract():
    # account = get_account()
    simple_storage = SimpleStorage[-1]

    print(simple_storage.retrieve())


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    read_contract()
