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

The randomness comes from a chainlinkNode, therefore the contract was fir st funded with link.
And the code includes events, also (off-chain) to do some logging(prints) on the blockchain.

First, the lottery is deployed, we get all the contracts and verify all our own contracts. Which we can interact with on etherscan.
We start the lottery, fund the contract with link. Get true randomness from the chainlink node and then pick a winner and transfer the funds.

How do we want to test this?

1. `mainnet-fork`
2. `development` with mocks
3. `testnet`
   both unit and integration tests are made.

4. project 4: Completely custom ERC20 tokens.

This project is a bit smaller, but it shows how to build completely custom ERC-20 tokens in one of the easiest ways possible. Since, these tokens are just smart contracts that include pre specified functions, I will add these functions by using the pre-built contracts from openzeppelin.

5. project 5: brownie-AAVE.
In this project, I will work with brownie and make some scripts that interact with defi protocols. First, I will borrow and lend funds on AAVE automatically based on some conditions.

6. project 6: NFT-dogs-with-random-scarcity-features
An NFT project, three different breeds of dogs can be minted, which breed of dog is minted depends on a randomnumber generatad by chainlink. The images and the metadata of all the nfts are hosted on ipfs.
By creating tokenURI's, NFT's are visible on OpenSea. This project contains different scripts to deploy the nft factory, create new random collectibles, setting the metadata and last of all to create the tokenURI's. 

7. 
Project explowing upgradable smart contracts with different proxy patterns. The three proxy patterns explored are the transparent proxy pattern, the universal upgradable proxy and the diamond proxy pattern. 
Transparent proxy pattern: Admins can't call implementation contract functions, only functions that govern the updates. 
Universal upgradable proxy UUPS: AdminOnly upgrade functions are in the implementation contract instead of the proxy contract
Diamond pattern: allows for multiple implementation contracts.