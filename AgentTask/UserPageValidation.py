import os
import asyncio

from browser_use.agent.service import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

async def pageValidation():
    os.environ["GEMINI_API_KEY"]="AIzaSyDZJ1xWz4UvLLfUG_A57qIEP2_Y1r6SZGE"
    task =(
        'Important : I am UI Automation tester validating the task'
        'open website https://opensource-demo.orangehrmlive.com'
        'Login with username and password. login Details available in the same page'
        'After login, validate Dashboard is displayed'
        'Then Navigate to each page one by one, available in Left hand menu'
        'if user encounter maintenance page click on Cancel or click on back button in browser'
    )
    api_key = os.environ["GEMINI_API_KEY"]
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp',api_key=SecretStr(api_key))
    agent = Agent(task,llm,use_vision=True)
    history = await agent.run()
    test_results = history.final_result()
    print(test_results)

asyncio.run(pageValidation())