import pandas as pd
import plotly.express as px  
import numpy as np
import dash 
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
server = app.server

data_ipl_2020 = pd.read_csv('./data/data_ipl_2020.csv')
data_ipl_2019 = pd.read_csv('./data/data_ipl_2019.csv')
data_ipl_2018 = pd.read_csv('./data/data_ipl_2018.csv')


app.layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                html.H1("IPL Players Statistics and Performance Dashboard "),
                html.H5("Riteek Sharma"),
            ], width={'size': 12, 'offset':3}),]),
        html.Hr(),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H3("Indian Premier League"),
                    html.H5("Key Parameters"),
                    html.P("Select the year"), 
                    dcc.Slider(
                    id='year',
                    min=2018,
                    max=2020,
                        marks={
                            2018: '2018',
                            2019: '2019',
                            2020: '2020',
                            },included=False),
                ]),
                html.Hr(),
                html.Div([
                    html.P("Select Batter type"),
                    dcc.Dropdown(id="display_ops",
                        options=[
                                 {'label': 'Openers', 'value': 'display_op'},
                                 {'label': 'Middleorder', 'value': 'display_mo'},
                                 {'label': 'Lowermiddleorder', 'value': 'display_lmo'},
                                 {'label': 'Wicketkeepers', 'value': 'display_wks'},
                        ],
                        value='display_op',
                        persistence=True,
                        persistence_type='memory'
                        ),
                ]),
                html.Hr(),
            ], width=3),

            dbc.Col([
                # html.Div(id='display')
                dbc.Spinner(
                    dcc.Graph(id='display', style={'height': '80vh'}),
                    color="primary"
                ),
                dbc.Spinner(
                    dcc.Graph(id='display_scat', style={'height': '80vh'}),
                    color="primary"
                ) 
            ], width=True)
        ]),


        html.Hr(),
        html.P([
            html.A("Source code", href="https://github.com/imriteek/IPL_Stats_dash"),
            ". Build beautiful UIs for your scientific computing apps with ",
            html.A("Plot.ly ", href="https://plotly.com/"),
            "and ",
            html.A("Dash", href="https://plotly.com/dash/"),
            "!",
        ]),
    ],
    fluid=True
)

@app.callback(
    [Output('display', 'figure'),
    Output('display_scat', 'figure')],
    [
        Input('year', 'value'),
        Input('display_ops', 'value'),
    ],
    prevent_initial_call=False
)

def display_plot(year_val, display_val):
    
    print(year_val, display_val)
    if year_val == None :
        fig = px.scatter()
        fig.add_annotation(x=2.5, y=1.5,font_size=40,font_color='Blue',
            text="Select Batter Type And Season",
            showarrow=False,
            yshift=13)
        fig2 = px.scatter()
        fig2.add_annotation(x=2.5, y=1.5,font_size=40,
            text="Select Batter Type And Season",
            showarrow=False,
            yshift=13)
        return fig,fig2


    if year_val == 2018:
        if display_val == 'display_op':
            fig = px.scatter_3d(data_ipl_2018.iloc[:13], x='Runs', y='SR', z='BF', color ='Runs', text = 'Player', title="Runs, Ball faced and Strike rate represented on 3D plane")
            fig2= px.scatter(data_ipl_2018.iloc[:13], x="BRPI", y="MRA", text="Player",size='Runs', hover_data=['SR','Inns'],labels={"BRPI": "Boundary Runs per Innings(BRPI)","MRA": "Milestone Reaching Ability(MRA)"},title="BoundaBall faced per Innings(BRPI) Vs Milestone Reaching Ability(MRA)")
            fig2.add_vline(x=data_ipl_2018.iloc[:13].BRPI.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.add_hline(y=data_ipl_2018.iloc[:13].MRA.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.update_traces(textposition='top center')
        elif display_val == 'display_mo':
            fig = px.scatter_3d(data_ipl_2018.iloc[13:34], x='Runs', y='SR', z='BF', color ='Runs', text = 'Player', title="Runs, Ball faced and Strike rate represented on 3D plane")
            fig2= px.scatter(data_ipl_2018.iloc[13:34], x="BRPI", y="MRA", text="Player",size='Runs', hover_data=['SR','Inns'],labels={"BRPI": "Boundary Runs per Innings(BRPI)","MRA": "Milestone Reaching Ability(MRA)"},title="BoundaBall faced per Innings(BRPI) Vs Milestone Reaching Ability(MRA)")
            fig2.add_vline(x=data_ipl_2018.iloc[13:34].BRPI.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.add_hline(y=data_ipl_2018.iloc[13:34].MRA.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.update_traces(textposition='top center')                
        elif display_val == 'display_lmo':
            fig = px.scatter_3d(data_ipl_2018.iloc[34:41], x='Runs', y='SR', z='BF', color ='Runs', text = 'Player', title="Runs, Ball faced and Strike rate represented on 3D plane")
            fig2= px.scatter(data_ipl_2018.iloc[34:41], x="BRPI", y="MRA", text="Player",size='Runs', hover_data=['SR','Inns'],labels={"BRPI": "Boundary Runs per Innings(BRPI)","MRA": "Milestone Reaching Ability(MRA)"},title="BoundaBall faced per Innings(BRPI) Vs Milestone Reaching Ability(MRA)")
            fig2.add_vline(x=data_ipl_2018.iloc[34:41].BRPI.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.add_hline(y=data_ipl_2018.iloc[34:41].MRA.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.update_traces(textposition='top center')
        elif display_val == 'display_wks':
            fig = px.scatter_3d(data_ipl_2018.iloc[41:], x='Runs', y='SR', z='BF', color ='Runs', text = 'Player', title="Runs, Ball faced and Strike rate represented on 3D plane")
            fig2= px.scatter(data_ipl_2018.iloc[41:], x="BRPI", y="MRA", text="Player",size='Runs', hover_data=['SR','Inns'],labels={"BRPI": "Boundary Runs per Innings(BRPI)","MRA": "Milestone Reaching Ability(MRA)"},title="BoundaBall faced per Innings(BRPI) Vs Milestone Reaching Ability(MRA)")
            fig2.add_vline(x=data_ipl_2018.iloc[41:].BRPI.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.add_hline(y=data_ipl_2018.iloc[41:].MRA.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.update_traces(textposition='top center')


    elif year_val == 2019:
        if display_val == 'display_op':
            fig = px.scatter_3d(data_ipl_2019.iloc[:13], x='Runs', y='SR', z='BF', color ='Runs', text = 'Player', title="Runs, Ball faced and Strike rate represented on 3D plane")
            fig2= px.scatter(data_ipl_2019.iloc[:13], x="BRPI", y="MRA", text="Player",size='Runs', hover_data=['SR','Inns'],labels={"BRPI": "Boundary Runs per Innings(BRPI)","MRA": "Milestone Reaching Ability(MRA)"},title="BoundaBall faced per Innings(BRPI) Vs Milestone Reaching Ability(MRA)")
            fig2.add_vline(x=data_ipl_2019.iloc[:13].BRPI.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.add_hline(y=data_ipl_2019.iloc[:13].MRA.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.update_traces(textposition='top center')
        elif display_val == 'display_mo':
            fig = px.scatter_3d(data_ipl_2019.iloc[13:33], x='Runs', y='SR', z='BF', color ='Runs', text = 'Player', title="Runs, Ball faced and Strike rate represented on 3D plane")
            fig2= px.scatter(data_ipl_2019.iloc[13:33], x="BRPI", y="MRA", text="Player",size='Runs', hover_data=['SR','Inns'],labels={"BRPI": "Boundary Runs per Innings(BRPI)","MRA": "Milestone Reaching Ability(MRA)"},title="BoundaBall faced per Innings(BRPI) Vs Milestone Reaching Ability(MRA)")
            fig2.add_vline(x=data_ipl_2019.iloc[13:33].BRPI.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.add_hline(y=data_ipl_2019.iloc[13:33].MRA.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.update_traces(textposition='top center')
        elif display_val == 'display_lmo':
            fig = px.scatter_3d(data_ipl_2019.iloc[33:42], x='Runs', y='SR', z='BF', color ='Runs', text = 'Player', title="Runs, Ball faced and Strike rate represented on 3D plane")
            fig2= px.scatter(data_ipl_2019.iloc[33:42], x="BRPI", y="MRA", text="Player",size='Runs', hover_data=['SR','Inns'],labels={"BRPI": "Boundary Runs per Innings(BRPI)","MRA": "Milestone Reaching Ability(MRA)"},title="BoundaBall faced per Innings(BRPI) Vs Milestone Reaching Ability(MRA)")
            fig2.add_vline(x=data_ipl_2019.iloc[33:42].BRPI.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.add_hline(y=data_ipl_2019.iloc[33:42].MRA.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.update_traces(textposition='top center')
        elif display_val == 'display_wks':
            fig = px.scatter_3d(data_ipl_2019.iloc[42:], x='Runs', y='SR', z='BF', color ='Runs', text = 'Player', title="Runs, Ball faced and Strike rate represented on 3D plane")
            fig2= px.scatter(data_ipl_2019.iloc[42:], x="BRPI", y="MRA", text="Player",size='Runs', hover_data=['SR','Inns'],labels={"BRPI": "Boundary Runs per Innings(BRPI)","MRA": "Milestone Reaching Ability(MRA)"},title="BoundaBall faced per Innings(BRPI) Vs Milestone Reaching Ability(MRA)")
            fig2.add_vline(x=data_ipl_2019.iloc[42:].BRPI.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.add_hline(y=data_ipl_2019.iloc[42:].MRA.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.update_traces(textposition='top center')


    elif year_val == 2020:
        if display_val == 'display_op':
            fig = px.scatter_3d(data_ipl_2020.iloc[:13], x='Runs', y='SR', z='BF', color ='Runs', text = 'Player', title="Runs, Ball faced and Strike rate represented on 3D plane")
            fig2= px.scatter(data_ipl_2020.iloc[:13], x="BRPI", y="MRA", text="Player",size='Runs', hover_data=['SR','Inns'],labels={"BRPI": "Boundary Runs per Innings(BRPI)","MRA": "Milestone Reaching Ability(MRA)"},title="BoundaBall faced per Innings(BRPI) Vs Milestone Reaching Ability(MRA)")
            fig2.add_vline(x=data_ipl_2020.iloc[:13].BRPI.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.add_hline(y=data_ipl_2020.iloc[:13].MRA.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.update_traces(textposition='top center')
        elif display_val == 'display_mo':
            fig = px.scatter_3d(data_ipl_2020.iloc[13:33], x='Runs', y='SR', z='BF', color ='Runs', text = 'Player', title="Runs, Ball faced and Strike rate represented on 3D plane")
            fig2= px.scatter(data_ipl_2020.iloc[13:33], x="BRPI", y="MRA", text="Player",size='Runs', hover_data=['SR','Inns'],labels={"BRPI": "Boundary Runs per Innings(BRPI)","MRA": "Milestone Reaching Ability(MRA)"},title="BoundaBall faced per Innings(BRPI) Vs Milestone Reaching Ability(MRA)")
            fig2.add_vline(x=data_ipl_2020.iloc[13:33].BRPI.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.add_hline(y=data_ipl_2020.iloc[13:33].MRA.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.update_traces(textposition='top center')
        elif display_val == 'display_lmo':
            fig = px.scatter_3d(data_ipl_2020.iloc[33:42], x='Runs', y='SR', z='BF', color ='Runs', text = 'Player', title="Runs, Ball faced and Strike rate represented on 3D plane")
            fig2= px.scatter(data_ipl_2020.iloc[33:42], x="BRPI", y="MRA", text="Player",size='Runs', hover_data=['SR','Inns'],labels={"BRPI": "Boundary Runs per Innings(BRPI)","MRA": "Milestone Reaching Ability(MRA)"},title="BoundaBall faced per Innings(BRPI) Vs Milestone Reaching Ability(MRA)")
            fig2.add_vline(x=data_ipl_2020.iloc[33:42].BRPI.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.add_hline(y=data_ipl_2020.iloc[33:42].MRA.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.update_traces(textposition='top center')
        elif display_val == 'display_wks':
            fig = px.scatter_3d(data_ipl_2020.iloc[42:], x='Runs', y='SR', z='BF', color ='Runs', text = 'Player', title="Runs, Ball faced and Strike rate represented on 3D plane")
            fig2= px.scatter(data_ipl_2020.iloc[42:], x="BRPI", y="MRA", text="Player",size='Runs', hover_data=['SR','Inns'],labels={"BRPI": "Boundary Runs per Innings(BRPI)","MRA": "Milestone Reaching Ability(MRA)"},title="BoundaBall faced per Innings(BRPI) Vs Milestone Reaching Ability(MRA)")
            fig2.add_vline(x=data_ipl_2020.iloc[42:].BRPI.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.add_hline(y=data_ipl_2020.iloc[42:].MRA.mean(), line_width=3, line_dash="dash", line_color="green")
            fig2.update_traces(textposition='top center')

    fig.update_layout(scene=dict(
                                    xaxis=dict(backgroundcolor="rgb(200, 200, 230)",gridcolor="white", 
                                            showbackground=True,zerolinecolor="white",),
                                    yaxis=dict(backgroundcolor="rgb(230, 200,230)",gridcolor="white", 
                                            showbackground=True,zerolinecolor="white",),
                                    zaxis=dict(backgroundcolor="rgb(230, 230,200)",gridcolor="white", 
                                            showbackground=True,zerolinecolor="white",),
                                    bgcolor='white'),
                            plot_bgcolor='rgb(13,163,135)',
                        )

    fig.update_layout(plot_bgcolor='powderblue',paper_bgcolor='teal')
    fig2.update_layout(plot_bgcolor='powderblue',paper_bgcolor='teal')

    print(display_val)

    return fig,fig2



if __name__ == '__main__':
    app.run_server(debug=True,use_reloader=False)