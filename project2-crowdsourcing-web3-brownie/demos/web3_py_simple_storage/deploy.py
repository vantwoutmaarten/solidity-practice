from solcx import compile_standard, install_solc
import json
from web3 import Web3

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    # print(simple_storage_file)

# Compile our solidity
install_solc("0.8.0")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.8.0",
)

# print(compiled_sol)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]
["bytecode"]["object"]

# get ABI
abi = compiled_sol["contract"]["SimpleStorage.sol"]["SimpleStorage"]

print(abi)


# for connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 5777
myaddress = "0xC0Bf27A5fa06D4d8DDDe025018ac7c53c91C4316"
private_key = "0x91c14c117c0f646c87d79f65c6010ac1d5fd9059428388a1d675f3d1639cfffc"

SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
print(SimpleStorage)
