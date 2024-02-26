import argparse as ap
import sys

parser = ap.ArgumentParser()
parser.add_argument("-a", "--add-item", help = "add a new command to the list", action="store_true")
parser.add_argument("-c", "--clear", help = "add a new command to the list", action="store_true")
args = parser.parse_args()

def main():
    try:
        if args.add_item:
            new_command = input("What do you want to add?:")
            commands = open("/usr/lib/funlist.txt", "a")
            commands.write("- " + new_command + "\n")
            commands.close()
        elif args.clear:
            try:
                commands = open("/usr/lib/funlist.txt", "w")
                commands.write("")
                commands.close()
            except:
                print("an error occured, try running this command as sudo")
        else:
            commands = open("/usr/lib/funlist.txt", "r")
            print("Fun Commands List\n\n" + commands.read())
            commands.close()
    except:
        temp_list = open("/usr/lib/funlist.txt", "w")
        temp_list.close()
if __name__ == "__main__":
    main()
