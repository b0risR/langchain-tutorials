"""
To convert your notebook code into a standard standalone .py script, you have to explicitly manage what Jupyter 
was doing for you in the background.
In a standard script, you cannot use await at the top level (outside of a function). If you try, Python will throw 
a SyntaxError: 'await' outside function.
------------------------------
## The Modified Code Structure
Here is how you must restructure your notebook code into a .py file. You need to group all your asynchronous steps 
into a main function (typically named async def main()) and use asyncio.run() to start the event loop:

"""

import asyncio
import sys

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
from rich.pretty import pprint as rpprint

# 1. Load environment variables at the top level
load_dotenv()

# 2. Put all your async logic inside an async function
async def main():
    # Initialize the client
    client = MultiServerMCPClient({
        "local_server": {
            "transport": "stdio",
            "command": "python",
            "args": ["resources/2.1_mcp_server.py"],
        }
    })

    # NOW you can safely use 'await' inside the async function
    tools = await client.get_tools()
    resources = await client.get_resources("local_server")
    
    prompt_data = await client.get_prompt("local_server", "prompt")
    system_prompt = prompt_data[0].content

    # Create your LangChain agent
    agent = create_agent(
        model="gpt-5-nano",
        tools=tools,
        system_prompt=str(system_prompt)
    )

    # Invoke the agent asynchronously
    config = {"configurable": {"thread_id": "1"}}
    response = await agent.ainvoke(
        {"messages": [HumanMessage(content="Tell me about the langchain-mcp-adapters library")]},
        config=config
    ) 

    # Print the output
    rpprint(response, indent_guides=True, expand_all=True)

# 3. Use asyncio.run() to bootstrap the script and start the event loop
if __name__ == "__main__":
    asyncio.run(main())

"""
## Key Differences Explained

   1. The async def main() Wrapper: Because await requires an asynchronous context, wrapping your application 
      logic inside an async def block satisfies Python's parser.

   2. The asyncio.run(main()) Entry Point: This line physically spins up a brand new event loop, executes your 
      main() coroutine to completion, closes the loop down safely, and shuts down any underlying thread executors.

   3. Lifespan Management: In Jupyter, your server connection client lives forever in the background kernel until 
      you restart it. In a script, the entire sequence executes from top to bottom, and everything automatically 
      clean up when asyncio.run() finishes.

"""