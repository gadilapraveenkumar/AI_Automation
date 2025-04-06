import os
import asyncio

from browser_use.agent.service import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr

async def testValidation():
    os.environ["GEMINI_API_KEY"]="AIzaSyDZJ1xWz4UvLLfUG_A57qIEP2_Y1r6SZGE"
    task =(
        'Important : I am UI Automation tester validating the task'
        'open website https://rahulshettyacademy.com/loginpagePractise/'
        'Login with username and password. login Details available in the same page'
        'After login, select first 2 products and add them to cart'
        'Then Checkout and store the total value ou see in screen'
        'Increase the quantity of any product and check if total value pdate accordingly'
        'checkout and select country, agree terms and purchase'
        'verify thank you message is displayed'
    )
    api_key = os.environ["GEMINI_API_KEY"]
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp',api_key=SecretStr(api_key))
    agent = Agent(task,llm,use_vision=True)
    await agent.run()
    test_results = history.final_result()
    print(test_results)

asyncio.run(testValidation())