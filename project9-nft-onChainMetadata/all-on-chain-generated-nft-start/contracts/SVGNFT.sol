// give the contract some SVG code
// output an NFT URI with SVG code
// Storing all the NFT metadata on chain.

// SPDX-Licence-Identifier: MIT
pragma solidity 0.8.13;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

// import "@openzeppelin/contracts/drafts/Counters.sol";

contract SVGNFT is ERC721URIStorage {
    constructor() public {
        super();
    }
}
