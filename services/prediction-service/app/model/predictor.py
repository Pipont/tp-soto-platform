import numpy as np
import json
import tensorflow as tf
import pandas as pd

# ============================
# CARGAR MODELO
# ============================
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(dir_path, 'modelo_rnn.h5')
scaler_mean_path = os.path.join(dir_path,'scaler_mean.npy')
scaler_scale_path = os.path.join(dir_path,'scaler_scale.npy')
columnas_modelo_path = os.path.join(dir_path,'columnas_modelo.json')

model = tf.keras.models.load_model(model_path)

def diagnostico_subcompetencias(data_dict):
    recomendaciones = []
    
    # Umbral mínimo deseado (por ejemplo, 480)
    umbral = 480

    # Subcompetencias claves
    subcompetencias = [
        'MATH_CANTIDAD', 'MATH_CAMBIO_REL', 'MATH_ESPACIO_FORMA',
        'MATH_DATOS_INCERT', 'MATH_FORMULACION', 'MATH_PROCEDIMIENTOS',
        'MATH_INTERPRETACION', 'MATH_RAZONAMIENTO'
    ]

    for sub in subcompetencias:
        puntaje = data_dict.get(sub)
        if puntaje is not None and puntaje < umbral:
            recomendaciones.append(f"⚠️ Reforzar la subcompetencia: {sub.replace('MATH_', '').capitalize()} (puntaje: {puntaje})")

    return recomendaciones

# ============================
# CARGAR SCALER
# ============================
scaler_mean = np.load(scaler_mean_path)
scaler_scale = np.load(scaler_scale_path)

# ============================
# CARGAR COLUMNAS USADAS EN EL ENTRENAMIENTO
# ============================
with open(columnas_modelo_path, "r") as f:
    columnas_ordenadas = json.load(f)

# ============================
# FUNCIÓN DE PREDICCIÓN
# ============================
def predecir_rendimiento(data_dict):

    # Convertir a DataFrame
    df = pd.DataFrame([data_dict])

    # Asegurarse del orden correcto de columnas
    df = df[columnas_ordenadas]

    #print("🚨 Columnas en df:", df.columns.tolist())
    #print("🎯 Esperadas por el modelo:", columnas_ordenadas)
    #print("❗ scaler_mean:", len(scaler_mean), "| scaler_scale:", len(scaler_scale))
    if "MATH_LOGRO" in df.columns:
        df = df.drop(columns=["MATH_LOGRO"])
    # Escalar los datos con los parámetros reales
    X = (df - scaler_mean) / scaler_scale

    # Darle la forma que espera la RNN
    X = np.expand_dims(X, axis=1)  # (batch_size, time_steps=1, features)

    # Predecir
    prediccion = model.predict(X)[0][0]

    # Recomendaciones por subcompetencia
    recomendaciones = diagnostico_subcompetencias(data_dict)
    
    # Redondear o categorizar según tu criterio
    return {
        "prediccion": float(prediccion),
        "recomendaciones": recomendaciones
    }
