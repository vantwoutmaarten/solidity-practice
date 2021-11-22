from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    # account = accounts.load("soliditypractice-account")
    # By using this config file we do not have to go through all the scripts but can access the key directly.
    # account = accounts.add(config["wallets"]["from_key"])
    account = accounts[0]
    print(account)
    print("printen account")
    # brownie knows the difference between transactions and calls
    simple_storage = SimpleStorage.deploy({"from": account})

    stored_value = simple_storage.retrieve()
    print(stored_value)

    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)

    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def main():
    print("helloe")
    deploy_simple_storage()
