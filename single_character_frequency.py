import operator #to sort the dict in descending order easily
#Single Character's Occurrence

#Takes input from user or either store the input in a variable or in a file.txt
# file= open("Cryptogram.txt")
# for x in file:
#     Cryptogram= x
# Cryptogram= Cryptogram.replace("\n", "")
# Cryptogram= Cryptogram.replace(" ", "")
# Cryptogram = Cryptogram.casefold() #casefold to ignore the case

Cryptogram= input("Enter the cryptogram: \n")
Cryptogram = Cryptogram.casefold() #casefold to ignore the case

#Made a Dictionary with the name of frequency
frequency = {}
#Loop for counting characters in the given input and displaying the key-value pair in dictionary
for i in Cryptogram:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
sorted_d = dict( sorted(frequency.items(), key=operator.itemgetter(1),reverse=True))

#Displaying the result(occurence of each single character) 
print ("Count of each single character is :\n" ,  sorted_d)


#Vowels Occurence


def Count_Vowels(Cryptogram, vowels):
     
    Cryptogram = Cryptogram.casefold() #casefold to ignore the case
    count = {}.fromkeys(vowels, 0)
    for character in Cryptogram:
        if character in count:
            count[character] += 1   
    return count
     
vowels = "aeiou"
Cryptogram= Cryptogram.replace("\ufeff", "")

print ("The Count of each vowel in the file is:\n", Count_Vowels(Cryptogram, vowels))


#Digraphs occurence in the cryptogram
n = 2
split_strings = [Cryptogram[index : index + n] for index in range(0, len(Cryptogram)-n+1)]
d = {x:split_strings.count(x) for x in split_strings}
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print ("The Digrpahs and their occurence is:\n",sorted_d)


#Polygraphs occurence 
n=3
split_strings = [Cryptogram[index : index + n] for index in range(0, len(Cryptogram)-n+1)]
d1 = {x:split_strings.count(x) for x in split_strings}
d1 = dict( sorted(d1.items(), key=operator.itemgetter(1),reverse=True))
print ("The three letters pairs and their occurence is:\n",d1)


n=4
split_strings = [Cryptogram[index : index + n] for index in range(0, len(Cryptogram)-n+1)]
d2 = {x:split_strings.count(x) for x in split_strings}
d2 = dict( sorted(d2.items(), key=operator.itemgetter(1),reverse=True))
print ("The four letters pairs and their occurence is:\n",d2)



n = 5
split_strings = [Cryptogram[index : index + n] for index in range(0, len(Cryptogram)-n+1)]
d3 = {x:split_strings.count(x) for x in split_strings}
d3 = dict( sorted(d3.items(), key=operator.itemgetter(1),reverse=True))
print ("The five letters pairs and their occurence is:\n",d3)

 

