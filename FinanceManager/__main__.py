import argparse
from Lib import util

desc = "A simple CLI tool to assist in finance management. Written in Python."

parser = argparse.ArgumentParser(description=desc)
subParsers = parser.add_subparsers(help='Available Commands')
init = subParsers.add_parser('init', help='Run before using anything else to set up data storage for things, only needs to be run once though.')
deposit = subParsers.add_parser('deposit', help='Deposit a value into your account')
spend = subParsers.add_parser('spend', help="Removes a value from the spendable part of your account. Throws an error if you don't have enough.")
deposit.add_argument('DepositValue', type=int, help='Amount to deposit.')
spend.add_argument('SpendValue', type=int, help='Amount to spend.')

parser.parse_args()