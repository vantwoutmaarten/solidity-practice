# Notes on the Lazy minting turtorial.

## Lazy minting is an advanced technique to defer the cost of NFT minting

The gas fees for minting are included in the same transaction as assigning the NFT to the buyer so a portion of the purchase price is used to create the record. Openzeppelin is also using this.

# How it works.

1.  NFT Creator creates a signature, (some data signed with privKey)
2.  The Creator makes NFTVouchers that include this signature, these can be redeemed for the NFT.
    Example.

struct NFTVoucher {

- uint256 tokenId;
- uint256 minPrice;
- string uri;
- bytes signature;
  }

3. The Voucher includes all NFT data for on-chain, in this case the id and uri, but also contains ofchain data, such minPrice, which you have to include in the transaction.

4. The voucher needs a condition, such as a price or a voucher.recipient.

5. EIP-712 is the standard for this signing, protects against replay attack, and let tools as metamask intepret and show what data is signed.

6. the solidity file contains the minter adress in the constructor, the minter address is also the voucher signer, but not the voucher redeemer, on redeem the nft is minted to the signer and then transfered to the redeemer.

and the voucherCreator/Lazyminter js file, gets the contract and signer address.

Advantages:

- owner can mint these nfts and decide who can mint.
- owner does have to pay for the minting of all the NFTs.
- ownver can later make different decisions about who should pay for the mint, by making vouchers for different redeemer addresses.
- reusable system for all by using this contract with different vouchers.
- By creating a voucher per tokenID, we do not need to keep track of who already minted. (saves storage for each mint).

Disadvantes:

- We could use different minting requirements than voucher.
- Owner can just be the only minter for other NFTs, easy but expensive.
- Not doing it would safe a little bit deployment cost, since the hash an verify functions to check the vouchers do not have to be deployed.
- It is more expensive for the user and they don’t immediately get an NFT when they ‘deserve’ one.

# notes for work.

Include the type nft type instead of the uri.

A condition in the voucher could have a price || privateSale investor || specialWallet investor.
