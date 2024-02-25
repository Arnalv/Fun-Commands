import argparse as ap
import sys

parser = ap.ArgumentParser()
parser.add_argument("-a", "--add-item", help = "add a new command to the list", action="store_true")
args = parser.parse_args()

def main():
    try:
        if args.add_item:
            new_command = input("What do you want to add?:")
            commands = open("list.txt", "a")
            commands.write("- " + new_command + "\n")
            commands.close()
        else:
            commands = open("list.txt", "r")
            print(commands.read())
            commands.close()
    except:
        temp_list = open("list.txt", "w")
        temp_list.close()
if __name__ == "__main__":
    main()
