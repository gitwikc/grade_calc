import streamlit as st
import numpy as np


def show_calc(current: float, sems_passed: int, total_sems: int = 10) -> None:
    cols = st.columns(2, gap="medium")

    completed = sems_passed / total_sems
    cpi = current * completed

    with cols[0]:
        st.subheader("Estimated SPI in Remaining Semesters")
        remaining = np.mean(
            [
                st.slider(
                    label=f"SPI in Sem {i + 1}",
                    min_value=0.00,
                    max_value=10.00,
                    value=6.00,
                    step=0.01,
                )
                for i in range(sems_passed, total_sems)
            ]
        )

    with cols[1]:
        cpi = current * completed + remaining * (1 - completed)
        st.subheader("Estimated CPI")
        st.metric(label="CPI", value=f"{cpi :.2f}", delta=f"{(cpi - current) :.2f}")


def main():
    st.set_page_config(page_icon=":clipboard:", page_title="CalcMyGrade")
    st.title("CalcMyGrade - CPI Calculator")
    current = st.slider(
        label="Current CPI", min_value=0.00, max_value=10.00, step=0.01, value=6.00
    )
    sems_passed = st.slider(
        label="Semesters Completed", min_value=1, max_value=9, step=1, value=5
    )
    total_sems = st.slider(
        label="Semesters Completed",
        min_value=sems_passed + 1,
        max_value=10,
        step=1,
        value=10,
    )

    show_calc(current=current, sems_passed=sems_passed, total_sems=total_sems)


if __name__ == "__main__":
    main()
