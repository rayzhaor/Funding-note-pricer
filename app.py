
import streamlit as st

from calculation import calculate_funding_note


st.set_page_config(
    page_title="Funding Note Pricing Tool",
    layout="centered"
)

st.title("Funding Note Pricing Tool")

st.subheader("Input Parameters")

sofr = st.number_input(
    "SOFR (%)",
    value=4.00,
    step=0.01
)

floating = st.number_input(
    "Floating Spread (bps)",
    value=20,
    step=1
)

currency = st.text_input(
    "Currency",
    value="HKD"
)

spot = st.number_input(
    "Spot Rate",
    value=7.85,
    step=0.01
)

swap_pts = st.number_input(
    "Swap Points",
    value=-50,
    step=1
)

months = st.number_input(
    "Tenor (months)",
    value=1,
    min_value=1,
    step=1
)


if st.button("Calculate", type="primary"):

    result = calculate_funding_note(
        sofr=sofr,
        floating=floating,
        currency=currency,
        spot=spot,
        swap_pts=swap_pts,
        months=months
    )

    st.divider()

    st.subheader("Pricing Result")

    st.metric(
        label="Funding Note Rate",
        value=f"{result['note_rate']:.2f}%"
    )
