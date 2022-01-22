// stakeTokens
// unStakeTokens
// issueTokens
// addAllowedTokens
// getEthValue

//SPDX-Licence-Identifier: MIT
pragma solidity ^0.8.0;'

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";


contract TokenFarm is Ownable{
    // mapping token adress --> staker address -> amount
    mapping(address => mapping(address => uint256)) public stakingAmount


    // stakeTokens
    // unStakeTokens
    // issueTokens
    // addAllowedTokens
    // getEthValue
    address[] public allowedTokens;

    function stakeTokens(uint256 _amount, address _token) public {
        //what tokens can the stake
        // how much
        require(_amount > 0, "Amount must be more than 0");
        require(tokenIsAllowed(_token), "token is currently not allowed");
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);
        stakingBalance[_token][msg.sender] = stakingBalance[_token][msg.sender] + _amount;
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