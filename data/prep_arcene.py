#!/usr/bin/env python3


import pandas as pd


df_train = pd.read_csv('./data/arcene/arcene_train.data',
                       sep='\\ ', header=None)
lab = pd.read_csv('./data/arcene/arcene_train.labels', header=None)
df_train['target'] = lab[0].tolist()


df_val = pd.read_csv('./data/arcene/arcene_valid.data', sep='\\ ', header=None)
lab = pd.read_csv('./data/arcene/arcene_valid.labels', header=None)
df_val['target'] = lab[0].tolist()


df = pd.concat([df_train, df_val])
df['target'] = df['target'].map({-1: 0, 1: 1}).tolist()
df.to_csv('./data/arcene.csv', sep=',', index=False)
