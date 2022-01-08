from scripts.helpful_scripts import get_account, encode_function_data, upgrade
from brownie import (
    Box,
    BoxV2,
    ProxyAdmin,
    Contract,
    TransparentUpgradeableProxy,
    exceptions,
)
import pytest


def test_proxy_upgrades():
    account = get_account()
    box = Box.deploy({"from": account})
    proxy_admin = ProxyAdmin.deploy({"from": account})
    box_encoded_initializer_function = encode_function_data()
    proxy = TransparentUpgradeableProxy.deploy(
        box.address,
        proxy_admin.address,
        box_encoded_initializer_function,
        {"from": account, "gas_limit": 1000000},
    )
    proxy_box = Contract.from_abi("Box", proxy.address, Box.abi)

    tx = proxy_box.store(1, {"from": account})
    tx.wait(1)

    box_v2 = BoxV2.deploy({"from": account})
    proxy_box = Contract.from_abi("BoxV2", proxy.address, BoxV2.abi)

    with pytest.raises(exceptions.VirtualMachineError):
        #  This gives an error, because the proxy does not yet contain the boxv2 abi.
        proxy_box.increment({"from": account})

    assert proxy_box.retrieve() == 1

    upgrade(account, proxy, box_v2.address, proxy_admin_contract=proxy_admin)
    tx2 = proxy_box.increment({"from": account})
    tx2.wait(1)

    assert proxy_box.retrieve() == 2
