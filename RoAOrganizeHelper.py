print("hex to text")
exec('b = open(r%s,"r").read()' % input("raw hex file "))#save inputted file to variable (b)
b = list(b) #make b a list to be able to del items later on
c="" #initialize c
a={'00': '\n', '5C': '\\', '3A': ':', '20': ' ', '21': '!', '23': '#', '24': '$', '25': '%', '26': '&', '27': "'", '28': '(', '29': ')', '2A': '*', '2B': '+', '2C': ',', '2E': '.', '2F': '/', '30': '0', '31': '1', '32': '2', '33': '3', '34': '4', '35': '5', '36': '6', '37': '7', '38': '8', '39': '9', '3B': ';', '3D': '=', '3F': '?', '40': '@', '41': 'A', '42': 'B', '43': 'C', '44': 'D', '45': 'E', '46': 'F', '47': 'G', '48': 'H', '49': 'I', '4A': 'J', '4B': 'K', '4C': 'L', '4D': 'M', '4E': 'N', '4F': 'O', '50': 'P', '51': 'Q', '52': 'R', '53': 'S', '54': 'T', '55': 'U', '56': 'V', '57': 'W', '58': 'X', '59': 'Y', '5A': 'Z', '5B': '[', '5D': ']', '5E': '^', '5F': '_', '60': '`', '61': 'a', '62': 'b', '63': 'c', '64': 'd', '65': 'e', '66': 'f', '67': 'g', '68': 'h', '69': 'i', '6A': 'j', '6B': 'k', '6C': 'l', '6D': 'm', '6E': 'n', '6F': 'o', '70': 'p', '71': 'q', '72': 'r', '73': 's', '74': 't', '75': 'u', '76': 'v', '77': 'w', '78': 'x', '79': 'y', '7A': 'z', '7B': '{', '7C': '|', '7D': '}', '7E': '~'} #a is a dictionary that's used to translate hex<->text
ErrorCounter=0
while (b!=[]):#the loop checks the first two items, compares them to the list in the dictionary and then deletes them, once every item has been checked the list is empty
    if(b[0]==" "):
        del b[0]
    try:
        c+=a[b[0]+b[1]]
    except KeyError:
        if(ErrorCounter==0):
            a.update({b[0]+b[1]: "<"})
        elif(ErrorCounter==1):
            a.update({b[0]+b[1]: "-"})
        else:
            a.update({b[0]+b[1]: ">"})
        ErrorCounter+=1
        c+=a[b[0]+b[1]]
    except IndexError:
        print(b[0])
    try:
        del b[1]
    except IndexError:
        pass
    del b[0]


open("RoAOrganizer.RoAText","w+").write(c) #create RoaText file
f = open("RoAOrganizer.RoAText","r")
for line in f: #open RoaText
    etest=""#helps finding unnamed characters by having an empty variable if no name has been found
    try :
        path = open(str(line)[0:len(line)-1]+"/config.ini","r")
    except OSError:
        path = open(str(line)[1:len(line)-1]+"/config.ini","r")
    for lin in path: #use each line of RoAText to find the config.ini and print the name by looking for a line starting with 'name'
        if(lin[0:4]=="name"):
            etest = lin[6:-2]
    if(etest==""):
        print("unnamed")
    else:
        print(etest)





input("press enter to copy text to hex ")
b = open("RoAOrganizer.RoAText","r").read() #save the RoaText to b
b = list(b) #make b a list for use of del later on (can probably skip the line right before)
c=""#initialize c (should be moved to before first input ?)
a2={'\n': '00', '\\': '5C', '<': 'A6', '>': '11', ':': '3A', ' ': '20', '!': '21', '#': '23', '$': '24', '%': '25', '&': '26', "'": '27', '(': '28', ')': '29', '*': '2A', '+': '2B', ',': '2C', '-': '2D', '.': '2E', '/': '2F', '0': '30', '1': '31', '2': '32', '3': '33', '4': '34', '5': '35', '6': '36', '7': '37', '8': '38', '9': '39', ';': '3B', '=': '3D', '?': '3F', '@': '40', 'A': '41', 'B': '42', 'C': '43', 'D': '44', 'E': '45', 'F': '46', 'G': '47', 'H': '48', 'I': '49', 'J': '4A', 'K': '4B', 'L': '4C', 'M': '4D', 'N': '4E', 'O': '4F', 'P': '50', 'Q': '51', 'R': '52', 'S': '53', 'T': '54', 'U': '55', 'V': '56', 'W': '57', 'X': '58', 'Y': '59', 'Z': '5A', '[': '5B', ']': '5D', '^': '5E', '_': '5F', '`': '60', 'a': '61', 'b': '62', 'c': '63', 'd': '64', 'e': '65', 'f': '66', 'g': '67', 'h': '68', 'i': '69', 'j': '6A', 'k': '6B', 'l': '6C', 'm': '6D', 'n': '6E', 'o': '6F', 'p': '70', 'q': '71', 'r': '72', 's': '73', 't': '74', 'u': '75', 'v': '76', 'w': '77', 'x': '78', 'y': '79', 'z': '7A', '{': '7B', '|': '7C', '}': '7D', '~': '7E'}#check line 5
for i,o in a.items():
    if(o=='<') or (o=='-') or (o=='>'):
        a2.update({o: i})         
while (b!=[]):#compare first item in the file to the dictionary to make it hex and the delete it
    c+=a2[b[0]]
    del b[0]
open("RoAOrganizer.RoAHex","w+").write(c)#save output
print("The data from \"RoAOrganizer.RoAText\" has been copied to \"RoAOrganizer.RoAHex\"")#express event
input("\npress enter to quit ")#Leave a way to end the program
