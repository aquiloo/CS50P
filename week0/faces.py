# receive the user input
def main():
    str = input("say something: ")
    print(convert(str))
# convert the emoticons to emojis
def convert(str):
    return str.replace(":)", "🙂").replace(":(","🙁")

main()