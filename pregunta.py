"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import csv

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";").drop(columns=['Unnamed: 0'])

    # Eliminando datos faltantes....
    df.dropna(inplace=True)
    # Eliminando datos duplicados...
    df.drop_duplicates(inplace=True)
    # Verificando shape...

    # Primera limpieza variable sexo....
    df["sexo"] = df.sexo.str.lower().astype(str).str.strip()
    
    # Limpieza 2 variable tipo_de_emprendimiento....
    df["tipo_de_emprendimiento"] = df.tipo_de_emprendimiento.str.lower().astype(str).str.strip()

    # Limpieza 3 variable idea_negocio...
    df["idea_negocio"] = df.idea_negocio.str.replace("-"," ", regex=True).str.replace("_"," ", regex=True).str.lower()

    # Limpieza 4 variable barrio...
    df["barrio"] = df.barrio.str.replace("_","-", regex=True).str.replace("-"," ", regex=True).str.lower()
    
    # Limpieza 5 variable fecha...
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], dayfirst=True)

    #Limpieza 6 variable monto_del_credito...
    # Eliminando simbolo de '$'...................................................
    df['monto_del_credito'] = df['monto_del_credito'].map(lambda x: x.lstrip('$'))
    # Extrayendo coma............................................................
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',', '')
    # Casteando el data type de monto_del_credito a tipo numérico..............................
    df.monto_del_credito = pd.to_numeric(df.monto_del_credito, errors='coerce')

    # Limpieza 7 variable línea_credito...
    df["línea_credito"] = df.línea_credito.str.replace("-"," ")
    df["línea_credito"] = df.línea_credito.str.replace("_"," ")
    df["línea_credito"] = df.línea_credito.str.lower()

    # Eliminamos duplicados y valores nulos
    df = df.drop_duplicates().dropna()


    return df

