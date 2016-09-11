def movie():
    numTests = int(input())
    for i in range(numTests):
        title = input()
        if " " not in title:
            print(title + " Returns")
        else:
            print(title + ": Age of Darkness")

if __name__ == "__main__":
    movie()
