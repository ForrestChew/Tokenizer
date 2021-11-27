# This file contains supporting functions used within other scripts.
# This file can also be run with <brownie run PATH/TO/utils.py> to obtain various info on deployed contracts
import sys
sys.path.append("nft_creator_gui/metadata_info")
from brownie import ERC20Token, NftFactory, accounts, network, config

LOCAL_BLOCKCHAIN_ENVIROMENTS = ["development", "mainnet-fork"]

#gets account based on what network contract is deployed to
def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIROMENTS:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])

#Reads the file path of image to be minted
def create_nft_metadata():
    with open("nft_creator_gui/TextFiles/nft_name.txt", "r") as name_metadata:
        name = name_metadata.read()
    with open("nft_creator_gui/TextFiles/nft_description.txt", "r") as description_metadata:
        description = description_metadata.read()

    metadata_dictionary["name"] = name
    metadata_dictionary["description"] = description
    print(metadata_dictionary)

def get_latest_info_on_contracts():
    token_contract = ERC20Token[-1]
    nft_contract = NftFactory[-]
    print(f"  Token address is: {contract_instance.address}")
    print(f"  NFT Factory address is: {nft_contract.address}")



def main():
    get_latest_token_address()