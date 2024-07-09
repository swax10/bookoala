from termcolor import colored
from prompts.prompts import agent_system_prompt_template
from models.ollama_models import OllamaModel
from tools.books import books
from toolbox.toolbox import ToolBox


class Bookoala:
    def __init__(self, tools, model_service, model_name, stop=None):
        self.tools = tools
        self.model_service = model_service
        self.model_name = model_name
        self.stop = stop
        self.chat_history = []

    def prepare_tools(self):
        toolbox = ToolBox()
        toolbox.store(self.tools)
        tool_descriptions = toolbox.tools()
        return tool_descriptions

    def think(self, prompt):
        tool_descriptions = self.prepare_tools()
        agent_system_prompt = agent_system_prompt_template.format(tool_descriptions=tool_descriptions)
        full_prompt = f"Chat history:\n{self.format_chat_history()}\n\nCurrent query: {prompt}"

        if self.model_service == OllamaModel:
            model_instance = self.model_service(
                model=self.model_name,
                system_prompt=agent_system_prompt,
                temperature=0,
                stop=self.stop
            )
        else:
            model_instance = self.model_service(
                model=self.model_name,
                system_prompt=agent_system_prompt,
                temperature=0
            )

        agent_response_dict = model_instance.generate_text(full_prompt)
        return agent_response_dict

    def work(self, prompt):
        agent_response_dict = self.think(prompt)
        tool_choice = agent_response_dict.get("tool_choice")
        tool_input = agent_response_dict.get("tool_input")

        for tool in self.tools:
            if tool.__name__ == tool_choice:
                response = tool(tool_input)
                self.chat_history.append({"user": prompt, "assistant": response})
                print(colored(response, 'cyan'))
                return response
            
        print(colored(tool_input, 'cyan'))
        self.chat_history.append({"user": prompt, "tool_input":tool_input, "assistant": response})
        return

    def format_chat_history(self):
        formatted_history = ""
        for message in self.chat_history[-5:]:
            formatted_history += f"User: {message['user']}\nAssistant: {message['assistant']}\n\n"
        return formatted_history.strip()


if __name__ == "__main__":

    tools = [books]
    model_service = OllamaModel
    model_name = 'llama3:instruct'
    stop = "<|eot_id|>"

    agent = Bookoala(tools=tools, model_service=model_service, model_name=model_name, stop=stop)

    while True:
        prompt = input("Ask 🐨 anything: ")
        if prompt.lower() == "exit":
            break
    
        agent.work(prompt)
