import '@nomiclabs/hardhat-ethers'
import { ethers } from "hardhat";

require("dotenv").config();

import contract from "../artifacts/contracts/BossNFT.sol/BossNFT.json";
const contractInterface = contract.abi;

let provider = ethers.provider;

const sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"

const privateKey = `0x${process.env.PRIVATE_KEY}`;
const wallet = new ethers.Wallet(privateKey, provider);
const signer = wallet.connect(provider);
const contractAddress = process.env.CONTRACT_ADDRESS!;


const nft = new ethers.Contract(
    contractAddress,
    contractInterface,
    signer
);

if (!contractAddress) {
    throw new Error("Please set your CONTRACT_ADDRESS in a .env file");
}


const main = () => {
    console.log("Waiting 5 blocks for confirmation...");
    nft
      .mintNFT(process.env.PUBLIC_KEY, sample_token_uri)
      .then((tx: { wait: (arg0: number) => any; }) => tx.wait(5))
      .then((receipt: { transactionHash: any; }) => console.log(`Your transaction is confirmed, its receipt is: ${receipt.transactionHash}`))
  
      .catch((e: any) => console.log("something went wrong", e));
  };
  
  main();