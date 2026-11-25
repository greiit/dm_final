"""Member C: splitting, imbalance handling, model zoo, evaluation helpers."""
from sklearn.model_selection import GroupShuffleSplit
from . import config


def split_by_patient(df, test_size=0.2):
    """Group split so one patient never appears in both train and test (avoids leakage)."""
    gss = GroupShuffleSplit(n_splits=1, test_size=test_size, random_state=config.RANDOM_STATE)
    train_idx, test_idx = next(gss.split(df, groups=df[config.GROUP_COL]))
    return df.iloc[train_idx], df.iloc[test_idx]

# TODO (C): baseline, class imbalance (class_weight / SMOTE inside CV), metrics
# (precision, recall, F1, ROC-AUC, PR-AUC, confusion matrix), final comparison table.
