// SPDX-License-Identifier: MIT

pragma solidity >=0.6.6 <0.9.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    
    mapping(address => uint256) public addressToAmountFunded;
    
    address[] public funders;
    address public owner;
    
    constructor() public {
        owner = msg.sender;    
    }
    

    function fund() public payable {
        // $50 
        uint256 minimumUSD = 50 * 10**18;
        require(getConversionRate(msg.value) >= minimumUSD, "You need to spend more ETH!");
        
        
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
        // what the ETH  -> USD conversion rate
    }
    
    function getVersion() public view returns(uint256){
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        return priceFeed.version();
    }
    
    function getPrice() public view returns(uint256){
        AggregatorV3Interface pricefeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        (,int256 answer,,,)
         = pricefeed.latestRoundData();
         return uint256(answer*10000000000);
    }

    //1000000000
    function getConversionRate(uint256 ethAmount) public view returns (uint256){
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUSD = (ethPrice * ethAmount) / 1000000000000000000;
        return ethAmountInUSD;
    }
    
    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }
    
    function withdraw() payable onlyOwner public {
        //msg.sender is the one who calls the function
        // only the admin should be able to rug the contract:)))!
        payable(msg.sender).transfer(address(this).balance);
        for (uint256 funderIndex=0; funderIndex < funders.length; funderIndex++){
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }
        funders = new address[](0);
    }
    
    

}