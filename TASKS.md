# Task distribution

Fill in names. Everyone must be able to explain their part at the defense.

## Member A: data foundation
- [ ] Problem definition, objectives, 2-4 research questions, why this dataset
- [ ] Dataset description (source, size, feature types, missing values, class distribution)
- [ ] Preprocessing: duplicates, missing values, outliers, encoding, scaling, transformations (all justified)
- [ ] Models: baseline (majority class), Logistic Regression, KNN
- [ ] README, report sections "Problem" and "Data"
- Files: `src/preprocessing.py`, `notebooks/01_preprocessing.ipynb`

## Member B: EDA and features
- [ ] Summary stats, distributions, correlations, >= 5 visualizations, >= 5 conclusions
- [ ] Statistical test (ANOVA / chi-square)
- [ ] >= 2 engineered features, feature selection, PCA
- [ ] Models: Decision Tree, Random Forest + hyperparameter tuning
- [ ] Report sections "EDA" and "Feature engineering"
- Files: `src/features.py`, `notebooks/02_eda_features.ipynb`

## Member C: evaluation and integration
- [ ] Split strategy (group split by patient), CV scheme, class imbalance handling
- [ ] Models: XGBoost / LightGBM, SVM
- [ ] Final comparison, overfitting check, final model on test set (test used once)
- [ ] Results, limitations, >= 3 future improvements, answers to research questions
- [ ] Assemble and proofread report and slides, team contribution statement
- Files: `src/models.py`, `notebooks/03_modeling.ipynb`

## Shared
- [ ] Slides (10-15): each person makes their own slides
- [ ] Report (5-8 pages): each writes own section, C merges
- [ ] Final check: fresh clone runs end-to-end following README
