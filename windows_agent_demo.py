from windows_use.providers.anthropic import ChatAnthropic
from windows_use import Agent, Browser

llm = ChatAnthropic(model="claude-sonnet-4-5")
agent = Agent(llm=llm, browser=Browser.EDGE)
agent.invoke(task="Open Notepad and write a short poem about Windows")
