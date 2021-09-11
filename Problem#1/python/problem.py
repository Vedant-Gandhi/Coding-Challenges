import time
def get_recurrent_character(input_string):
    all_chars=set() 
    insertions=[]

    for letter in input_string[-1::-1]:
        if not letter in all_chars:
            insertions.append(letter)
            all_chars.add(letter)
        else :
            try:
                insertions.remove(letter)
            except :
                ''
    if len(insertions) == 0:
        return None
    return insertions[-1]

stringData=input("Enter the string:")
print(f'Detected Letter {print(get_recurrent_character('race'))}')