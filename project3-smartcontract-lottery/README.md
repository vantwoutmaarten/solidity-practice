1. Users can enter the lottery with ETH based on a USD fee
2. An admin will choose when the lottery is over (Later this might be a DAO))
3. The lottery will select a random winner

How do we want to test this?

1. `mainnet-fork`
2. `development` with mocks
3. `testnet`

First, the lottery is deployed, we get all the contracts and verify all our own contracts. Which we can interact with on etherscan.
We start the lottery, fund the contract with link. Get true randomness from the chainlink node and then pick a winner and transfer the funds.


