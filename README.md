# AirBnB_clone
![hbnb](https://github.com/DuncanMoyo/AirBnB_clone/assets/122837330/7aaf05b3-a274-451d-a5ef-1eadb5df8b14)

## Project Description

This project is issued by Alx_africa and its goal is to deploy on our server a simple copy of the [Airbnb Website](https://www.airbnb.com/).

## Goals

This application will be built step by step and after 4 months, we will have a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Contributors:

- Duncan Moyo (Cohort 13)
- Zaineb Hammouda (Cohort 13)

### General Concepts

- Python Packages
- Command interpreters using the cmd module
- serializing and deserializing classes and instances using JSON
- Unit tests
- UUIDs
- managing datetime
- *args and **kwargs

### The Command Interpreter

In this section we focused on developing the backend file storage component using Python. This component allows us to create, manage, store, and manipulate user data. It serves as the foundation for future developments.

We have defined a base model with public attributes and methods that are used in other classes. The data is serialized and stored in a JSON file, and can be deserialized from JSON to recreate an instance based on its ID.

To facilitate testing and debugging, we have also created a command line interface. This interface allows us to create, view, update, and delete data points.

### How to use the command Interpreter

To use the command interpreter, simply run the console.py file from the directory where it is stored (or specify the directory where it is stored). The interpreter supports several commands, which can be viewed by entering help. For more information about a specific command, enter ``$ help {command}``.

| Command  | Description |
| ------------- | ------------- |
| ```quit```  | Exits the console  |
| ```Ctrl+D```  | Exits the console  |
| ```help``` or ```help <command>```  | Displays all commands or Displays instructions for a specific command
| ```create <class>```  | Creates an object of that class, saves it to a JSON file, and prints the objects ID
| ```show <class> <ID>```  | Shows string representation of an object
| ```destroy <class> <ID>```  | Deletes an object based on its class and id
| ```all or all <class>```  | Prints all string representations of all objects or Prints all string representations of all objects of a specific class
| ```update <class> <id> <attribute name> "<attribute value>"```  | Updates an object with a certain attribute (new or existing)
| ```<class>.all()```  | Same as all ```<class>```
| ```<class>.count()```  | Retrieves the number of objects of a certain class
| ```<class>.show(<ID>)```  | Same as show ```<class> <ID>```
| ```<class>.destroy(<ID>)```  | Same as destroy ```<class> <ID>```
| ```<class>.update(<ID>, <attribute name>, <attribute value>```  | Same as update ```<class> <ID> <attribute name> <attribute value>```
| ```<class>.update(<ID>, <dictionary representation>)```  | Updates an objects based on a dictionary rep of attribute names and values
