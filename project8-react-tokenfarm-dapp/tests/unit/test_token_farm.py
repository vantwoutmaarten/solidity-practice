from black import token
from brownie import network, exceptions
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account, get_contract
from scripts.deploy import deploy_token_farm_and_dapp_token
import pytest
from web3 import Web3

def test_set_price_feed_contract():
    #Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
            pytest.skip("only for local testing")
    account = get_account()
    non_owner = get_account(index=1)

    # Act
    token_farm, dapp_token = deploy_token_farm_and_dapp_token()

    priceFeedAddress = get_contract("eth_usd_price_feed")
    token_farm.setPriceFeedContract(dapp_token.address, priceFeedAddress.address, {"from": account})
    # Assert
    assert token_farm.tokenPriceFeedMapping(dapp_token.address) == get_contract("eth_usd_price_feed")
    with pytest.raises(exceptions.VirtualMachineError):
        token_farm.setPriceFeedContract(dapp_token.address, priceFeedAddress.address, {"from": non_owner})

INITIAL_PRICE_FEED_VALUE = Web3.toWei(2000, "ether")

def test_issue_tokens(amount_staked):
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing!")
    account = get_account()
    token_farm, dapp_token = test_stake_tokens(amount_staked)
    starting_balance = dapp_token.balanceOf(account.address)

    print(f"token farm balance of dapp tokens {dapp_token.balanceOf(token_farm.address)}")

    print(f"the user total value is {token_farm.getUserTotalValue(account.address)}")

    tx = token_farm.issueTokens({"from": account})
    tx.wait(1)

    assert (
        dapp_token.balanceOf(account.address) 
        == starting_balance + INITIAL_PRICE_FEED_VALUE
    )


def test_stake_tokens(amount_staked):
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    account = get_account()
    token_farm, dapp_token = deploy_token_farm_and_dapp_token()
    # Act 
    dapp_token.approve(token_farm.address, amount_staked , {"from": account})
    
    # token_farm.allowedTokens.push(dapp_token)
    token_farm.stakeTokens(amount_staked, dapp_token.address, {"from": account})
    assert (
        token_farm.stakingAmount(account.address, dapp_token.address) == amount_staked
    )
    assert token_farm.stakers(0) == account.address
    return token_farm, dapp_token