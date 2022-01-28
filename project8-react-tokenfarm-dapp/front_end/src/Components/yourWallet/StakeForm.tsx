import { useEthers, useTokenBalance, useNotifications } from "@usedapp/core";
import { Token } from "../Main";
import { formatUnits } from "@ethersproject/units";
import { Button, CircularProgress, Input, Snackbar } from "@material-ui/core";
import Alert from "@material-ui/lab/Alert";
import React, { useState, useEffect } from "react";
import { useStakeTokens } from "../../hooks";
import { utils } from "ethers";

export interface StakeFormProps {
  token: Token;
}

export const StakeForm = ({ token }: StakeFormProps) => {
  const { address: tokenAddress, name } = token;
  const { account } = useEthers();
  const tokenBalance = useTokenBalance(tokenAddress, account);
  const { notifications } = useNotifications();

  const formattedTokenBalance: number = tokenBalance
    ? parseFloat(formatUnits(tokenBalance, 18))
    : 0;
  const [amount, setAmount] = useState<
    number | string | Array<number | string>
  >(0);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const newAmount =
      event.target.value === "" ? "" : Number(event.target.value);
    console.log(newAmount);

    setAmount(newAmount);
  };

  const { approveAndStake, state } = useStakeTokens(tokenAddress);

  const handleStakeSubmit = () => {
    const amountAsWei = utils.parseEther(amount.toString());
    console.log("approvingandstaking!!!!!!!", amountAsWei.toString());
    return approveAndStake(amountAsWei.toString());
  };

  const isMining = state.status === "Mining";
  const [showErc20ApprovalSucces, setShowErc20ApprovalSucces] = useState(false);
  const [showStakeTokenSucces, setShowStakeTokenSucces] = useState(false);

  const handleCloseSnack = () => {
    setShowErc20ApprovalSucces(false);
    setShowStakeTokenSucces(false);
  };

  useEffect(() => {
    if (
      notifications.filter(
        (notification) =>
          notification.type === "transactionSucceed" &&
          notification.transactionName === "Approve ERC20 Transfer"
      ).length > 0
    ) {
      console.log("Approved!");
      setShowErc20ApprovalSucces(true);
    }
    if (
      notifications.filter(
        (notification) =>
          notification.type === "transactionSucceed" &&
          notification.transactionName === "Stake Tokens"
      ).length > 0
    ) {
      console.log("tokens staked");
      setShowStakeTokenSucces(true);
    }
  }, [notifications, showErc20ApprovalSucces, showStakeTokenSucces]);

  return (
    <React.Fragment>
      <div>
        <Input onChange={handleInputChange} />
        <Button
          color="primary"
          size="large"
          onClick={handleStakeSubmit}
          disabled={isMining}
        >
          {isMining ? <CircularProgress size={26} /> : "Stake!!!"}
        </Button>
        <Snackbar
          open={showErc20ApprovalSucces}
          autoHideDuration={5000}
          onClose={handleCloseSnack}
        >
          <Alert onClose={handleCloseSnack} severity="success">
            ERC20 token transfer approved! Now approve the 2nd transaction
          </Alert>
        </Snackbar>
        <Snackbar
          open={showStakeTokenSucces}
          autoHideDuration={5000}
          onClose={handleCloseSnack}
        >
          <Alert onClose={handleCloseSnack} severity="success">
            Tokens Staked!
          </Alert>
        </Snackbar>
      </div>
    </React.Fragment>
  );
};
