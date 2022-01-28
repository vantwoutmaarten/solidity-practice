pragma solidity ^0.8.0;

import '@openzeppelin/contracts/token/ERC20/ERC20.sol';

contract MockERC20 is ERC20 {
  constructor(string memory _name, string memory _symbol) public ERC20(_name, _symbol) {}

  function mint(address to, uint amount) public {
    _mint(to, amount);
  }

  function burn(address from, uint amount) public {
    _burn(from, amount);
  }
}