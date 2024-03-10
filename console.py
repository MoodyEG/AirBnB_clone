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

    def do_show(self, line):
        """ Prints the string representation of an instance
        based on the class name and id """
        if not line:
            print("** class name missing **")
            return
        args = line.split(" ")
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            data = storage.all()
            for key, value in data.items():
                ins_name = value.__class__.__name__
                ins_id = value.id
                if (ins_name == args[0]) and (ins_id == args[1]):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id """
        if not line:
            print("** class name missing **")
            return
        args = line.split(" ")
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            data = storage.all()
            for key, value in data.items():
                ins_name = value.__class__.__name__
                ins_id = value.id
                if (ins_name == args[0]) and (ins_id == args[1]):
                    del value
                    """ del storage.__objects[key] """
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, line):
        """ Prints all string representation of all instances
        based or not on the class name """
        ins_list = []
        data = storage.all()
        if len(line) == 0:
            for key, value in data.items():
                ins_list.append(value.__str__())
            print(ins_list)
            return
        args = line.split(" ")
        if args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, value in data.items():
                ins_name = value.__class__.__name__
                if ins_name == args[0]:
                    ins_list.append(value.__str__())
            print(ins_list)

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
