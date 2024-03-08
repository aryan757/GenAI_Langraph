from langgraph.graph import Graph
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

os.getenv("OPENAI_API_KEY ")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
#os.environ["LANGCHAIN_API_KEY"] = getpass.getpass("LangSmith API Key:")
os.getenv("LANGCHAIN_API_KEY ")

load_dotenv()

# Set the model as ChatOpenAI
model = ChatOpenAI(temperature=0)

def function_1(input_1):
    response = model.invoke(input_1)
    return response.content

def function_2(input_2):
    return "Agent Says: " + input_2


# Define a Langchain graph
workflow = Graph()

#calling node 1 as agent
workflow.add_node("agent", function_1)
workflow.add_node("node_2", function_2)

workflow.add_edge('agent', 'node_2')

workflow.set_entry_point("agent")
workflow.set_finish_point("node_2")

app = workflow.compile()


def main():
    input = 'Hey there'
    for output in app.stream(input):
        # stream() yields dictionaries with output keyed by node name
        for key, value in output.items():
            print(f"Output from node '{key}':")
            print("---")
            print(value)
        print("\n---\n")

if __name__ == "__main__":
    main()
