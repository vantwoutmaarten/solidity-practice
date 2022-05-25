// working with ethers.js and to do a require we are:
// yarn add browserify
// yarn add ethers
// yarn browserify index.js --standalone bundle -o ./dist/bundle.js
// const {ethers } = require('ethers');
const { getContractAddress } = require('@ethersproject/address');
const {ethers } = require('ethers');

async function connect() {
    if (typeof window.ethereum !== "undefined"){
        await window.ethereum.request({method: "eth_requestAccounts"})
        document.getElementById("connectButton").innerHTML = "Connected";
    }
}

async function store() {
    if(typeof window.ethereum !== "undefined"){
    // address
    // abi
    const address = "0x5FbDB2315678afecb367f032d93F642f64180aa3";
    const abi = [
        {
          "inputs": [
            {
              "internalType": "string",
              "name": "_name",
              "type": "string"
            },
            {
              "internalType": "uint256",
              "name": "_favoriteNumber",
              "type": "uint256"
            }
          ],
          "name": "addPerson",
          "outputs": [],
          "stateMutability": "nonpayable",
          "type": "function"
        },
        {
          "inputs": [
            {
              "internalType": "string",
              "name": "",
              "type": "string"
            }
          ],
          "name": "nameToFavoriteNumber",
          "outputs": [
            {
              "internalType": "uint256",
              "name": "",
              "type": "uint256"
            }
          ],
          "stateMutability": "view",
          "type": "function"
        },
        {
          "inputs": [
            {
              "internalType": "uint256",
              "name": "",
              "type": "uint256"
            }
          ],
          "name": "people",
          "outputs": [
            {
              "internalType": "uint256",
              "name": "favoriteNumber",
              "type": "uint256"
            },
            {
              "internalType": "string",
              "name": "name",
              "type": "string"
            }
          ],
          "stateMutability": "view",
          "type": "function"
        },
        {
          "inputs": [],
          "name": "retrieve",
          "outputs": [
            {
              "internalType": "uint256",
              "name": "",
              "type": "uint256"
            }
          ],
          "stateMutability": "view",
          "type": "function"
        },
        {
          "inputs": [
            {
              "internalType": "uint256",
              "name": "_favoriteNumber",
              "type": "uint256"
            }
          ],
          "name": "store",
          "outputs": [],
          "stateMutability": "nonpayable",
          "type": "function"
        }
      ];
          const provider = new ethers.providers.Web3Provider(window.ethereum);
          console.log(provider);
          const signer = provider.getSigner();
          console.log(signer);
          const contract = new ethers.Contract(address, abi, signer);
          console.log(contract);
    try {
        await contract.store(77);
    } catch (error) {
        console.log(error);
    }
    }
}

async function retrieve() {

  if(typeof window.ethereum !== "undefined"){
    // address
    // abi
    const address = "0x5FbDB2315678afecb367f032d93F642f64180aa3";
    const abi = [
        {
          "inputs": [
            {
              "internalType": "string",
              "name": "_name",
              "type": "string"
            },
            {
              "internalType": "uint256",
              "name": "_favoriteNumber",
              "type": "uint256"
            }
          ],
          "name": "addPerson",
          "outputs": [],
          "stateMutability": "nonpayable",
          "type": "function"
        },
        {
          "inputs": [
            {
              "internalType": "string",
              "name": "",
              "type": "string"
            }
          ],
          "name": "nameToFavoriteNumber",
          "outputs": [
            {
              "internalType": "uint256",
              "name": "",
              "type": "uint256"
            }
          ],
          "stateMutability": "view",
          "type": "function"
        },
        {
          "inputs": [
            {
              "internalType": "uint256",
              "name": "",
              "type": "uint256"
            }
          ],
          "name": "people",
          "outputs": [
            {
              "internalType": "uint256",
              "name": "favoriteNumber",
              "type": "uint256"
            },
            {
              "internalType": "string",
              "name": "name",
              "type": "string"
            }
          ],
          "stateMutability": "view",
          "type": "function"
        },
        {
          "inputs": [],
          "name": "retrieve",
          "outputs": [
            {
              "internalType": "uint256",
              "name": "",
              "type": "uint256"
            }
          ],
          "stateMutability": "view",
          "type": "function"
        },
        {
          "inputs": [
            {
              "internalType": "uint256",
              "name": "_favoriteNumber",
              "type": "uint256"
            }
          ],
          "name": "store",
          "outputs": [],
          "stateMutability": "nonpayable",
          "type": "function"
        }
      ];
          const provider = new ethers.providers.Web3Provider(window.ethereum);
          console.log(provider);
          const signer = provider.getSigner();
          console.log(signer);
          const contract = new ethers.Contract(address, abi, signer);
          console.log(contract);
    try {
        console.log((await contract.retrieve()).toString());
    } catch (error) {
        console.log(error);
    }
    }
}

module.exports = {
    connect,
    store,
    retrieve
}