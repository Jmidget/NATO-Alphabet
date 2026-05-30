import pandas
# Reads in NATO alphabet csv file then converts the letter column and code column into a dictionary
data = pandas.read_csv('nato_phonetic_alphabet.csv')
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}

# Asks the user for a word, then breaks down each letter of the word with a corresponding NATO code word and prints the result
while True:
    try:
        NATO = [data_dict[x] for x in input('Enter a Word: ').upper()]
        break
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
print(NATO)
