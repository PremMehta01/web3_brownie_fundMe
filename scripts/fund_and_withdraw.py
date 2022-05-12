from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]  # use -1 to get the latest one.
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"The current entry fees is: {entrance_fee}")
    print("Funding...")

    fund_me.fund({"from": account, "value": entrance_fee})
    print("Congrats funded!!")


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("Withdrawing funded amount")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
