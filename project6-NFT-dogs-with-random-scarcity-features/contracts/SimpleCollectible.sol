 // SPDX-License-Identifier: MIT

pragma solidity ^0.8.0

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleCollectible is ERC721 {

    constructor () public ERC721 ("Dogie", "DOG") {
        
    }

}