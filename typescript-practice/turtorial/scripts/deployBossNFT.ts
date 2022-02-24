import { ethers } from "hardhat";

async function main() {
    const bossNFTFactory = await ethers.getContractFactory("BossNFT");

    let bossNFT = await bossNFTFactory.deploy("CyperPunkBoss", "CPB");

    await bossNFT.deployed();

    console.log("Deployed BossNFT to ", bossNFT.address);
}

main()