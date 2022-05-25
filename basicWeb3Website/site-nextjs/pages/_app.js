import '../styles/globals.css'
import Header from '../components/Header'
import { MoralisProvider } from "react-moralis";

function MyApp({ Component, pageProps }) {
  return (
  <MoralisProvider initializeOnMount={false}>
    <Header/>
 <Component {...pageProps} />
  </MoralisProvider>
  )
}

export default MyApp
