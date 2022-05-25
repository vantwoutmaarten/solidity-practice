import { ConnectButton } from "web3uikit";

export default function Header() {
    return (
        <nav>
            <ConnectButton moralisAuth={false}/>
        </nav>
    )
}