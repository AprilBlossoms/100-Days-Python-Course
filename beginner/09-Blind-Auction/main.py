import art
import os
clear = lambda: os.system('clear')
clear()


bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bidder = ""
  highest_bid = 0
  for bidder in bidding_record:
    if bidding_record[bidder] > highest_bid:
      highest_bid = bidding_record[bidder]
      highest_bidder = bidder
  print(f"The highest bidder is {highest_bidder}.")


print(art.logo)
while not bidding_finished:
  name = input("What is your name?")
  bid = input("What is your bid?")
  bids[name] = int(bid)
  should_continue = input("Are there any other bidders? Type yes or no.")
  if should_continue == "no":
    clear()
    bidding_finished = True
  else:
    clear()

find_highest_bidder(bids)