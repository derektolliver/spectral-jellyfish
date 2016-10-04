def run():
    print("Welcome to the Lob Letter Generator! Please enter the following information to send your letter.")
    input_list = createInputList()
    gatherInput()

def createInputList():
    input_list = []
    input_list.append("Name")
    input_list.append("Address Line 1")
    input_list.append("Address Line 2")
    input_list.append("City")
    input_list.append("State")
    input_list.append("Zip Code")
    input_list.append("Message")
    return input_list

def gatherInput(input_list):
    user_info = []
    for i in range(0, len(input_list)):
        print("From %s: ") (input_list[i])
        info = input()
        checkInput(input_list[i], info)
        user_info.append(info)

def checkInput(term, info):
    if term == "Name":
        for l in term:
            if !l.isalpha():
                raise ValueError("Character in name is not a valid letter.")
    elif term == "Address Line 1":

    elif term == "Address Line 2":

    elif term == "City":

    elif term == "State":

    elif term == "Zip Code":

    elif term == "Message":



if __name__ == "__main__":
    run()
