import streamlit as st
from sodapy import Socrata
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from dotenv import load_dotenv
load_dotenv('.env')

APP_TOKEN = os.getenv('TOKEN_SODAPY')
DATASET_ID = os.getenv('DATASET_ID')

st.title('Contratos')
st.write('Mi primer aplicativo para contratos')

client = Socrata("www.datos.gov.co", 'xv66xLFwvXNRjMns6TbebGarR')

Query = """ 
select
    id_contrato, nombre_entidad, departamento, descripcion_del_proceso, valor_del_contrato, fecha_de_firma
where
    fecha_de_firma > '2024-01-01'
limit
10000000
"""

result = client.get("jbjy-vk9h", query = Query)

df = pd.DataFrame.from_records(result)

Entidad = st.selectbox('seleccione un contrato', df['nombre_entidad'])

dataset_Entidad = df[df['nombre_entidad'] == Entidad].transpose

st.dataframe(dataset_Entidad)



