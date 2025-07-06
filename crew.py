from crewai import Agent, Task, Crew
from model import load_mistral

llm = load_mistral()

# Agent 1: Research Topic Finder
topic_agent = Agent(
    role="Research Expert",
    goal="Explore the provided topic and brainstorm key questions",
    backstory="You're an expert in identifying the core areas of AI research based on trends.",
    verbose=True,
    llm=llm,
)

# Agent 2: Summarizer
summarizer_agent = Agent(
    role="Research Summarizer",
    goal="Summarize the provided research text in easy language",
    backstory="You're skilled in summarizing dense academic papers.",
    verbose=True,
    llm=llm,
)

# Agent 3: Blog Writer
blog_agent = Agent(
    role="AI Blogger",
    goal="Write an engaging blog post from the research summary",
    backstory="You write blogs that translate research into public-friendly content.",
    verbose=True,
    llm=llm,
)

# Agent 4: Social Media Specialist
caption_agent = Agent(
    role="Content Marketer",
    goal="Create a short social media caption to share the blog",
    backstory="You're an expert in writing catchy one-liners and hashtags.",
    verbose=True,
    llm=llm,
)

def run_crew(topic, text):
    # Task 1: Summarize research
    task1 = Task(
        description=f"Summarize the following paper content:\n{text}",
        expected_output="A 5-7 sentence research summary",
        agent=summarizer_agent,
    )

    # Task 2: Blog post from summary
    task2 = Task(
        description="Write a 3-paragraph blog post using the research summary",
        expected_output="Engaging, non-technical blog post",
        agent=blog_agent,
        context=[task1]
    )

    # Task 3: Social media post
    task3 = Task(
        description="Create a short tweet-style caption to promote the blog",
        expected_output="One-liner with hashtags",
        agent=caption_agent,
        context=[task2]
    )

    crew = Crew(
        agents=[summarizer_agent, blog_agent, caption_agent],
        tasks=[task1, task2, task3],
        verbose=True,
    )

    result = crew.kickoff()
    return {
        'summary': task1.output,
        'blog': task2.output,
        'caption': task3.output
    }
