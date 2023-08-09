#!/usr/bin/python3
"""
the hbnb console version 0.1
entry point of the command line interpreter
"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json


class HBNBCommand(cmd.Cmd):
    """console class:
        entry point of the command interpreter of our Hbnb Console
    """

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

    def do_create(self, line):
        """Create command: creates a new instance of BaseModel
        saves it and prints its id
        Ex: $ create BaseModel
        """

        if (self.errors(line) == 1):
            return False
        instance = line()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """Show command: prints a string rep of an instance
        based on the class name and id
        Ex: $ show BaseModel 1234-1234-1234
        """

        if (self.errors(line) == 1):
            return False
        args = line.split()
        instances_dict = storage.all()
        print(instances_dict[args[0].args[1]])

    def do_destroy():

    def do_update():

    def do_all():
        """ all command: prints all string representation of all instances based or not on the class name.
        Ex: $ all BaseModel or $ all
        """

    def errors(self, line):
        """manages error messages for user input"""

        cls_list = ["BaseModel", "FileStorage"]

        args = line.split()
        if line == "":
            print("** class name missing **")
            return 1
        elif args[0] not in cls_list:
            print("** class doesn't exist **")
            return 1
        elif len(args) < 2:
            print("** instance id missing **")
        elif id doesnt exist:
            print("** no instance found **")

if __name__ == '__main__':
        HBNBCommand().cmdloop()
