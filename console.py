#!/usr/bin/python3
"""
the cmd module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ entry point of the command interpreter of our Hbnb Console"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF command to exit the program with ctrl+D"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        return False

if __name__ == '__main__':
        HBNBCommand().cmdloop()
