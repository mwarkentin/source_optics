from django.db.models import Sum, Count

from ...models import Repository, Commit, Statistic, Tag, Author

from plotly import tools
from .. import util

from .. import graph

import plotly.graph_objs as go
import plotly.offline as opy
import math

class AuthorGraph:
    def __init__(self, **kwargs):
        self.interval = kwargs.get('interval') if kwargs.get('interval') else 'DY'
        self.repo = kwargs['repo']
        self.start = kwargs['start']
        self.end = kwargs['end']
        self.attribute = kwargs['attribute']


    def top_graphs(self):    
        
        # Get the top contributors to be graphed
        authors = util.get_top_authors(repo=self.repo, start=self.start, end=self.end, attribute=self.attribute)

        figure = []
        # Generate a graph for each author based on selected attribute for the displayed repo
        if len(authors) != 0:
            figure = tools.make_subplots(
                rows=math.ceil(len(authors)/2),
                cols=2,
                shared_xaxes=True,
                vertical_spacing=0.1,
                shared_yaxes=True,
                subplot_titles=tuple([_.email for _ in authors]),
            )
            figure['layout'].update(height=800)
        for i in range(len(authors)):
            figure = graph.generate_graph_data(
                figure=figure,
                repo=self.repo,
                interval=self.interval,
                name=authors[i].email,
                start=self.start,
                end=self.end,
                author=authors[i],
                attribute=self.attribute,
                row=math.floor(i/2) + 1,
                col=( i % 2 )+1

            )
        
        if figure != []:
            graph_obj = opy.plot(figure, auto_open=False, output_type='div')

            return graph_obj

        return None

class AuthorContributeGraph:
    def __init__(self, **kwargs):
        self.interval = kwargs.get('interval') if kwargs.get('interval') else 'DY'
        self.author = kwargs['author']
        self.start = kwargs['start']
        self.end = kwargs['end']
        self.attribute = kwargs['attribute']

    # show author contributions per repo
    def top_graphs(self):

        repos = self.author.repos.all()
        figure = []
        # Generate a graph for each author based on selected attribute for the displayed repo
        if repos.count() != 0:
            figure = tools.make_subplots(
                rows=math.ceil(len(repos)/2),
                cols=2,
                shared_xaxes=True,
                vertical_spacing=0.1,
                shared_yaxes=True,
                subplot_titles=tuple([_.name for _ in repos]),
            )
            figure['layout'].update(height=800)

        # list 4 repos
        for i in range(min(len(repos), 6)):
            figure = graph.generate_graph_data(
                figure=figure,
                repo=repos[i],
                interval=self.interval,
                name=repos[i].name,
                start=self.start,
                end=self.end,
                author=self.author,
                attribute=self.attribute,
                row=math.floor(i/2) + 1,
                col=( i % 2 )+1

            )

        if figure != []:
            graph_obj = opy.plot(figure, auto_open=False, output_type='div')

            return graph_obj

        return None