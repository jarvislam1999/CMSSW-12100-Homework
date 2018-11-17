'''
Helper function for traffic stops assignment
'''

import seaborn as sns

def visualize_rate_series(rate_series, filename='barplot.png'):
    '''
    Purpose: creates a barplot and prints to file
    '''
    graph_df = (rate_series
                .to_frame()
                .reset_index())
    bar_plot = sns.barplot(
        x=graph_df.iloc[:, -2], y=graph_df.iloc[:, -1], color='blue')
    fig = bar_plot.get_figure()
    fig.savefig(filename)
