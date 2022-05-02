# Tokenizer <br>
This project is a Chainlink, 2021 Fall Hackathon winner. https://devpost.com/software/erc-20-erc-721-token-minter-gui <br>
<br>
<br>
This project gives users an all in one NFT creation experience, and consists of two smart contracts. The first is a NFT Factory contract that depends on OpenZeppelin's ERC-721 libraries. The second is an ERC-20 token contract that incentivizes users to mint their NFT's through the program. Users can apply basic style filters to their .PNG or .JPG, give a name and description, and mint it onto an EVM compatible blockchain. When a user mints an NFT, they are awarded 1 to 15 ERC-20 tokens, determined randomly by a Chainlink VRF oracle.

This project is still in its infancy, so no smart contracts exist on-chain, however, both contracts are provided in the repo and can be deployed to test the GUI's functionality. Steps are provided below. <br>

*NOTE: This has only been tested on the Rinkeby network* 

# Project Requirements <br>
1) MetaMask - https://metamask.io/faqs/ <br> 
 - Obtain Rinkeby ETH and Rinkeby LINK - https://faucets.chain.link/rinkeby <br>
3) Provider (choose one from below): <br> 
 - Infura - https://infura.io/ <br>
 - Alchemy - https://www.alchemy.com/ <br>
 - Moralis - https://moralis.io/speedy-nodes/ <br> 
4) Etherscan API Key - https://etherscan.io/myapikey <br>
5)  Pinata API key and secret - https://docs.pinata.cloud/
6)  IPFS command-line - https://docs.ipfs.io/install/command-line/#official-distributions

# Setup Steps <br>

### 1) Clone repository <br>
~~~
git clone https://github.com/McManOfTheLand/ERC721-ERC-20-Token-Minter
~~~
### 2)  Create and activate python virtual enviroment <br>
~~~
python3 -m venv venv
./venv/scripts/activate
~~~
### 3)  Install packages <br>
~~~
pip install -r requirements.txt
~~~

### 4) Create .env file <br>
Inside the root directory of your project, create a .env file. Add API keys as well as your MetaMask accounts private key.
![](ReadmePhotos/env_setup.PNG ".env file populated with necessary information")
 
### 5) Deploy contracts <br>
To set the name and symbol for smart contracts, navigate to the `ERC721-ERC-20-Token-Minter/scripts/deploy_contracts.py` file and change the deployment parameters that will ultimately get passed to the smart contract's constructor. <br>
Deploy contracts to the Rinkeby network:
~~~
brownie run scripts/deploy_contracty.py --network rinkeby
~~~
A successful deployment to the Rinkeby test network should look something like this: <br>
![](ReadmePhotos/deployment_success.png "Console output on deployment success") <br>
### 6) Fund ERC-20 token contract instance with LINK<br>
This is an imperative step. Not doing so will result in the program crashing when you try and mint an NFT. <br> 
### 7) Start IPFS server <br>
In a new terminal, run the command: <br>
~~~
ipfs daemon
~~~
### 8) Start GUI <br> 
Run the command: <br>
~~~
brownie run scripts/start_gui.py --network rinkeby
~~~
### 9) Get image from local storage <br> 
Click on the "Browse" button to select an image with the file extension .PNG or .JPG. <br>
![](ReadmePhotos/browse_btn.PNG "Click the Browse button to select an image") <br>
### 10) Stage an image <br> 
Select a style using the checkboxs. Then, click "Stage" to add the image to the minting area with the style you've selected. If you want to unstage an image, click "delete", and it will be removed from the minting area.
![](ReadmePhotos/stage_actions.PNG "Click the Stage button to apply the style to the image") <br>
### 11) Give your NFT a name and description <br>
Use the provided dialogue boxes to give a name and description to your NFT.
![](ReadmePhotos/mint_actions.PNG "Provide a name and description to your NFT")<br>
### 12) Completion 
If you followed the above steps correctly, your console should look something like this:
![](ReadmePhotos/mint_success.PNG "Console output on minting success")

### A successfull transaction means <br>
You can view your NFT at https://testnets.opensea.io/account (make sure you are connected to the OpenSea rinkeby testnet). <br>
Your wallet gains from 1 and 15 ERC-20 Tokens from the contract you previously deployed.

Blockchains can take time. If you are not seeing your NFT or tokens immedietly, check back in several mintutes.
## Congragulations. You've done it!




