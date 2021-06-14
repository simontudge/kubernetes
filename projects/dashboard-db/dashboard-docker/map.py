import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import psycopg2


# Read from the database

def get_data():
    conn = psycopg2.connect(
        host="postgres-db",
        database="mapper",
        user="mapper",
        password="password1234",
        port=5432)

    return pd.read_sql_query('select * from mapper.murders', con=conn)

try:
    df = get_data()
except:
    # If anything goes wrong, we just make an empty dataframe and continue
    df = pd.DataFrame(columns = ['name','size','lat','long','color'],
                         data = [['mega-city', 1, 1, 1, 1]])

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