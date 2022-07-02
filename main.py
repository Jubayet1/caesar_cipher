from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(text, shift, direction):
  if direction =='encode' or direction =='decode':
    if shift >26:
      shift = shift % 26
    new_text = ''
    for letter in text:
      if letter not in alphabet:
        new_text += letter
      else:
        position = alphabet.index(letter)
        if direction == 'encode':
          new_position = position + shift
          if new_position> 26:
            new_position = new_position - 26
        else:
          new_position = position - shift
        new_text += alphabet[new_position]
    print(new_text)
  else:
    print('Wrong Input')


ceaser(text, shift, direction)