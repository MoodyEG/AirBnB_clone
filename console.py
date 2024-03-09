#!/usr/bin/python3
""" Our main console """
import cmd


class HBNBCommand(cmd.Cmd):
    """ CMD....nothing more to say """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Quit command """
        return True

    def do_EOF(self, line):
        """ End of File command """
        return True

    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
