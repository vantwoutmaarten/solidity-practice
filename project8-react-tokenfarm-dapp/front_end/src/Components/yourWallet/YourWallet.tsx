import { Token } from "../Main";
import { useState } from "react";
import { Box } from "@material-ui/core";
import { Tab } from "@material-ui/core";
import { TabContext, TabList, TabPanel } from "@material-ui/lab";
import { WalletBalance } from "./WalletBalance";

interface YourWalletProps {
  supportedTokens: Array<Token>;
}

export const YourWallet = ({ supportedTokens }: YourWalletProps) => {
  const [selectedTokenIndex, setSelectedTokenIndex] = useState<number>(0);

  const handleChange = (event: React.ChangeEvent<{}>, newValue: string) => {
    setSelectedTokenIndex(parseInt(newValue));
  };

  return (
    <Box>
      <h1>Your Wallet</h1>
      <Box>
        <TabContext value={selectedTokenIndex.toString()}>
          <Box>
            <TabList onChange={handleChange} aria-label="stake form tabs">
              {supportedTokens.map((token, index) => {
                return (
                  <Tab
                    label={token.name}
                    value={index.toString()}
                    key={index}
                  />
                );
              })}
            </TabList>
          </Box>
          {supportedTokens.map((token, index) => {
            return (
              <TabPanel value={index.toString()} key={index}>
                <div>
                  <WalletBalance token={supportedTokens[selectedTokenIndex]} />
                  2. big stake button
                </div>
              </TabPanel>
            );
          })}
        </TabContext>
      </Box>
    </Box>
  );
};
