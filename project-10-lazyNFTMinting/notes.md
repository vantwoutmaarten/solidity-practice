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
5.

# notes for work.

Include the type nft type instead of the uri.

A condition in the voucher could have a price || privateSale investor || specialWallet investor.
