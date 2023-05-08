from langchain import OpenAI,SQLDatabase,SQLDatabaseChain
from langchain.chains import SQLDatabaseSequentialChain
import gradio as gr

#can prepare list of db, or use input method
dblist={
    'dbname':'mysql+pymysql://user:pass@some_mysql_db_address/db_name'
}

# Define your langchain SQL query function
def run_langchain_query(question):
    llm = OpenAI(openai_api_key="YourKEY", temperature=0)
    db = SQLDatabase.from_uri(dblist.get('dbname'))
    db_chain = SQLDatabaseSequentialChain.from_llm(llm=llm, database=db, verbose=True)
    result = db_chain.run(question)
    
    return result

# Define the Gradio interface
interface = gr.Interface(
    fn=run_langchain_query,
    inputs=gr.inputs.Textbox(label="Enter your question in natural language:"),
    outputs=gr.outputs.Textbox(label="Result of your query:")
)

# Launch the interface
interface.launch()