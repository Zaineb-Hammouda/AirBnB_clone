#!/usr/bin/python3
"""
the hbnb console version 0.1
entry point of the command line interpreter
"""

import cmd
import models
from models import storage
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
        pass

    def do_create(self, line):
        """Create command: creates a new instance of BaseModel
        saves it and prints its id
        Ex: $ create BaseModel
        """

        if (self.errors(line, "create") == 1):
            return False
        instance = eval(line)
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """Show command: prints a string rep of an instance
        based on the class name and id
        Ex: $ show BaseModel 1234-1234-1234
        """

        if (self.errors(line, "show") == 1):
            return False
        args = line.split()
        instances_dict = storage.all()
        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        print(instances_dict[args[0] + '.' + args[1]])

    def do_destroy():
        """Delete command: deletes an instance based on the class name and id
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        if (self.errors(line, "destroy") == 1):
            return False

    def do_update():
        """Updates an instance based on the class name and id
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        if (self.errors(line, "update") == 1):
            return False

    def do_all():
        """all command: prints all string representation of all
        instances based or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        if (self.errors(line, "all") == 1):
            return False

    def errors(self, line, cmd):
        """manages error messages for user input"""

        cls_list = ["BaseModel", "FileStorage"]

        args = line.split()
        if line == "":
            print("** class name missing **")
            return 1
        if args[0] not in cls_list and cmd == "create":
            print("** class doesn't exist **")
            return 1
        elif cmd == "create":
            return 0

        if len(args) < 2 and cmd in ["show", "destroy"]:
            print("** instance id missing **")
            return 1

        instances_dict = storage.all()
        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        k = args[0] + '.' + args[1]

        if k not in instances_dict and cmd in ["show", "destroy"]:
            print("** no instance found **")
            return 1
        elif cmd in ["show", "destroy"]:
            return 0

        if len(args) < 3 and cmd == "update":
            print("** attribute name missing **")
            return 1
        if len(args) < 4 and cmd == "update":
            print("** value missing **")
            return 1
        return 0

if __name__ == '__main__':
        HBNBCommand().cmdloop()
