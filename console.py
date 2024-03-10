#!/usr/bin/python3
""" Our main console """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ CMD....nothing more to say """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_create(self, line):
        """ Creates a new instance of BaseModel and prints the id"""
        if not line:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            new_model = self.classes[line]()
            print(new_model.id)
            new_model.save()

    def do_quit(self, line):
        """ Quit command """
        return True

    def do_EOF(self, line):
        """ End of File command """
        return True

    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")

    def emptyline(self):
        """ Nothing happen when empty line """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
