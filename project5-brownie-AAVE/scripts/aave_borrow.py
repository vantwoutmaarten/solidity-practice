from scripts.helpful_scripts import get_account
from brownie import config, network, interface
from scripts.get_weth import get_weth
from web3 import Web3

amount = Web3.toWei(0.01, "ether")


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
    # ....How much can we borrow? Depends on the current collaterol and Debts
    borrowable_eth, total_debth = get_borrowable_data(lending_pool, account)
    # DAI in terms of ETH so we have to get the conversion rate
    dai_eth_price = get_asset_price(
        config["networks"][network.show_active()]["dai_eth_price_feed"]
    )
    amount_dai_to_borrow = (1 / dai_eth_price) * (borrowable_eth * 0.50)
    # borrowable_eth --> borrowable_dai * 50%
    print(f"We are going to borrow {amount_dai_to_borrow} DAI!")
    # Now we will borrow
    borrow_tx = lending_pool.borrow(
        config["networks"][network.show_active()]["dai_token"],
        Web3.toWei(amount_dai_to_borrow, "ether"),
        1,
        0,
        account.address,
        {"from": account},
    )
    borrow_tx.wait(1)
    print("Borrowed some DAI")
    get_borrowable_data(lending_pool, account)
    repay_all(amount, lending_pool, account)


def repay_all(amount, lending_pool, account):
    approve_erc20(
        Web3.toWei(amount, "ether"),
        lending_pool.address,
        config["networks"][network.show_active()]["dai_token"],
        account,
    )
    repay_tx = lending_pool.repay(config["networks"][network.show_active()]["dai_token"], amount, 1, account.address, {"from": account})
    repay_tx.wait(1)
    print("Finally, deposited, borrowed and repayed with Aave, Brownie, and chainlink!")


def get_asset_price(dai_eth_price_feed):
    # ABI
    # Address
    dai_eth_price_feed = interface.AggregatorV3Interface(dai_eth_price_feed)
    latest_price = dai_eth_price_feed.latestRoundData()[1]
    converted_latest_price = Web3.fromWei(latest_price, "ether")
    print(f"The DAI/ETH price is {converted_latest_price}")
    return float(latest_price)


def get_borrowable_data(lending_pool, account):
    (
        total_collaterol_eth,
        total_debt_eth,
        available_borrow_eth,
        current_liquadation_threshold,
        ltv,
        healthfactor,
    ) = lending_pool.getUserAccountData(account.address)

    available_borrow_eth = Web3.fromWei(available_borrow_eth, "ether")
    total_collaterol_eth = Web3.fromWei(total_collaterol_eth, "ether")
    total_debt_eth = Web3.fromWei(total_debt_eth, "ether")

    print(f"You have {total_collaterol_eth} worth of eth deposited")
    print(f"You have {total_debt_eth} worth of eth borrowed")
    print(f"You can borrow {available_borrow_eth} worth of eth")
    # Using floats conveniet to do math on them later
    return (float(available_borrow_eth), float(total_debt_eth))


def approve_erc20(amount, spender, erc20_address, account):
    print("Approving ERC20 token....")
    # ABI
    # Address
    erc20 = interface.IERC20(erc20_address)
    tx = erc20.approve(spender, amount, {"from": account})
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
