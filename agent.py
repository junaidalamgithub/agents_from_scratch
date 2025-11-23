import re
from dotenv import load_dotenv
from google import genai
from prompts import INSTRUCTION_PROMPT
from tools import get_weather, calculate_sum
load_dotenv()

tools_available = {"get_weather":get_weather, "calculate_sum":calculate_sum}

class Agent:
    def __init__(self):
        self.llm = genai.Client()
        self.system_prompt = INSTRUCTION_PROMPT
        self.messsages_store = []
        self.messsages_store.append({"role": "model", "parts": [{ "text": self.system_prompt }]})
        print("Agent initialized")

    def send_message(self, user_message):
        self.messsages_store.append({"role": "user", "parts": [{ "text": user_message }]})
        response = self.llm.models.generate_content(
            model="gemini-2.0-flash",
            contents=self.messsages_store)
        self.messsages_store.append({"role": "model", "parts": [{ "text": response.text}]})
        return response.text


def extract_tool(message):
    action_regex = re.compile(r"Action: (.+)$")
    input_regex = re.compile(r"Action Input: (.+)$")

    lines = message.split('\n')
    action = None
    action_input = None

    for line in lines:
        action_match = action_regex.match(line)
        input_match = input_regex.match(line)

        if action_match:
            action = action_match.group(1)
        elif input_match:
            action_input = input_match.group(1)

    return action, action_input


def extract_answer(message):
    answer_regex = re.compile(r"Answer: (.+)$")
    lines = message.split('\n')
    answer = None

    for line in lines:
        answer_match = answer_regex.match(line)
        if answer_match:
            answer = answer_match.group(1)
    return answer


def agent_query(user_input, max_turns=10):
    agent = Agent()
    i = 0
    
    while i < max_turns:
        i += 1
        
        response = agent.send_message(user_input)
        print(response)
        print()
        
        action, action_input = extract_tool(response)
        
        if action:
            result = tools_available[action](action_input)
            user_input = str(result)
        
        else:
            return extract_answer(response)
            
    return
