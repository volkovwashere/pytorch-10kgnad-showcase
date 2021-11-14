import os.path
import fastapi
import catboost
from catboost import Pool, CatBoostClassifier
from german_article_classifier.utils.config import read_yaml, get_root_path

CONFIG = read_yaml(root_path=get_root_path())
model_path = os.path.join(get_root_path(), CONFIG["model_path"], CONFIG["model_name"])
model = CatBoostClassifier()
model.load_model(fname=model_path)
