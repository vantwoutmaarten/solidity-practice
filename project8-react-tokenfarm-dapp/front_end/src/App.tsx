import React from "react";
import {
  DAppProvider,
  Kovan,
  Rinkeby,
  Localhost,
  useNotifications,
} from "@usedapp/core";
import { Header } from "./Components/Header";
import { Container } from "@material-ui/core";
import { Main } from "./Components/Main";

function App() {
  return (
    <DAppProvider
      config={{
        networks: [Kovan, Rinkeby, Localhost],
        notifications: {
          expirationPeriod: 1000,
          checkInterval: 1000,
        },
      }}
    >
      <div className="App">
        <Header />
        <Container maxWidth="md">
          <div>Hi</div>
          <Main />
        </Container>
      </div>
    </DAppProvider>
  );
}

export default App;
