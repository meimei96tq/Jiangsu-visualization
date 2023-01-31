import json
from pymongo import MongoClient
import plotly.express as px

myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient["Jiangsu"]
data_col = mydb["data"]

with open('江苏省.json', encoding='utf-8') as f:
    map = json.load(f)
data = []

for row in data_col.find():
    data.append({
        "City": row["mapName"],
        "#Exist covid people": int(row["conNum"]),
        "#Cure": row["cureNum"],
        "#Death": row["deathNum"]
    })

fig = px.choropleth(data, geojson=map, color="#Exist covid people",
                    locations="City", featureidkey="properties.name",
                    projection="mercator", hover_data=["#Exist covid people", "#Cure", "#Death"],
                    color_continuous_scale=[(0, "white"),(1, "red")],
                    title=""
                    )
# print(fig)
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
