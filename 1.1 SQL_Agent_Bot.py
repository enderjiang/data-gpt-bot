# a much more advancing version using langchain agent, integrate with multiple SQL sources
#So user can choose the data source from frontend

from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
import gradio as gr
import os

db_dict={
    'db1':'uri1',
    'db2':'uri2'
}    
def run_agent(input_text, db):
    db_uri = db_dict.get(db)
    if not db_uri:
        return "Invalid database selected"
    db = SQLDatabase.from_uri(db_uri)
    toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0))
    #there is a wrong example in toolkit from langchain, make sure toolki includes llm parameter
    agent_executor = create_sql_agent(llm=OpenAI(temperature=0), toolkit=toolkit, verbose=True)
    result = agent_executor.run(input_text)
    return result

# Define the Gradio interface
interface = gr.Interface(
    fn=run_agent,
    inputs=[
        gr.inputs.Textbox(label="Enter your question in natural language:"),
        gr.inputs.Dropdown(label="Select a database:", choices=list(db_dict.keys()))
    ],
    outputs=gr.outputs.Textbox(label="Result of your query:"),
    title="Large Language Data Bot",
    description="test demo @ ender",
    theme=gr.themes.Soft()
)

# Launch the interface
interface.launch()