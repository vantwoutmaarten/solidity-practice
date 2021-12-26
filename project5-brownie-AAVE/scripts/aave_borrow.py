from scripts.helpful_scripts import get_account
from brownie import config, network, interface
from scripts.get_weth import get_weth
from web3 import Web3

amount = Web3.toWei(0.01, 'ether')

def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]["weth-token"]
    if network.show_active() in ["mainnet-fork"]:
        get_weth()
    # ABI
    # Address
    lending_pool = get_lending_pool()
    # Approve sending the ERC-20 token
    approve_erc20(amount, lending_pool.address, erc20_address, account)
    # Deposit WETH into Pool
    print("Depositing")
    tx = lending_pool.deposit(erc20_address, amount, account, 0, {"from": account})
    tx.wait(1)
    print("depositedd!! oohyea")


def approve_erc20(amount, spender, erc20_address, account):
    print("Approving ERC20 token....")
    # ABI
    # Address
    erc20 = interface.IERC20(erc20_address)
    tx = erc20.approve(spender, amount, {"from":account})
    tx.wait(1)
    print("Approved!")
    return tx


def get_lending_pool():
    # ABI, Address of pool provider
    lending_pool_addresses_provider = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"]
    )
    lending_pool_address = lending_pool_addresses_provider.getLendingPool()
    # Now we have gotten the address, now we will get the ABI by using a interface
    lending_pool = interface.ILendingPool(lending_pool_address)
    return lending_pool