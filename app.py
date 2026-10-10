import pandas as pd
import streamlit as st

# Custom mathematical computation engine
import analytics

st.set_page_config(page_title="Tech Market Analytics Engine", layout="wide")

st.title("🍁 Predictive Tech Job Market Analytics Platform")
st.write(
    "This system calculates role-specific insights and trains custom regression models from raw data chunks."
)

try:
    # 1. Ingest real parsed CSV data
    df = pd.read_csv("data.csv")

    # 2. Add the dynamic dropdown filter in the sidebar
    st.sidebar.header("Data Filter Settings")
    available_roles = sorted(df["Job_Title"].unique().tolist())
    selected_role = st.sidebar.selectbox("Select Target Job Role:", available_roles)

    # 3. Filter down to the selected job cluster
    filtered_df = df[df["Job_Title"] == selected_role]

    # Extract clean vectors for mathematical calculation
    salaries = filtered_df["Salary"].tolist()
    experience = filtered_df["Years_Experience"].tolist()

    # 4. Fire analytics using your custom modular code logic
    avg_salary = analytics.calculate_average(salaries)
    max_salary = analytics.find_max(salaries)
    min_salary = analytics.find_min(salaries)

    # 5. Display specific role card metrics across the screen layout
    st.subheader(f"📊 Market Overview for: {selected_role}")
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Average Market Base Pay", value=f"${avg_salary:,.2f}")
    col2.metric(label="Highest Recorded Offer", value=f"${max_salary:,.2f}")
    col3.metric(label="Lowest Recorded Offer", value=f"${min_salary:,.2f}")

    # 6. Train the ML predictive curve based purely on the filtered selection
    slope, intercept = analytics.train_salary_predictor(experience, salaries)

    # 7. Interactive Prediction Segment
    st.markdown("---")
    st.subheader(f"🔮 Custom {selected_role} Salary Predictor Engine")

    user_exp = st.slider(
        "Target Years of Industry Experience:",
        min_value=0.0,
        max_value=15.0,
        value=3.0,
        step=0.5,
    )

    # Compute prediction tracking using raw calculated parameters
    predicted_pay = analytics.predict_salary(user_exp, slope, intercept)

    st.metric(
        label=f"Statistical Salary Estimation for {user_exp} Yrs Experience",
        value=f"${predicted_pay:,.2f}",
    )

    # 8. Interactive Plotting Map
    st.subheader("Historical Market Sample Distributions")
    st.scatter_chart(filtered_df, x="Years_Experience", y="Salary", color="#FF4B4B")

except FileNotFoundError:
    st.error(
        "Could not discover 'data.csv' in your directory path. Execute 'generate_data.py' first!"
    )