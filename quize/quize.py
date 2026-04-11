import random 
print("simple quize")
print("You want play quize ?")
print("yes/no")
choice = input()
if choice.lower().strip() != "yes":
    print("ok bye")
    quit()

print("ok lets play")
score = 0

questions = [
    ("CPU stands for ? ", "central processing unit"),
    ("GPU stands for ? ", "graphics processing unit"),
    ("RAM stands for ? ", "random access memory"),
    ("PS stands for ? ", "playstation"),
    ("SSD stands for ? ", "solid state drive"),
    ("ROM stands for ? ", "read only memory"),
    ("HTML stands for ? ", "hypertext markup language"),
    ("HTTP stands for ? ", "hypertext transfer protocol"),
    ("URL stands for ? ", "uniform resource locator"),
    ("IP stands for ? ", "internet protocol"),
    ("OS stands for ? ", "operating system"),
    ("LAN stands for ? ", "local area network"),
    ("WAN stands for ? ", "wide area network"),
    ("WLAN stands for ? ", "wireless local area network"),
    ("USB stands for ? ", "universal serial bus"),
    ("BIOS stands for ? ", "basic input output system"),
    ("HDD stands for ? ", "hard disk drive"),
    ("VGA stands for ? ", "video graphics array"),
    ("WIFI stands for ? ", "wireless fidelity"),
    ("PDF stands for ? ", "portable document format"),
    ("XML stands for ? ", "extensible markup language"),
    ("SQL stands for ? ", "structured query language"),
    ("VPN stands for ? ", "virtual private network"),
    ("MAC stands for ? ", "media access control"),
    ("GUI stands for ? ", "graphical user interface"),
    ("API stands for ? ", "application programming interface"),
    ("DNS stands for ? ", "domain name system"),
    ("FTP stands for ? ", "file transfer protocol"),
    ("IOT stands for ? ", "internet of things"),
    ("AI stands for ? ", "artificial intelligence"),
    ("ML stands for ? ", "machine learning"),
    ("SEO stands for ? ", "search engine optimization"),
    ("JSON stands for ? ", "javascript object notation"),
    ("PHP stands for ? ", "hypertext preprocessor"),
    ("UI stands for ? ", "user interface"),
    ("UX stands for ? ", "user experience"),
]
quize = random.sample(questions, 5)
for q, a in quize:
    answer = input(q)
    if answer.lower().strip() == a:
        print("correct")
        score += 1
    else:
        print("wrong")


print(f"you got {score} out of 5 points")

