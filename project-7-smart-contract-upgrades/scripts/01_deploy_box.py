from brownie.network.contract import Contract
from scripts.helpful_scripts import get_account, encode_function_data
from brownie import Box, network, ProxyAdmin, TransparentUpgradeableProxy


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
        {"from": account, "gas_limit": 1000_000}
    )

    proxy_box = Contract.from_abi("Box", proxy.address, Box.abi)
    print(f"Proxy deployed to {proxy}, you can now upgrade to v2!")
    
    print(proxy_box.retrieve())

