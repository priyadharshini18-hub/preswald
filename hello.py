from preswald import connect, get_df, query, plotly, table, text
import plotly.express as px

connect()

df = get_df("seattle_weather_csv")

sql = """
SELECT * 
FROM seattle_weather_csv
WHERE weather LIKE '%rain%' AND precipitation > 5
"""
filtered_df = query(sql, "seattle_weather_csv")

text("# Seattle Weather Insights")
text("My name is Priyadharshini Ganeshkumar, MSCS student from UC Davis. Here is my is my submission for Preswald challenge.")

text("I have used `seattle-weather.csv` from Kaggle. The following are the columns present in the data:\n\n- `date`\n- `precipitation`\n- `temp_max`\n- `temp_min`\n- `wind`\n- `weather`")


fig = px.scatter(
    df,
    x="temp_max",
    y="precipitation",
    color="weather",
    title="Max Temperature vs Precipitation by Weather Type",
    labels={"temp_max": "Max Temperature (°C)", "precipitation": "Precipitation (mm)"}
)

plotly(fig)

text("")

fig2 = px.scatter(
    df,
    x="wind",
    y="precipitation",
    color="weather",
    title="Wind Speed vs Precipitation by Weather Type",
    labels={"wind": "Wind Speed (km/h)", "precipitation": "Precipitation (mm)"}
)
plotly(fig2)