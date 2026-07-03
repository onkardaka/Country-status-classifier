import streamlit as st  # es la libreria que nos va permitir crear la app web con los datos
import joblib  #esto sirve para cargar nuestro modelo guardado
import numpy as np # ya sabemos que sirve para hacer operaciones matemáticas avanzadas y manejar matrices o vectores numéricos.

# vamos a ponerle un titulo a la pagina, le dare el mismo estilo que mi modelo anterior de life expectancy
st.title("🌍 Clasificador del Estado de Desarrollo de Países")
st.write("Mueve las barras para predecir si un país es Desarrollado o en Desarrollo según sus índices.")

# este comando va cargar nuesto modelo que previamente he descargado del notebook
modelo = joblib.load('modelo_clasificador.pkl') #yo le puse este nombre, tu  pon el que quieras y que sea idencio y que todos estos archivo esten en la misma carpeta

#esto para crear barras deslizantes, los famosos sliders
escuela = st.slider("Años de Escolaridad (Schooling)", 0.0, 21.0, 12.0)
ingresos = st.slider("Índice de Composición de Recursos (Income Resources)", 0.0, 1.0, 0.5)

# para que cuando el usuario mueva las barras, metemos los datos en el modelo
#el modelo espera una lista con los datos de los dos variables que definimos : Escuela y ingresos
datos_entrada = np.array([[escuela, ingresos]])

# El modelo hace la predicción (entre 0 o 1) y calcula la probabilidad
prediccion = modelo.predict(datos_entrada)[0]
probabilidad = modelo.predict_proba(datos_entrada)[0] # Nos dice el % de seguridad

# ahora mostramos el resultado final en la pantalla con colores
st.subheader("Resultado de la Inteligencia Artificial:")

if prediccion == 1:
    st.success(f"🏆 País DESARROLLADO (Probabilidad: {probabilidad[1]*100:.1f}%)")
else:
    st.warning(f"🚜 País EN DESARROLLO (Probabilidad: {probabilidad[0]*100:.1f}%)")
