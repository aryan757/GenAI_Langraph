from langgraph.graph import Graph
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

os.getenv("OPENAI_API_KEY ")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
#os.environ["LANGCHAIN_API_KEY"] = getpass.getpass("LangSmith API Key:")
os.getenv("LANGCHAIN_API_KEY ")

load_dotenv()

#os.environ["LANGCHAIN_TRACING_V2"] = "true"
#os.environ["LANGCHAIN_API_KEY"] = getpass.getpass("LangSmith API Key:")

def function_1(input_1):
    return input_1 + " Hi "

def function_2(input_2):
    return input_2 + "there"



# Define a Langchain graph
workflow = Graph()

workflow.add_node("node_1", function_1)
workflow.add_node("node_2", function_2)

workflow.add_edge('node_1', 'node_2')

workflow.set_entry_point("node_1")
workflow.set_finish_point("node_2")

app = workflow.compile()

def main():
    app.invoke("Hello")

    input = 'Hello'
    for output in app.stream(input):
        # stream() yields dictionaries with output keyed by node name
        for key, value in output.items():
            print(f"Output from node '{key}':")
            print("---")
            print(value)
        print("\n---\n")

if __name__ == "__main__":
    main()
