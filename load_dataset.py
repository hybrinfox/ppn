import json
import os
import pickle
from typing import *

import pandas as pd

def convert_json_list_to_pandas(json_list):
    compiled_doc = {}
    for json_doc in json_list:
        for key, val in json_doc.items():
            compiled_doc[key] = compiled_doc.get(key, []) + [val]
    data = pd.DataFrame()
    for key, val in compiled_doc.items():
        data[key] = val
    return data

def load_from_folder(folder: str, languages: List[str] = ["ar", 'de', "en", "es", "fr", "it", "ua", "ru", "zh"]):
    docs = []
    if folder[-1] != '/':
        folder = folder + '/'
    if type(languages) == str:
        languages = [languages]
    dataset_files = os.listdir(folder)
    for file in dataset_files:
        if file[-4:] == "json":
            with open(folder+file, 'r') as f:
                lines = f.readlines()[0]
            doc_json = json.loads(lines)
            if doc_json["language"] in languages:
                docs.append(doc_json)
    return docs

def load_from_folder_tribunal_ukraine(folder: str, languages: List[str] = ['de', "en", "es", "fr", "ru"]):
    docs = []
    if folder[-1] != '/':
        folder = folder + '/'
    if type(languages) == str:
        languages = [languages]
    language_list_tribunal_ukraine = ["lang=" + lang for lang in languages]
    if "de" in languages:
        language_list_tribunal_ukraine.append("lang=_")
    dataset_files = os.listdir(folder)
    for file in dataset_files:
        if file[-4:] == "json":
            for lang in language_list_tribunal_ukraine:
                if lang in file:
                    with open(folder+file, 'r') as f:
                        lines = f.readlines()[0]
                    doc_json = json.loads(lines)
                    docs.append(doc_json)
    return docs

def load_rrn(languages: List[str] = ["ar", 'de', "en", "es", "fr", "it", "ua", "ru", "zh"]):
    if type(languages) == str:
        languages = [languages]
    docs = load_from_folder("ppn_data/2023/09/13/rrn.media/", languages=languages)
    return convert_json_list_to_pandas(docs)

def load_tribunalukraine(languages: List[str] = ['de', "en", "es", "fr", "ru"]):
    # Language identification is broken for this dataset
    if type(languages) == str:
        languages = [languages]
    docs = load_from_folder_tribunal_ukraine("ppn_data/2023/11/09/tribunalukraine.info/", languages=languages)
    return convert_json_list_to_pandas(docs)

def load_waronfakes(languages: List[str] = ["ar", 'de', "en", "es", "fr", "zh"]):
    if type(languages) == str:
        languages = [languages]
    docs = load_from_folder("ppn_data/2023/11/09/waronfakes.com/", languages=languages)
    return convert_json_list_to_pandas(docs)

def load_lavirgule():
    # Articles are only in French but the language annotator didn't work correctly
    languages = ["ar", 'de', "en", "es", "fr", "it", "ua", "ru", "zh"]
    if type(languages) == str:
        languages = [languages]
    docs = load_from_folder("ppn_data/2023/11/09/lavirgule.news/", languages=languages)
    return convert_json_list_to_pandas(docs)

def load_notrepays():
    # Articles are only in French but the language annotator didn't work correctly
    languages = ["ar", 'de', "en", "es", "fr", "it", "ua", "ru", "zh"]
    if type(languages) == str:
        languages = [languages]
    docs = load_from_folder("ppn_data/2023/11/09/notrepays.today/", languages=languages)
    return convert_json_list_to_pandas(docs)

def load_regular_fr():
    return pickle.load(open("regular_data/regular_ukraine_FR.pkl", "rb"))

def load_regular_en():
    return pickle.load(open("regular_data/regular_ukraine_EN.pkl", "rb"))



def load_ppn(languages: List[str] = ["ar", 'de', "en", "es", "fr", "it", "ua", "ru", "zh"]):
    if type(languages) == str:
        languages = [languages]
    rrn_docs = load_from_folder("ppn_data/2023/09/13/rrn.media/", languages=languages)
    tribunalukraine_docs = load_from_folder_tribunal_ukraine("ppn_data/2023/11/09/tribunalukraine.info/", languages=languages)
    waron_fakes_doc = load_from_folder("ppn_data/2023/11/09/waronfakes.com/", languages=languages)
    docs = rrn_docs + tribunalukraine_docs + waron_fakes_doc
    if "fr" in languages:
        lavirgule_docs = load_from_folder("ppn_data/2023/11/09/lavirgule.news/", languages=["ar", 'de', "en", "es", "fr", "it", "ua", "ru", "zh"])
        notrepays_docs = load_from_folder("ppn_data/2023/11/09/notrepays.today/", languages=["ar", 'de', "en", "es", "fr", "it", "ua", "ru", "zh"])
        docs = docs + lavirgule_docs + notrepays_docs
    return convert_json_list_to_pandas(docs)
