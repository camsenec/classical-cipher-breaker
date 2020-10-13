import wordninja

if __name__ == "__main__":

    with open("input/split_text_input.txt", mode="r") as f:
        message = f.read()

    word_list = wordninja.split(message)
    splitted_message = ""

    for word in word_list:
        splitted_message += word + " "

    print("SPLITTED")
    print("----------------------------------------------")
    print(splitted_message)
