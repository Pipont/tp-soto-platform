import pandas as pd
import pyreadstat

import re

def clean_column_name(name):
    name = name.lower()                           # minúsculas
    name = re.sub(r"[^\w\s]", "", name)           # elimina signos (incluye comas y guiones)
    name = re.sub(r"\s+", "_", name)              # espacios → guion bajo
    name = re.sub(r"_+", "_", name)               # elimina múltiples __
    return name.strip("_")                        # quita guiones bajos al inicio o fin


df, meta = pyreadstat.read_sav("data/3. BD DE ESTUDIANTES.sav", apply_value_formats=True)
column_map = dict(zip(meta.column_names, meta.column_labels))

print(column_map)
# Renombrar columnas con etiquetas
#df.rename(columns=column_map, inplace=True)


# Limpiar nombres
#df.columns = [clean_column_name(col) for col in df.columns]

#df.to_csv("dataset_pisa.csv",index=False)