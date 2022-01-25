import React from "react";
import { DAppProvider, ChainId } from "@usedapp/core";
import { Header } from "./Components/header";
import { Container } from "@material-ui/core";

function App() {
  return (
    <DAppProvider
      config={{
        supportedChains: [ChainId.Kovan, ChainId.Rinkeby, 1337],
      }}
    >
      <div className="App">
        <Header />
        <Container maxWidth="md">
          <div>Hi</div>
        </Container>
      </div>
    </DAppProvider>
  );
}

export default App;
