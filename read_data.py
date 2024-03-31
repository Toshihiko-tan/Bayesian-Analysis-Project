import pandas as pd

# URL of the CSV file
url = (
    "https://storage.googleapis.com/kagglesdsdata/datasets/4553963/7781877/smoking.csv"
    "?X-Goog-Algorithm=GOOG4-RSA-SHA256"
    "&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240331%2Fauto%2Fstorage%2Fgoog4_request"
    "&X-Goog-Date=20240331T003424Z"
    "&X-Goog-Expires=259200"
    "&X-Goog-SignedHeaders=host"
    "&X-Goog-Signature=25c47b6313b98b8227ca1ffff67722416fbeacb96ae7e24a9a6d5c3573b2a5e3"
    "b22c2c1c70d17a031a36505d6b9ef516a3d532405fba2fdbcfcf20636bb07b2767"
    "2f89d41524a072f27f640d9cc2795e16ef58e61f79afdaf6273468e94d91f3644f"
    "e8840e81aa305163498aab0fedc7befdb7b841209823555f0cb8db0cbba70b1b8c"
    "6dd8c657b62277adb9feb2ce86414c075b3838ecf81c3e5d654636a25942367500"
    "eff814ca66e09d562c9c46b93b9c9b3318d96f22408245ee13ec8a9b2a43a2c881"
    "21d0128074b01ab1e5281da0b9bf064dde99f0d9c404a89d613e6acb4d48096471"
    "504262b70f00fbc404cadb3c4b88e744d241f9a0bfe5a6f1e9ed"
)

# Reading the CSV file into a pandas DataFrame
df = pd.read_csv(url)
