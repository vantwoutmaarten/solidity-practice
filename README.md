# solidity-practice

Practicing solidity by building simple Dapps till full stack Defi

project1-crowdsourcing-contracts-remix:

This is a remix ethereum project made in Remix, it contains fundable smart contracts, a crowdsourcing application is made that can be funded by anybody and the funds can only be withdrawn by the owner of the contract.
By integrating chainlink price feeds, a minumum deposit amount in USD is integrated by creating conversion functions.

project2-crowdsourcing-contracts-web3-brownie:
this project contains three demos

1.  Almost the same as the previous project in terms of contracts, but this time it is not using the online remix IDE,
    here in this project, I deployed contracts to local ganache blockchains, deploying to testnets and even mainnets, signing and sending transactions to these nets.
    Also practiced with private key management and the ganache-cli.

2.  Now I will make the exact same functionality, but now simplified by using brownie.

3.  Here the contract is made functional with the payable functions and now has the contract functionalities with much less work needed than when developing in remix.

project3-smartcontract-lottery:

1. Users can enter the lottery with ETH based on a USD fee
2. An admin will choose when the lottery is over (Later this might be a DAO))
3. The lottery will select a random winner

The randomness comes from a chainlinkNode, therefore the contract was first funded with link.
And the code includes events, also (off-chain) to do some logging(prints) on the blockchain.

First, the lottery is deployed, we get all the contracts and verify all our own contracts. Which we can interact with on etherscan.
We start the lottery, fund the contract with link. Get true randomness from the chainlink node and then pick a winner and transfer the funds.

How do we want to test this?

1. `mainnet-fork`
2. `development` with mocks
3. `testnet`
   both unit and integration tests are made.

4. Completely custom ERC20 tokens.

This project is a bit smaller, but it shows how to build completely custom ERC-20 tokens in one of the easiest ways possible. Since, these tokens are just smart contracts that include pre specified functions, I will add these functions by using the pre-built contracts from openzeppelin.
