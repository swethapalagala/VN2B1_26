print("---------String Functions--------")
a="sweety"
b=a.capitalize()     #uppercase the first letter in this sentence
print("1.",b)

a="HELLO GUYS"
b=a.casefold()       #make the string lowercase
print("2.",b)

a="This Is Center"
b=a.center(40)       #Returns a centered string
print("3.",b)

a="This Is Count"
b=a.count('s')        #Returns the number of times a specified value occurs in a string
print("5.",b)

b=a.encode()
print("5.",b)        #Returns an encoded version of the string

b=a.endswith("t")     #Returns true if the string ends with the specified value
print("6.",b)

a="This Is E\txp\tandtabs"
b=a.expandtabs(1)            #Sets the tab size of the string
print("7.",b)

b=a.find('E')
print("8.",b)             #Searches the string for a specified value and returns the position of where it was found

b=a.format()
print("9.",b)               #Format specified values in a string

b=a.index("is")
print("10.",b)             #Searches the string for a specified value and returns the position of where it was found

a="ThisIsisa1num46"
b=a.isa1num()              #check if all the characters in the text are alphanumeric:
print("11.",b)

a="ThisIsisa1num"
b=a.isalpha                #Check if all the characters in the text are letters:
print("12.",b)

b=a.isascii()
print("13.",b)               #Returns True if all characters in the string are ascii characters

a='\u0033'
b=a.isdecimal()                #Returns True if all characters in the string are decimals
print("14.",b)

a=('6666')
b=a.isdigit()                 #Returns True if all characters in the string are digits
print("15.",b)

a="Video"
b=a.isidentifier()           #Returns True if the string is an identifier
print("16.",b)

a="swetha"
b=a.islower()               #check if all the characters in the text are in lowercase:
print("17.",b)

a="12345"
b=a.isnumeric()             #check if all the characters in the text are numeric:
print("18.",b)


a="Hi Guys Hru #@1!"
b=a.isprintable()           #check if all the characters in the text are printable:
print("19.",b)

a=" "
b=a.isspace()              #check if all the characters in the text are whitespaces:
print("20.",b)

a="Hi How R You"
b=a.istitle()               #Returns True if the string follows the rules of a title
print("21.",b)

a="HI HOW R YOU"
b=a.isupper()               #Returns True if all characters in the string are upper case
print("22.",b)

a=("Varun","Aaria","Nikhil")
b=' '.join(a)                   #Join all items in a tuple into a string,using a hash character as separator:
print("23.",b)

a="Uday"
b=a.1just(10)                   #Return a 10 characters long,left justified version of the word "Swetha":
print("24.",b,"Beautiful")

a="She IS BEAUTIFUL"
b=a.lower()                    #coverts a string into lower case
print("25.",b)

a="    swetha   "
b=a.1strip()                  #Returns a left trim version of the string
print("26. Hello ",b,"Looking Beautiful")

a="Hi Swetha"
b=a.maketrans("S","W"          #create a mapping table,and use it in the translate () method to replace any "S" characters with "w" character:
print("27.",a.translate(b))

a="She Is A Good Girl"
b=a.partition("Swetha")       #Returns a tuple where the string is parted into three parts
print("28.",b)

a="All is All"
b=a.replace("All","Swetha")
print("29.",b)          #Returns a string where a specified value is replaced with a specified value

a="Swetha, Have Oneplus9r."
b=a.rfind("Have")       #Where in the text is the last occurrence of the string "Have"?:
print("30.",b)

b=a.rindex("Oneplus9r")
print("31.",b)

a="She Is Beautiful"
b=a.rpartition("Beautiful")
print("32.",b)          #Returns a tuple where the string is parted into three parts

a="She,Is,Beautiful"
b=a.rsplit(", ")        #Splits the string at the specified separator, and returns a list
print("33.",b)

a="She Is Beautiful"
b=a.rstrip()            #Remove any white spaces at the end of the string:
print("34. She",b,'Is Beautiful')

a="Welcome To Pycham"
b=a.split()             #Split a string into a list where each word is a list item:
print("35.",b)

a="She Is\ Beautiful"
b=a.splitlines()        #Splits the string at line breaks and returns a list
print("36.",b)

b=a.startswith("She")  #Returns true if the string starts with the specified value
print("37.",b)

a="     Is     "
b=a.strip()             #Remove spaces at the beginning and at the end of the string:
print("38. She",b,"Is Beautiful")

a="She Is Beautiful"
b=a.swapcase()          #Make the lower case letters upper case and the upper case letters lower case:
print("39.",b)

a="Welcome To Pycham"
b=a.title()             #Make the first letter in each word upper case:
print("40.",b)

a= {85:68}
b= "Hello World.!"       #Replace any "S" characters with a "P" character:
print ("41.",b.translate(a))

a="50"
b=a.zfill(5)            #Fill the string with zeros until it is 10 characters long:
print("42.",b)

a="Swetha"
b=a.upper()             #Upper case the string:
print("43.",b)




















