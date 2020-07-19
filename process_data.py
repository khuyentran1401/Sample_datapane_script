import pandas as pd 

class ClapsToNumerical(BaseEstimator, TransformerMixin):
    '''Transform claps to numerical data'''

    def __init__(self):

        pass

    def fit(self, X, y=None):

        return self

    def str_to_float(self, feature):
        '''Change string with K or M to a float (.i.e, 5k)'''

        feature = feature.replace(r'[KM]+$', '', regex=True).astype(float) * \
            feature.str.extract(r'[\d\.]+([KM]+)', expand=False).fillna(
                1).replace(['K', 'M'], [10**3, 10**6]).astype(int)

        return feature

    def transform(self, X):

        X = X.copy()
        X.Claps = self.str_to_float(X.Claps)

        cut_bins = [-1, 10, 100, 1000, 10000, 26000]
        X['Claps'] = pd.cut(X['Claps'], bins=cut_bins)

        X.Claps = X.Claps.cat.rename_categories([0, 1, 2, 3, 4])

        return X.Claps
