from solcx import compile_standard, install_solc
import json
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()

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


with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get ABI
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]


# for connecting to ganache
w3 = Web3(
    Web3.HTTPProvider("https://rinkeby.infura.io/v3/34e77dfbe97443a9b5435282eafde927")
)
# 4 is the chain id of rinkeby
chain_id = 4
my_address = "0xBd4dCc658BD59F5E73133809C03F2AcD9C4Cd944"

# It is really bad to hardcode private keys in code pushed to github, therefore we set them in Environment variables.
# private_key = "0x03c9021073093e5e9ffa28068764d460b111063c60ad3b2e711961a167fd4ee8"
private_key = os.getenv("PRIVATEKEY_FAKEMONEY")

# Create the contract in Python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# Before making a statechange to the blockchain we first have to build a transaction. Build, Sign, Send a transaction
nonce = w3.eth.getTransactionCount(my_address)

contract_transaction = SimpleStorage.constructor()

# Before it was not necessary to include the gasprice, but now it is. Here the transaction is builld
transaction = contract_transaction.buildTransaction(
    {"chainId": chain_id, "from": my_address, "nonce": nonce, "gasPrice": 20000000000}
)

signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

print("Deploying the smart contract")
# Send this signed transaction
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
# This will wait for a few block confirmations to make sure it actually happened.
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Deployed contract")

# Working with a contract
# Contract Address
# Contract ABI
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# There are two ways to interact with the block chain call or transact
# Call -> Simulate making the call and getting the return value without making a statechange
# Transact -> is when you actually make a state change
# when transicting on a view function nothing happens

print(simple_storage.functions.retrieve().call())

print("starting updating contract")
store_transaction = simple_storage.functions.store(15).buildTransaction(
    {
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce + 1,
        "gasPrice": 20000000000,
    }
)

signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)

send_store_txn = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_txn)
print("stored value and updated contract")
print(simple_storage.functions.retrieve().call())
