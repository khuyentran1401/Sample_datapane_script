import pandas as pd
import altair as alt
import datapane as dp

import pickle

# load objects and plots
author_rank = dp.Blob.get('author_rank', owner='khuyentran1401').download_obj()
author_count = pickle.load(open('./author_count', 'rb'))
publication_count = pickle.load(open('./publication_count', 'rb'))
publication_rank = pickle.load(open('./publication_rank', 'rb'))


# size of the data
data_size = len(author_rank)

# load parameters from input
dp.Params.load_defaults('datapane.yaml')
author = dp.Params.get('author_name', 'Khuyen Tran')
publication = dp.Params.get('publication_name')


percentile_author = 100-(list(author_rank).index(author)+1)/len(author_rank) * 100
percentile_publications = 100 - (list(publication_rank).index(publication)+1)/len(publication_rank) * 100


dp.Report(
    dp.Markdown("# Medium Visualization"),
   dp.Plot(author_count),
   dp.Markdown(f'''
   Author {author} ranks {list(author_rank).index(author)+1} out of {data_size} authors who publish most frequently on topics related to data science last year, which is
    in the {str(round(percentile_author,2))}% percentile
   '''),
   dp.Plot(publication_count),
    dp.Markdown(f'''Publication {publication} ranks {list(publication_rank).index(publication)+1} out of {data_size} publications which publish most frequently on topics related to data science last year, which is
    in the {str(round(percentile_publications,2))}% percentile'''),
   ).publish(headline='Medium Visualization', name='medium_report')
