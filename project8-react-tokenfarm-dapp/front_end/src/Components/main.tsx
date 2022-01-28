/* eslint-disable spaced-comment */
/// <reference types="react-scripts" /
import { useEthers } from "@usedapp/core";
import helperConfig from "../helper-config.json";
import networkMapping from "../chain-info/deployments/map.json";
import { constants } from "ethers";
import brownieConfig from "../brownie-config.json";
import dapp from "../dapp.png";
import dai from "../dai.png";
import weth from "../eth.png";
import { YourWallet } from "./yourWallet";
import { makeStyles } from "@material-ui/core";

export type Token = {
  image: string;
  address: string;
  name: string;
};

const useStyles = makeStyles((theme) => ({
  title: {
    color: theme.palette.common.white,
    textAlign: "center",
    padding: theme.spacing(4),
  },
}));

export const Main = () => {
  const classes = useStyles();

  // show token values from the wallet

  // Get the address of different tokens
  // Get the balance of the users wallet

  // send the Brownie-config to the src folder
  // send the build folder, this has access to the dapp token address and the mock addresses.
  const { chainId } = useEthers();
  const networkName = chainId ? helperConfig[chainId] : "dev";
  const dappTokenAddress = chainId
    ? networkMapping[String(chainId)]["DappToken"][0]
    : constants.AddressZero;
  const wethTokenAddress = chainId
    ? brownieConfig["networks"][networkName]["weth_token"]
    : constants.AddressZero;
  const fauTokenAddress = chainId
    ? brownieConfig["networks"][networkName]["fau_token"]
    : constants.AddressZero;

  const supportedTokens: Array<Token> = [
    {
      image: dapp,
      address: dappTokenAddress,
      name: "DAPP",
    },
    {
      image: dai,
      address: fauTokenAddress,
      name: "DAI",
    },
    {
      image: weth,
      address: wethTokenAddress,
      name: "WETH",
    },
  ];

  return (
    <div>
      <h2 className={classes.title}>Dapp Token App</h2>
      <YourWallet supportedTokens={supportedTokens} />
    </div>
  );
};
