import streamlit as st

st.set_page_config(
    page_title="FiberGuard AI",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 FiberGuard AI")
st.subheader("AI-Based Optical Fiber Fault Detection")

st.write(
    "An intelligent prototype for monitoring "
    "optical fibre performance and identifying "
    "possible signal faults."
)

st.divider()

st.header("📡 Optical Fiber Measurements")

col1, col2, col3 = st.columns(3)

with col1:
    signal = st.number_input(
        "Received Signal Power (dBm)",
        value=-15.5
    )

with col2:
    attenuation = st.number_input(
        "Attenuation (dB/km)",
        min_value=0.0,
        value=0.3
    )

with col3:
    length = st.number_input(
        "Fiber Length (km)",
        min_value=0.1,
        value=5.0
    )

if st.button("🔍 Analyze Fiber", use_container_width=True):

    st.header("Analysis Results")

    if signal >= -20 and attenuation <= 0.5:
        st.success("FIBER STATUS: NORMAL")

    elif signal >= -25 and attenuation <= 1.0:
        st.warning("FIBER STATUS: WARNING")

    else:
        st.error("FIBER STATUS: POSSIBLE FAULT")

    st.write("### Measurement Summary")

    st.write(f"Signal Power: {signal} dBm")
    st.write(f"Attenuation: {attenuation} dB/km")
    st.write(f"Fiber Length: {length} km")

    st.info(
        "Analysis completed using "
        "illustrative rule-based detection."
    )

st.divider()

st.caption(
    "FiberGuard AI | Optical Fiber Monitoring Prototype | 2026"
)
