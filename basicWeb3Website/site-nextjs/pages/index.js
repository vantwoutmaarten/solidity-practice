import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import { useWeb3Contract} from "react-moralis";
import {abi } from "../constants/abi"
export default function Home() {

  const {runContractFunction} = useWeb3Contract(
    {
      abi:  abi,
      contractAddress: "0x5FbDB2315678afecb367f032d93F642f64180aa3",
      functionName: "store",
      params: {
        _favoriteNumber: 778
      }
    }
  );

  return (
    <div className={styles.container}>
      <button onClick={() =>runContractFunction()}>store 778</button>
    </div>
  )
}
