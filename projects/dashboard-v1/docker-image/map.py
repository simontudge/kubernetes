import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('data/data.csv')


px.set_mapbox_access_token(open(".mapbox_token").read())

hover_data = {'lat': False,
              'long': False,
              'color': False,
              'size': ':,.1f'
}

fig = px.scatter_mapbox(df, lat="lat", lon="long",
                        color="color", size="size",
                        height = 1000,  hover_name='name',
                        hover_data=hover_data,
                        zoom=2
                        )

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=False, host='0.0.0.0')
