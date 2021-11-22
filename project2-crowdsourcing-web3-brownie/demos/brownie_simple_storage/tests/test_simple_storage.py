from brownie import SimpleStorage, accounts

#  Testing happens in three stages, Arrange, Act, Assert


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_stored_value():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    expected = 15

    retrieved = simple_storage.retrieve()
    # Assert
    assert 5 == retrieved
