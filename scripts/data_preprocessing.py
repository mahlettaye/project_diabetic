
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import matplotlib.pyplot as plt

def percent_missing(df):

    # Calculate total number of cells in dataframe
    totalCells = np.prod(df.shape)

    # Count number of missing values per column
    missingCount = df.isnull().sum()

    # Calculate total number of missing values
    totalMissing = missingCount.sum()

    # Calculate percentage of missing values
    print("The Diabetes dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")


def fix_missing_ffill(df, col):
    df[col] = df[col].fillna(method='ffill')
    return df[col]


def fix_missing_bfill(df, col):
    df[col] = df[col].fillna(method='bfill')
    return df[col]




def select_features(x, y):
    # Feature extraction
    test = SelectKBest(score_func=chi2, k=4)
    fit = test.fit(x, y)

    # Summarize scores
    np.set_printoptions(precision=3)
    print(fit.scores_)

    for i in range(len(fit.scores_)):
        print('Feature %d: %f' % (i, fit.scores_[i]))
    # plot the scores
    plt.bar([i for i in range(len(fit.scores_))], fit.scores_)
    plt.show()

    features = fit.transform(x)
    #Summarize selected features
    print(features[0:5,:])
