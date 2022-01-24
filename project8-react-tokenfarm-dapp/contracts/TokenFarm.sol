// stakeTokens
// unStakeTokens
// issueTokens
// addAllowedTokens
// getEthValue

//SPDX-Licence-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";


contract TokenFarm is Ownable{
    // mapping token adress --> staker address -> amount 
    mapping(address => mapping(address => uint256)) public stakingAmount;
    mapping(address => uint256) public uniqueTokensStaked;

    mapping(address => address) public tokenPriceFeedMapping;
    
    address[] public allowedTokens;
    address[] public stakers;

    IERC20 public dappToken;

    // stakeTokens
    // unStakeTokens
    // issueTokens
    // addAllowedTokens
    // getEthValue

    constructor(address _dappTokenAddress) {
        dappToken = IERC20(_dappTokenAddress);
    }

    function unStakeTokens(address _token) public {
        uint256 balance = stakingAmount[msg.sender][_token];
        require(balance > 0, "staking balance cannt be zero");
        IERC20(_token).transfer(msg.sender, balance);
        stakingAmount[msg.sender][_token] = 0;
        uniqueTokensStaked[msg.sender] = uniqueTokensStaked[msg.sender] - 1;
    }


    function setPriceFeedContract(address _token, address _pricefeed) public onlyOwner {
        tokenPriceFeedMapping[_token] = _pricefeed;
    }

    function issueTokens() public onlyOwner {
        // Issue tokens to all stakers
        for(uint256 stakersIndex = 0; stakersIndex < stakers.length; stakersIndex++){
            address recipient = stakers[stakersIndex];
            uint256 userTotalValue = getUserTotalValue(recipient);
            dappToken.transfer(recipient, userTotalValue);
        }
    }

    function getUserTotalValue(address _user) public view returns (uint256){
        uint256 totalValue = 0;
        require(uniqueTokensStaked[_user]>0, "no tokens staked");
        
        for(uint256 allowedTokensIndex = 0; allowedTokensIndex<allowedTokens.length; allowedTokensIndex++){
            totalValue = totalValue + getUserSingleTokenValue(_user, allowedTokens[allowedTokensIndex]);
        }
        return totalValue;
    }

    function getUserSingleTokenValue(address _user, address _token) public view returns(uint256) {
        if (uniqueTokensStaked[_user] <= 0){
            return 0;
        }
        (uint256 priceOfToken, uint256 decimals) = getTokenValue(_token);
        uint256 amountoftoken = stakingAmount[_user][_token];

        return (stakingAmount[_user][_token] * priceOfToken / (10**decimals));

    }

    function getTokenValue(address _token) public view returns (uint256, uint256){
        // priceFeedAddress
        address priceFeedAddress = tokenPriceFeedMapping[_token];
        AggregatorV3Interface priceFeed = AggregatorV3Interface(priceFeedAddress);
        (,int256 price,,,) = priceFeed.latestRoundData();
        uint256 decimals = priceFeed.decimals();
        
        return (uint256(price), decimals);
    }

    function stakeTokens(uint256 _amount, address _token) public {
        //what tokens can the stake
        // how much
        require(_amount > 0, "Amount must be more than 0");
        require(tokenIsAllowed(_token), "token is currently not allowed");
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);
        updateUniqueTokensStaked(msg.sender, _token);
        if (uniqueTokensStaked[msg.sender] == 1){
            stakers.push(msg.sender);
        }
        stakingAmount[msg.sender][_token] = stakingAmount[msg.sender][_token] + _amount;
    }

    function updateUniqueTokensStaked(address _user, address _token) internal {
        if (stakingAmount[_user][_token] <= 0){
            uniqueTokensStaked[_user] = uniqueTokensStaked[_user] + 1;
        }
    }

    function tokenIsAllowed(address _token) public returns (bool) {
        for ( uint256 addAllowedTokensIndex=0; addAllowedTokensIndex < allowedTokens.length; addAllowedTokensIndex++){
            if(allowedTokens[addAllowedTokensIndex] == _token){
               return true; 
            }
        }
        return false;
    }

    function addAllowedTokens(address _token) public onlyOwner {
        allowedTokens.push(_token);
    }

}