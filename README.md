# data-gpt-bot
Welcome to the Data GPT Bot program! This program allows you to easily query databases using natural language queries.

The program is built using Python and leverages the GPT-3.5 architecture to convert natural language questions into SQL queries that can be executed on the specified database. The SQLDatabaseSequentialChain class is used to chain together multiple SQL queries to produce the final result.

To use the program, simply enter your question in the input box and the program will generate the corresponding SQL query and execute it on the database. The result will be displayed in the output box.

The program currently uses an OpenAI API key for language processing and connects to an Omron database, but it can be easily adapted to work with other databases and APIs.

The front-end of this program is built using Gradio, a Python library that allows for the creation of web-based interfaces for machine learning models.

In this program, the Gradio interface is used to provide a simple and intuitive way for users to interact with the LangChain SQL Query function. The interface consists of two text boxes: one for entering natural language questions, and another for displaying the result of the SQL query.

When the user enters a question and clicks the "Submit" button, the LangChain SQL Query function is called with the user's question as input. The function then generates the corresponding SQL query, executes it on the specified database, and returns the result to the interface. The result is then displayed in the output text box.

The Gradio interface makes it easy for users to quickly and easily query databases using natural language, without having to write complex SQL queries themselves. It also provides a user-friendly way for developers to showcase and test their machine learning models.

![image](https://user-images.githubusercontent.com/65903200/236637785-a254f08d-c776-461b-8372-abab6f1a35f9.png)
