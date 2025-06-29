from src.graph import WorkFlow


"""
RunnableConfig is a class that lets you customize how LangChain processes calls and their sub-calls. Here's what you can do with it:

Key Functionality:

Recursion Limit: Control the maximum recursion depth allowed within your LangChain processes (recursion_limit). This helps prevent infinite loops.
Maximum Concurrency: Limit the number of parallel calls that can be made at once (max_concurrency), optimizing resource usage.
Callbacks: Trigger functions at various stages of LangChain execution (e.g., on_start, on_end, on_error). Use this for monitoring or custom error handling.
Tags: Add descriptive labels to a call and its sub-calls, helpful for tracking and analysis.
Tracer Name: Set the name to identify the tracer run (used for debugging and profiling).
Runtime Attributes: Dynamically modify configurable fields of your underlying Runnables during execution.

Why Use It

Error Handling: Define custom error-handling behavior.
Resource Management: Fine-tune parallel execution.
Monitoring: Track and log execution details with callbacks and tags.
Flexibility: Control the behavior of Runnables without modifying the underlying code.
"""
from langchain_core.runnables import RunnableConfig

new_limit = 30  # Set your desired limit
config = RunnableConfig(recursion_limit=new_limit)


app = WorkFlow().app
app.invoke({}, config=config) 