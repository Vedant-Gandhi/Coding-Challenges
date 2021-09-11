import time
def get_recurrent_character(input_string):
    all_chars=set() 
    insertions=[]

    for letter in input_string[-1::-1]:
        if not letter in all_chars:
          insertions.insert(0,letter)
          all_chars.add(letter)
        else :
            try:
                if(insertions [0] == letter):
                    insertions.pop(0)
            except :
                ''
    if len(insertions) == 0:
        return None
    return insertions[0]

stringData=input("Enter the string:")
print(f'Detected Letter {(get_recurrent_character(stringData))}')