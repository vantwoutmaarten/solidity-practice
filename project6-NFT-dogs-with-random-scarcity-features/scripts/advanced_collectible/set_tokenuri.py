from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import OPENSEA_URL, get_account, get_breed

tokenId_metadata_dic = {
    0: "https://ipfs.io/ipfs/QmUQjup5E5KAESEFmNQmc9c5BtGA4Z1vpeY4b5VzhA73Ne?filename=0-ST_BERNARD.json",
    1: "https://ipfs.io/ipfs/QmUQjup5E5KAESEFmNQmc9c5BtGA4Z1vpeY4b5VzhA73Ne?filename=1-ST_BERNARD.json",
    2: "https://ipfs.io/ipfs/QmdJHLooxHfbzk6ZsVFrpyq1HQpcQSb97T1YC6HaJxZwCQ?filename=2-SHIBA_INU.json",
    3: "https://ipfs.io/ipfs/QmUQjup5E5KAESEFmNQmc9c5BtGA4Z1vpeY4b5VzhA73Ne?filename=3-ST_BERNARD.json",
    4: "https://ipfs.io/ipfs/QmdJHLooxHfbzk6ZsVFrpyq1HQpcQSb97T1YC6HaJxZwCQ?filename=4-SHIBA_INU.json",
    5: "https://ipfs.io/ipfs/QmeYmgiRSE3VJFE51BRNgMz4SAAGQC3AU5111zcn1GR2oy?filename=5-HAPPY_PUG.json",
}


def main():
    print(f"working on {network.show_active()}")
    advanced_collectible = AdvancedCollectible[-1]
    number_of_collectibles = advanced_collectible.tokenCounter()
    print(f"there are {number_of_collectibles} tokenIds")

    for token_id in range(number_of_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("http"):
            print(f"Set tokenURI of {token_id}")
            set_tokenURI(token_id, advanced_collectible, tokenId_metadata_dic[token_id])


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"Awesome! view NFT now at opensea: {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
