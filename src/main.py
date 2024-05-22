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
        st.write(f"Your calculated CPI is {cpi :.2f}")


def main():
    st.header("CPI Calculator")
    current = st.slider(
        label="Current CPI", min_value=0.00, max_value=10.00, step=0.01, value=6.00
    )
    sems_passed = st.slider(
        label="Semesters Completed", min_value=1, max_value=9, step=1, value=5
    )

    show_calc(current=current, sems_passed=sems_passed, total_sems=10)


if __name__ == "__main__":
    main()
