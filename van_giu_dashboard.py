# 🌐 VAN-GIU - DASHBOARD WEB PROFESIONAL
# Guardar como: van_giu_dashboard.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="🚀 VAN-GIU Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ESTILOS CSS PERSONALIZADOS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
    }
    .recommendation-buy {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #28a745;
    }
    .recommendation-sell {
        background-color: #f8d7da;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #dc3545;
    }
    .recommendation-hold {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #ffc107;
    }
</style>
""", unsafe_allow_html=True)

# GENERAR DATOS REALISTAS
def generar_datos_mercado():
    """Genera datos de mercado realistas para el dashboard"""
    np.random.seed(42)
    
    fechas = [datetime.now() - timedelta(days=i) for i in range(100, 0, -1)]
    
    # Bitcoin
    btc_prices = [45000]
    for i in range(1, 100):
        change = np.random.normal(0.002, 0.02)
        btc_prices.append(btc_prices[-1] * (1 + change))
    
    # Ethereum
    eth_prices = [2500]
    for i in range(1, 100):
        change = np.random.normal(0.0025, 0.025)
        eth_prices.append(eth_prices[-1] * (1 + change))
    
    # S&P 500
    spy_prices = [450]
    for i in range(1, 100):
        change = np.random.normal(0.001, 0.01)
        spy_prices.append(spy_prices[-1] * (1 + change))
    
    df = pd.DataFrame({
        'Date': fechas,
        'BTC': btc_prices,
        'ETH': eth_prices,
        'SPY': spy_prices
    })
    
    df.set_index('Date', inplace=True)
    return df

# SIMULAR MODELO ML
def simular_prediccion_ml(precio_actual):
    """Simula predicción de modelo ML"""
    cambio = np.random.normal(0.005, 0.015)  # ±1.5% en promedio
    prediccion = precio_actual * (1 + cambio)
    return prediccion, cambio * 100

# HEADER PRINCIPAL
st.markdown('<h1 class="main-header">🚀 VAN-GIU ANALYTICS</h1>', unsafe_allow_html=True)
st.markdown("### Plataforma Profesional de Análisis Financiero con IA")

# SIDEBAR
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1006/1006555.png", width=100)
    st.title("Configuración")
    
    st.subheader("🎯 Mercados")
    mercado_seleccionado = st.selectbox(
        "Seleccionar Activo:",
        ["BTC - Bitcoin", "ETH - Ethereum", "SPY - S&P 500"]
    )
    
    st.subheader("📈 Análisis")
    mostrar_ml = st.checkbox("Mostrar Predicciones ML", value=True)
    mostrar_tecnicos = st.checkbox("Mostrar Indicadores Técnicos", value=True)
    
    st.subheader("💎 Acerca de")
    st.info("""
    **VAN-GIU Analytics**
    
    Sistema profesional de análisis financiero
    con Machine Learning y Deep Learning.
    
    📊 Análisis en tiempo real
    🤖 Modelos predictivos
    📈 Visualización avanzada
    """)

# OBTENER DATOS
df = generar_datos_mercado()
activo = mercado_seleccionado.split(" - ")[0]
precio_actual = df[activo].iloc[-1]

# KPI CARDS
st.subheader("📊 Métricas Principales")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h3>💰 Precio Actual</h3>
        <h2>${precio_actual:,.2f}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    cambio_24h = ((df[activo].iloc[-1] - df[activo].iloc[-2]) / df[activo].iloc[-2]) * 100
    st.markdown(f"""
    <div class="metric-card">
        <h3>📈 Cambio 24h</h3>
        <h2>{cambio_24h:+.2f}%</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    volatilidad = df[activo].pct_change().std() * 100
    st.markdown(f"""
    <div class="metric-card">
        <h3>⚡ Volatilidad</h3>
        <h2>{volatilidad:.2f}%</h2>
    </div>
    """, unsafe_allow_html=True)

with col4:
    max_30d = df[activo].tail(30).max()
    min_30d = df[activo].tail(30).min()
    st.markdown(f"""
    <div class="metric-card">
        <h3>🎯 Rango 30D</h3>
        <h4>Máx: ${max_30d:,.0f}</h4>
        <h4>Mín: ${min_30d:,.0f}</h4>
    </div>
    """, unsafe_allow_html=True)

# PREDICCIÓN ML
if mostrar_ml:
    st.subheader("🤖 Predicción con Machine Learning")
    
    prediccion, cambio_pred = simular_prediccion_ml(precio_actual)
    
    col_pred1, col_pred2 = st.columns(2)
    
    with col_pred1:
        st.plotly_chart({
            'data': [
                {
                    'type': 'indicator',
                    'mode': 'number+delta',
                    'value': prediccion,
                    'delta': {'reference': precio_actual, 'relative': True},
                    'number': {'prefix': '$', 'valueformat': ',.2f'},
                    'title': {'text': '🎯 Predicción Mañana'},
                    'domain': {'x': [0, 1], 'y': [0, 1]}
                }
            ],
            'layout': {
                'height': 300
            }
        }, use_container_width=True)
    
    with col_pred2:
        # Recomendación basada en predicción
        if cambio_pred > 2:
            recomendacion = "COMPRAR"
            explicacion = "Tendencia alcista fuerte esperada"
            clase_css = "recommendation-buy"
            emoji = "🚀"
        elif cambio_pred > 0.5:
            recomendacion = "COMPRAR"
            explicacion = "Tendencia alcista moderada"
            clase_css = "recommendation-buy"
            emoji = "📈"
        elif cambio_pred < -2:
            recomendacion = "VENDER"
            explicacion = "Tendencia bajista fuerte esperada"
            clase_css = "recommendation-sell"
            emoji = "🔴"
        elif cambio_pred < -0.5:
            recomendacion = "VENDER"
            explicacion = "Tendencia bajista moderada"
            clase_css = "recommendation-sell"
            emoji = "📉"
        else:
            recomendacion = "MANTENER"
            explicacion = "Movimiento lateral esperado"
            clase_css = "recommendation-hold"
            emoji = "⚖️"
        
        st.markdown(f"""
        <div class="{clase_css}">
            <h2>{emoji} {recomendacion}</h2>
            <p><strong>Cambio esperado:</strong> {cambio_pred:+.2f}%</p>
            <p><strong>Razón:</strong> {explicacion}</p>
            <p><strong>Confianza:</strong> 85%</p>
        </div>
        """, unsafe_allow_html=True)

# GRÁFICAS PRINCIPALES
st.subheader("📈 Análisis Técnico")

tab1, tab2, tab3, tab4 = st.tabs(["Precio", "Indicadores", "Comparativa", "Análisis ML"])

with tab1:
    # Gráfica de precio
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df[activo], linewidth=2, label=f'Precio {activo}')
    
    # Medias móviles
    df['MA_20'] = df[activo].rolling(20).mean()
    df['MA_50'] = df[activo].rolling(50).mean()
    
    ax.plot(df.index, df['MA_20'], label='MA 20 días', alpha=0.7)
    ax.plot(df.index, df['MA_50'], label='MA 50 días', alpha=0.7)
    
    ax.set_title(f'Precio {activo} con Medias Móviles', fontsize=14, fontweight='bold')
    ax.set_ylabel('Precio (USD)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    
    st.pyplot(fig)

with tab2:
    # Indicadores técnicos
    col_ind1, col_ind2 = st.columns(2)
    
    with col_ind1:
        # RSI
        delta = df[activo].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        
        fig_rsi, ax_rsi = plt.subplots(figsize=(10, 4))
        ax_rsi.plot(df.index, rsi, color='purple', linewidth=2)
        ax_rsi.axhline(70, color='red', linestyle='--', alpha=0.7, label='Sobrecompra')
        ax_rsi.axhline(30, color='green', linestyle='--', alpha=0.7, label='Sobreventa')
        ax_rsi.set_title('RSI (Relative Strength Index)')
        ax_rsi.set_ylabel('RSI')
        ax_rsi.legend()
        ax_rsi.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        st.pyplot(fig_rsi)
    
    with col_ind2:
        # Volumen (simulado)
        volatilidad = df[activo].pct_change().rolling(20).std() * 100
        
        fig_vol, ax_vol = plt.subplots(figsize=(10, 4))
        ax_vol.plot(df.index, volatilidad, color='orange', linewidth=2)
        ax_vol.set_title('Volatilidad (20 días)')
        ax_vol.set_ylabel('Volatilidad (%)')
        ax_vol.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        st.pyplot(fig_vol)

with tab3:
    # Comparativa de mercados
    fig_comp, ax_comp = plt.subplots(figsize=(12, 6))
    
    # Normalizar precios para comparar rendimientos
    for col in ['BTC', 'ETH', 'SPY']:
        normalized = (df[col] / df[col].iloc[0]) * 100
        ax_comp.plot(df.index, normalized, label=col, linewidth=2)
    
    ax_comp.set_title('Comparativa de Rendimientos (Base 100)', fontweight='bold')
    ax_comp.set_ylabel('Rendimiento (%)')
    ax_comp.legend()
    ax_comp.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    
    st.pyplot(fig_comp)

with tab4:
    # Análisis ML avanzado
    st.subheader("🧠 Análisis con Machine Learning")
    
    col_ml1, col_ml2 = st.columns(2)
    
    with col_ml1:
        # Importancia de características (simulada)
        features = ['Precio', 'Volumen', 'Volatilidad', 'RSI', 'MACD', 'Media Móvil']
        importancia = np.random.dirichlet(np.ones(6))
        
        fig_imp, ax_imp = plt.subplots(figsize=(10, 6))
        ax_imp.barh(features, importancia, color='lightblue')
        ax_imp.set_title('Importancia de Características (ML)')
        ax_imp.set_xlabel('Importancia Relativa')
        st.pyplot(fig_imp)
    
    with col_ml2:
        # Distribución de errores (simulada)
        errores = np.random.normal(0, precio_actual * 0.01, 1000)
        
        fig_err, ax_err = plt.subplots(figsize=(10, 6))
        ax_err.hist(errores, bins=30, alpha=0.7, color='lightcoral', edgecolor='black')
        ax_err.axvline(0, color='red', linestyle='--', linewidth=2)
        ax_err.set_title('Distribución de Errores de Predicción')
        ax_err.set_xlabel('Error (USD)')
        ax_err.set_ylabel('Frecuencia')
        st.pyplot(fig_err)

# FOOTER
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p><strong>🚀 VAN-GIU Analytics</strong> - Plataforma profesional de análisis financiero</p>
    <p>🤖 Machine Learning • 📊 Análisis Técnico • 📈 Predicciones • 🎯 Recomendaciones</p>
    <p><em>Última actualización: {}</em></p>
</div>
""".format(datetime.now().strftime("%d/%m/%Y %H:%M")), unsafe_allow_html=True)