from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENT,
)
from web3 import Web3


def deploy_fund_me():
    account = get_account()

    price_feed_address = get_price_feed_address()

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def get_price_feed_address():
    # If we are on persistent network(not local) like rinkeby, use the associated address
    # otherwise deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        return config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        return MockV3Aggregator[-1].address


def main():
    deploy_fund_me()
