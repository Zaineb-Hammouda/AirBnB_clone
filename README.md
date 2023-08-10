# AirBnB_clone

The goal of this project is to deploy on our server a simple copy of the AirBnB website

## Contributors:

Duncan Moyo
Zaineb Hammouda

## Goals

this application will be built step by step and after 4 months, we will have a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## The Command Interpreter

In this section we focused on developing the backend file storage component using Python. This component allows us to create, manage, store, and manipulate user data. It serves as the foundation for future developments.

We have defined a base model with public attributes and methods that are used in other classes. The data is serialized and stored in a JSON file, and can be deserialized from JSON to recreate an instance based on its ID.

To facilitate testing and debugging, we have also created a command line interface. This interface allows us to create, view, update, and delete data points.

## How to use the command Interpreter

To use the command interpreter, simply run the console.py file from the directory where it is stored (or specify the directory where it is stored). The interpreter supports several commands, which can be viewed by entering help. For more information about a specific command, enter ``$ help {command}``.

Some of the available commands include:
 - **create**: Creates a new instance of BaseModel, saves it to the JSON file, and prints its ID. Example: ``$ create BaseModel``
 - **show**: Prints the string representation of an instance based on its class name and ID. Example: ``$ show BaseModel 1234-1234-1234``
 - **destroy**: Deletes an instance based on its class name and ID (and saves the change to the JSON file). Example: ``$ destroy BaseModel 1234-1234-1234``
 - **all**: Prints the string representation of all instances, either based on their class name or not. Example: $ ``all BaseModel`` or ``$ all``
 - **update**: Updates an instance based on its class name and ID by adding or updating an attribute (and saves the change to the JSON file). Example: ``$ update BaseModel 1234-1234-1234 email 'aibnb@mail.com'``
