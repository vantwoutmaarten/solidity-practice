from brownie.network.contract import Contract
from scripts.helpful_scripts import get_account, encode_function_data, upgrade
from brownie import (
    Box,
    network,
    ProxyAdmin,
    TransparentUpgradeableProxy,
    accounts,
    BoxV2,
)


def main():
    account = get_account()
    print(f"Deploying to {network.show_active()}")

    box = Box.deploy({"from": account})
    print(box.retrieve())

    proxy_admin = ProxyAdmin.deploy({"from": account})

    # possible initializer -> initializer = box.store, 1
    # box_encoded_initializer_function = encode_function_data(initializer)
    box_encoded_initializer_function = encode_function_data()

    proxy = TransparentUpgradeableProxy.deploy(
        box.address,
        proxy_admin.address,
        box_encoded_initializer_function,
        {"from": account, "gas_limit": 1000_000},
    )

    proxy_box = Contract.from_abi("Box", proxy.address, Box.abi)
    print(f"Proxy deployed to {proxy}, you can now upgrade to v2!")
    proxy_box.store(1, {"from": account})

    box_v2 = BoxV2.deploy({"from": account})
    upgrade_transaction = upgrade(
        account, proxy, box_v2.address, proxy_admin_contract=proxy_admin
    )

    print("Proxy has been updated!")
    proxy_box = Contract.from_abi("BoxV2", proxy.address, BoxV2.abi)

    tx = proxy_box.increment({"from": account})
    tx.wait(1)

    print(proxy_box.retrieve())
