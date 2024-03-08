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
model = ChatOpenAI(temperature=0.8)


## this is just a BASIC Propmt !!

def function_1(input_1):
    complete_query = " Your task is to extract the product name based on the user query.\
                     and tell me the basic details of the each product in json format \
                    Here is the User query " + input_1

    response = model.invoke(complete_query)
    return response.content

def function_2(input_2):
    return "Agent Says :" + input_2


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
    input_1 = 'Tesla Model 3: Sleek electric car with long-range and autopilot features. \
    Apple AirPods Pro: Wireless earbuds with noise cancellation and seamless integration.\
     DJI Mavic Air 2: Compact drone with 4K camera and intelligent flight modes. \
     Google Pixel 6: Flagship smartphone with advanced camera and vibrant display. \
     Amazon Echo Show 10: Smart display with rotating screen and Alexa integration.'

    for output in app.stream(input_1):
        # stream() yields dictionaries with output keyed by node name
        for key, value in output.items():
            print(f"Output from node '{key}':")
            print("---")
            print(value)
        print("\n---\n")

if __name__ == "__main__":
    main()


