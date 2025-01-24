import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool  # For travel research
from crewai import LLM



# Initializing tools
serper_tool = SerperDevTool()

# Agents

# 1. Travel Budget Manager
budget_manager = Agent(
    role="Travel Budget Manager",
    goal="Validate the budget and provide a minimum budget if needed.",
    backstory=(
        "You specialize in budget optimization for travel. Your job is to ensure that travelers "
        "can afford their trip and suggest feasible alternatives if the budget is insufficient."
    ),
    tools=[],
    verbose=True,
    memory=True
)

# 2. Travel Researcher
researcher = Agent(
    role="Travel Researcher",
    goal="Gather detailed information about attractions, transportation, and accommodations "
         "for the specified cities and interests.",
    backstory=(
        "You are an expert in travel research. You have access to a wide range of tools to find "
        "the best options for travelers."
    ),
    tools=[serper_tool],
    verbose=True,
    memory=True
)

# 3. Travel Itinerary Planner
itinerary_planner = Agent(
    role="Travel Itinerary Planner",
    goal="Create a detailed travel itinerary that matches the user's preferences, budget, and schedule.",
    backstory=(
        "You are skilled in crafting comprehensive and engaging travel itineraries, ensuring travelers "
        "make the most of their trip."
    ),
    tools=[],
    verbose=True,
    memory=True
)

# Tasks

# Task 1: Validate Budget
validate_budget_task = Task(
    description=(
        "Check if the provided budget is sufficient for the travel plan. "
        "If the budget is not enough, calculate and suggest the minimum required budget."
    ),
    expected_output=(
        "A confirmation of budget sufficiency or a minimum budget suggestion."
    ),
    agent=budget_manager
)

# Task 2: Research Travel Options
research_task = Task(
    description=(
        "Research attractions, accommodations, and transportation options for the specified cities. "
        "Focus on user interests and find budget-friendly options."
    ),
    expected_output=(
        "A list of attractions, accommodations, and transportation details, categorized by city."
    ),
    agent=researcher
)

# Task 3: Plan Itinerary
plan_itinerary_task = Task(
    description=(
        "Using the user's budget, interests, and number of days, create a detailed itinerary. "
        "Ensure the plan fits the budget and provides a balanced experience."
    ),
    expected_output=(
        "A day-by-day travel itinerary, including activities, transportation, and accommodations."
    ),
    agent=itinerary_planner
)

# Crew
travel_crew = Crew(
    agents=[budget_manager, researcher, itinerary_planner],
    tasks=[validate_budget_task, research_task, plan_itinerary_task],
    process=Process.sequential  # Tasks will run sequentially
)

def run(inputs):
    inputs = inputs
    result = travel_crew.kickoff(inputs=inputs)
    return result

# Run the crew
result = travel_crew.kickoff(inputs=inputs)

print(result)
