import { useEthers, useContractFunction } from "@usedapp/core";
import TokenFarm from "../chain-info/contracts/TokenFarm.json";
import networkMapping from "../chain-info/deployments/map.json";
import { constants, Contract, utils } from "ethers";
import { useEffect, useState } from "react";
import ERC20 from "../chain-info/contracts/MockERC20.json";

export const useStakeTokens = (tokenAddress: string) => {
  //approve
  //address of Farm and then token
  //abi
  //chainId
  const { chainId } = useEthers();
  const { abi } = TokenFarm;
  const TokenFarmAddress = chainId
    ? networkMapping[String(chainId)]["TokenFarm"][0]
    : constants.AddressZero;

  const tokenFarmInterface = new utils.Interface(abi);
  const TokenFarmContract = new Contract(TokenFarmAddress, tokenFarmInterface);

  const erc20ABI = ERC20.abi;

  const erc20Interface = new utils.Interface(erc20ABI);
  const erc20Contract = new Contract(tokenAddress, erc20Interface);

  const { send: approveErc20Send, state: approveAndStakeErc20State } =
    useContractFunction(erc20Contract, "approve", {
      transactionName: "Approve ERC20 Transfer",
    });
  const approveAndStake = (amount: string) => {
    setAmountToStake(amount);
    return approveErc20Send(TokenFarmAddress, amount);
  };

  const { send: stakeSend, state: stakeState } = useContractFunction(
    TokenFarmContract,
    "stakeTokens",
    {
      transactionName: "Stake Tokens",
    }
  );

  const [amountToStake, setAmountToStake] = useState("0");

  useEffect(() => {
    if (approveAndStakeErc20State.status === "Success") {
      stakeSend(amountToStake, tokenAddress);
    }
  }, [approveAndStakeErc20State, tokenAddress]);

  const [state, setState] = useState(approveAndStakeErc20State);

  useEffect(() => {
    if (approveAndStakeErc20State.status === "Success") {
      setState(stakeState);
    } else {
      setState(approveAndStakeErc20State);
    }
  }, [approveAndStakeErc20State, stakeState]);

  return { approveAndStake, state };
};
