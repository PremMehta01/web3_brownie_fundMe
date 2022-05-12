from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000

# you can see all env of brownie by running "brownie networks list" in terminal
LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]
FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork"]


# If blockchain env is local or forked then get the address from loal
# basically the 0th index address
# else take the address from the brownie-config.yaml file
def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT
        or network.show_active() in FORKED_LOCAL_ENVIRONMENT
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


# we need to deploy mocks for getting local price_feed
def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")

    # check if MockV3Aggregator is deploying for the first time.
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()}
        )

    print("Mocks Deployed!")
