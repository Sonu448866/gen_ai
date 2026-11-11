React: Reasoning + Action
LLM keeps on reasoning based on the user query and keep on taking action in a loop until the final goal is achieved.
Tools are external ai agents and LLM has access to that .LLm decides which tool to delegate the tasks.
Internally answer of each call are sent to the LLM and based on the response it takes another set of actions.
What input and other thing goes into the ai agents is formateed by LLM itself as it has full knowledge of each
agents that are there.LLM itself soesn't execute anything by itself.
Tools can be google search,external api ,calculator etc.
LLM has to give :
1.Tools List with the code and argument ,its description
2.System Prompt(which tool is best etc. ,reuse the response etc.)

LLM + Tools(tools are just functions)
