alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(message, shift_amount, direction):
  return_message = ""
  for letter in message:
    if letter == " ":
      return_message += " "
    else:  
      position = alphabet.index(letter)
      if direction == 'encode':
        if position + shift_amount > 25:
          to_end = 26 - position
          new_shift = shift_amount - to_end
          new_position = 0 + new_shift
        else:
          new_position = position + shift_amount
      else:
        new_position = position - shift_amount
    return_message += alphabet[new_position]
  print(f"The {direction}d text is {return_message}.")

caesar(text, shift, direction)