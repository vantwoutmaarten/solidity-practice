const { deployments, getNamedAccounts, getChainId, ethers, network } = require("hardhat")
const fs = require("fs")
let {networkConfig} = require('../helper-hardhat-config');

module.exports = async({
    getNamedAccounts,
    deployments,
    getChainId
}) => {
    const {deploy, log} = deployments
    const {deployer} = await getNamedAccounts()
    const chainId = await getChainId()

    log("---------------------------------------")
    const SVGNFT = await deploy("NFT_StorageOpt", {
        from: deployer,
        log: true
    })
    log(`You have deployed an NFT Contract to ${SVGNFT.address}`)
    let filepath = "./img/triangle.svg";
    let svg = fs.readFileSync(filepath, { encoding: "utf8" });

    const svgNFTContract = await ethers.getContractFactory("NFT_StorageOpt");
    const accounts = await ethers.getSigners();
    const signer = accounts[0];

    const svgNFT = new ethers.Contract(SVGNFT.address, svgNFTContract.interface, signer);
    log("--------------------.", chainId);
    log(networkConfig)
    log(networkConfig[chainId])
    log("shown chainId")
    const networkName = networkConfig[chainId]['name']
    log(`Verify with \n npx hardhat verify --network ${network.name} ${svgNFT.address}`)

    let transactionResponse = await svgNFT.create(svg);
    console.log("transaction send out")
    console.log("transactionResponse: ", transactionResponse);
    let receipt = await transactionResponse.wait(1);
    log(`You've made an NFT!`)

    log(`You can view the tokenURI here ${await svgNFT.tokenURI(0)}`);
}