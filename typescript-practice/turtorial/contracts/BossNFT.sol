// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.12;
import "hardhat/console.sol";

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract BossNFT is ERC721 {

    constructor(string memory name, string memory symbol) 
        ERC721(name, symbol) {

        }

}