import chai, { expect } from "chai";
import { ethers } from "hardhat";
import { solidity } from "ethereum-waffle";

import { BossNFT } from "../typechain-types/BossNFT"

chai.use(solidity);

describe.only("BossNFT", () => {
    let bossNFT: BossNFT;

    beforeEach(async () => {
        // 1
        const signers = await ethers.getSigners();
        // 2
        const bossNFTFactory = await ethers.getContractFactory("BossNFT", signers[0])
        bossNFT = (await bossNFTFactory.deploy("CypherPunk", "CYP")) as BossNFT;
        await bossNFT.deployed();
    })
    describe("Deployment", async () => {
        it("should be deployed to a properaddress", async () => {
            expect(bossNFT.address).to.properAddress;
        })
    });

    describe("correct name and symbol", async () => {
        //3
        it("should return correct name", async () => {
            expect(await bossNFT.name()).to.equal("CypherPunk");
        })
        //3
        it("should return the correct symbol", async () => {
            expect(await bossNFT.symbol()).to.equal("CYP");
        })
    })

    describe("Minting", async () => {
        it("should be mintable and then have an owner", async () => {
            expect(await bossNFT).to.equal("CypherPunk");
        })
    });
})