import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AI Market Viewer",
    layout="wide"
)

st.title("📈 AI Market Viewer")

st.sidebar.header("Controls")

market = st.sidebar.selectbox(
    "Select Market",
    ["Shares", "Crypto"]
)

symbol = st.sidebar.text_input(
    "Symbol",
    "RELIANCE" if market == "Shares" else "BTCUSDT"
)

timeframe = st.sidebar.selectbox(
    "Timeframe",
    ["1", "5", "15", "60", "D"]
)

st.divider()

st.subheader(f"{market} Chart : {symbol}")

if market == "Shares":
    widget = f"""
    <div class="tradingview-widget-container">
      <div id="tv_chart"></div>
      <script src="https://s3.tradingview.com/tv.js"></script>
      <script>
      new TradingView.widget({{
        width: "100%",
        height: 600,
        symbol: "{symbol}",
        interval: "{timeframe}",
        timezone: "Asia/Kolkata",
        theme: "light",
        style: "1",
        locale: "en",
        toolbar_bg: "#f1f3f6",
        allow_symbol_change: true,
        container_id: "tv_chart"
      }});
      </script>
    </div>
    """
    components.html(widget, height=620)
else:
    st.info("Crypto chart will appear here next step.")
