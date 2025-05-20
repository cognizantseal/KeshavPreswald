import pandas as pd
import plotly.express as px
import preswald

#connect()
#df = get_df('veg')

df = pd.read_csv('data/Vegetable-Prices-2022.csv')
grouped_df = df[['Form', 'RetailPrice']].groupby('Form').agg('mean')

sql = "SELECT Vegetable, RetailPrice FROM veg WHERE Form = 'Fresh' ORDER BY RetailPrice DESC LIMIT 5"
sql_grouped_df = preswald.query(sql, "veg")
fig = px.bar(sql_grouped_df, x='Vegetable', y='RetailPrice')
fig.update_layout(
    xaxis_title="Vegetable",
    yaxis_title="Retail Price",
    title="Top 5 Fresh Vegetables by Retail Price",
    yaxis=dict(autorange=True)
)

box_fig = px.box(df, y="RetailPrice", x="Form")
box_fig.update_layout(
    xaxis_title="Form",
    yaxis_title="Retail Price",
    title="Box Plot of Retail Price by Form"
)

# Displays

preswald.text("# Exploring Vegetable Retail Trends")
preswald.text("## An analysis of pricing patterns from a US government dataset")

preswald.table(sql_grouped_df)
preswald.plotly(fig)
preswald.text('As we can see, asparagus is the most expensive vegetable by retail price')

preswald.plotly(box_fig)
preswald.text('The box plot shows that fresh and frozen vegetables have the highest median price, and canned vegetables the lowest.')