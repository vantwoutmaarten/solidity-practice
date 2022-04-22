// give the contract some SVG code
// output an NFT URI with SVG code
// Storing all the NFT metadata on chain.

// SPDX-Licence-Identifier: MIT
pragma solidity 0.8.13;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "base64-sol/base64.sol";

contract SVGNFT is ERC721URIStorage {
    uint256 public tokenCounter;

    event CreatedSVGNFT(uint256 indexed tokenId, string tokenURI);

    constructor() ERC721("SVG NFT", "svgNFT") {
        tokenCounter = 0;
    }

    function create(string memory _svg) public {
        // imageURI
        string memory imageURI = svgToImageURI(_svg);
        // tokenURI
        string memory tokenURI = formatTokenURI(imageURI);

        emit CreatedSVGNFT(tokenCounter, tokenURI);
        _safeMint(msg.sender, tokenCounter);
        _setTokenURI(tokenCounter, tokenURI);
    }

    function formatTokenURI(string memory _imageURI)
        public
        pure
        returns (string memory)
    {
        string memory tokenURI = string.concat(
            "data:application/json;base64,",
            Base64.encode(
                bytes(
                    string.concat(
                        '{"name":"SVG NFT",',
                        '"description":"An NFT based SVG!",',
                        '"attributes":"",',
                        '"image":"',
                        _imageURI,
                        '"}'
                    )
                )
            )
        );
        return tokenURI;
    }

    function svgToImageURI(string memory _svg)
        public
        pure
        returns (string memory)
    {
        string memory baseURL = "data:image/svg+xml;base64,";
        string memory svgBase64Encoded = Base64.encode(
            bytes(string(abi.encodePacked(_svg)))
        );
        string memory imageURI = string.concat(baseURL, svgBase64Encoded);
        return imageURI;
    }
}
