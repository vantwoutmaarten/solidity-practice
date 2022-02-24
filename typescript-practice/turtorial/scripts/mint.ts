import '@nomiclabs/hardhat-ethers'
import { ethers } from "hardhat";

require("dotenv").config();

import contract from "../artifacts/contracts/BossNFT.sol/BossNFT.json";
const contractInterface = contract.abi;

let provider = ethers.provider;

// const tokenURI = "https://ipfs.io/ipfs/QmUFbUjAifv9GwJo7ufTB5sccnrNqELhDMafoEmZdPPng7";
const sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"

const privateKey = `0x${process.env.PRIVATE_KEY}`;
const wallet = new ethers.Wallet(privateKey, provider);
// wallet.provider = provider;
console.log("wallet provider: ", wallet.provider)
const signer = wallet.connect(provider);

const nft = new ethers.Contract(
    process.env.CONTRACT_ADDRESS? process.env.CONTRACT_ADDRESS : "0x000",
    contractInterface,
    signer
);

const main = () => {
    console.log("Waiting 5 blocks for confirmation...");
    nft
      .mintNFT(process.env.PUBLIC_KEY, sample_token_uri)
      .then((tx: { wait: (arg0: number) => any; }) => tx.wait(5))
      .then((receipt: { transactionHash: any; }) => console.log(`Your transaction is confirmed, its receipt is: ${receipt.transactionHash}`))
  
      .catch((e: any) => console.log("something went wrong", e));
  };
  
  main();