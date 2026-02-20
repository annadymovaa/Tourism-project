import kagglehub
from kagglehub import KaggleDatasetAdapter

#kagglehub.login()

path = kagglehub.dataset_download("leondesilva1/travel-destinations")

print("Path to dataset files:", path)
#/Users/arthopoda/.cache/kagglehub/datasets/leondesilva1/travel-destinations/versions/2