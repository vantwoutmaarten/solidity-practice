from brownie import SimpleStorage, accounts
from brownie.network import account


def test_deploy():
    # Arrange, Act, Assert
    account = accounts[0]

    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    assert starting_value == expected


def test_updating_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    expected = 15
    simple_storage.store(expected, {"from": account})

    assert expected == simple_storage.retrieve()
