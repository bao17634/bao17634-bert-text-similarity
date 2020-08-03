import requests
import pandas as pd
import os


def download_sick(f, file_name):
    file_path = os.path.dirname(__file__) + "/" + file_name
    response = requests.get(f).text
    lines = response.split("\n")[1:]
    lines = [l.split("\t") for l in lines if len(l) > 0]
    lines = [l for l in lines if len(l) == 5]
    df = pd.DataFrame(lines, columns=["idx", "sent_1", "sent_2", "sim", "label"])
    df['sim'] = pd.to_numeric(df['sim'])
    print(df)
    df.to_csv(file_name)
    return df


sick_train = download_sick("https://raw.githubusercontent.com/alvations/stasis/master/SICK-data/SICK_train.txt",
                           "train1.csv")
sick_dev = download_sick("https://raw.githubusercontent.com/alvations/stasis/master/SICK-data/SICK_trial.txt",
                         "dev.csv")
sick_test = download_sick("https://raw.githubusercontent.com/alvations/stasis/master/SICK-data/SICK_test_annotated.txt",
                          "test1.csv")
# sick_all = sick_train.append(sick_test).append(sick_dev)
# print(sick_all)
