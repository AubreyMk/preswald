from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

# Show text first
text("# Welcome to the AI Productivity Dashboard")
text("Visualizing developer habits and their cognitive performance.")

# Connect and load data
connect()
df = get_df("ai_csv")
# Query: Coffee intake > 50 mg
sql = "SELECT * FROM ai_csv WHERE coffee_intake_mg > 5"
filtered_df = query(sql, "ai_csv")
table(filtered_df, title="Filtered Data")

# Plot: Coding hours vs Cognitive Load by Task Success
fig = px.scatter(df, x="hours_coding", y="cognitive_load", color="task_success")

plotly(fig)
