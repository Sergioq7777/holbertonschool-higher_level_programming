#!/usr/bin/python3
def main():
    i = 0
    for i in dir(hidden_4):
        if i[0:1] != '_':
            print("{}".format(i))
if __name__ == '__main__':
    import hidden_4
    main()
