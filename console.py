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
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, line):
        """Create command: creates a new instance of BaseModel
        saves it and prints its id
        Ex: $ create BaseModel
        """

        if (self.errors(line, "create") == 1):
            return False
        """ evaluate the contents of line string to class and execute it
        with ()"""
        instance = eval(line)()
        """save it to JSON file"""
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """Show command: prints a string rep of an instance
        based on the class name and id
        Ex: $ show BaseModel 1234-1234-1234
        """

        if (self.errors(line, "show") == 1):
            return False
        """split line to multiple args"""
        args = line.split()
        """get all instances's dicts from storage"""
        instances_dict = storage.all()
        """remove the quotations if string inputted has them"""
        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        print(instances_dict[args[0] + '.' + args[1]])

    def do_destroy(self, line):
        """Delete command: deletes an instance based on the class name and id
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        if (self.errors(line, "destroy") == 1):
            return False

        instances_dict = storage.all()
        args = line.split()
        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        del instances_dict[args[0] + '.' + args[1]]
        storage.save()

    def do_update(self, line):
        """Updates an instance based on the class name and id
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if (self.errors(line, "update") == 1):
            return False

        args = line.split()
        instances_dict = storage.all()
        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        x = args[0] + '.' + args[1]
        new_key = args[2]
        new_value = args[3]
        setattr(instances_dict[x], new_key, new_value)
        storage.save()

    def do_all(self, line):
        """all command: prints all string representation of all
        instances based or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        instances_dict = storage.all()
        """if all is used without class name"""
        d_list = []
        if line == "":
            d_list = [str(i) for i in instances_dict.values()]
            print(d_list)
            return False
        args = line.split()
        """if all is used with class name, manage errors, if any, and return"""
        if (self.errors(line, "all") == 1):
            return False
        for i in instances_dict.values():
            if i.__class__.__name__ == args[0]:
                d_list.append(str(i))
        print(d_list)

    def errors(self, line, cmd):
        """manages error messages for user input"""

        cls_list = ["BaseModel", "FileStorage"]
        cmd_list = ["create", "show", "all", "destroy", "update"]

        if line == "":
            print("** class name missing **")
            return 1
        args = line.split()
        if args[0] not in cls_list and cmd in cmd_list:
            print("** class doesn't exist **")
            return 1
        elif cmd in ["create", "all"]:
            return 0

        if len(args) < 2 and cmd in ["show", "destroy", "update"]:
            print("** instance id missing **")
            return 1

        instances_dict = storage.all()
        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        k = args[0] + '.' + args[1]

        if k not in instances_dict and cmd in ["show", "destroy", "update"]:
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
