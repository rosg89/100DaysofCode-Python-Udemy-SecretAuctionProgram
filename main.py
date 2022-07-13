from replit import clear
#HINT: You can call clear() to clear the output in the console.

#Importo el logo
from art import logo
print(logo)

#Creo el diccionario
bids = {}

#Hago una función para encontrar el highest bidder
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

#Creamos un loop
bidding_finished = False

while not bidding_finished:
  #Pido los datos
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  #Agregamos al diccionario
  bids[name] = price
  #Preguntamos si hay otros users
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue =="yes":
    clear()


    