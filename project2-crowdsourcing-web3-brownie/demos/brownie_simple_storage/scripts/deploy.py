from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    # account = accounts.load("soliditypractice-account")
    # By using this config file we do not have to go through all the scripts but can access the key directly.
    # account = accounts.add(config["wallets"]["from_key"])
    account = get_account()

    print("printen account")
    # brownie knows the difference between transactions and calls
    simple_storage = SimpleStorage.deploy({"from": account})

    stored_value = simple_storage.retrieve()
    print(stored_value)

    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)

    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


# Using this function this file can be used on local development networks, or on defined persisstent networks such as rinkeby in this case.
def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    print("helloe")
    deploy_simple_storage()
