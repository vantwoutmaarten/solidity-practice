const number = 43;

const lazyminter = new LazyMinter({ myDeployedContract.address, signerForMinterAccount });

async createVoucher(tokenId, uri, minPrice = 0) {
    const voucher = { tokenId, uri, minPrice }
    const domain = await this._signingDomain()
    const types = {
      NFTVoucher: [
        {name: "tokenId", type: "uint256"},
        {name: "minPrice", type: "uint256"},
        {name: "uri", type: "string"},  
      ]
    }
    const signature = await this.signer._signTypedData(domain, types, voucher)
    return {
      ...voucher,
      signature,
    }
  }