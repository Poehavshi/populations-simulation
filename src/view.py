import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

from src.model import simulate


def make_grid(cols, rows):
    grid = [0] * cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid


def quantity_of_specie_form(index):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader(str(index))
    with col2:
        quantity = st.number_input("Количество", min_value=0, step=1, key=str(index) + "q")
    with col3:
        increase = st.number_input("Коэффициент прироста", step=0.0001, key=str(index) + "i", format="%.5f")
    return quantity, increase


def interaction_coefficients_form(number_of_species):
    b_matrix = np.zeros((number_of_species, number_of_species))
    grid = make_grid(number_of_species, number_of_species)
    for i in range(number_of_species):
        for j in range(number_of_species):
            b_matrix[i][j] = grid[i][j].number_input(f"{i}{j}", key=str(i) + str(j) + "interaction", format="%.5f")
    return b_matrix


def main_page():
    st.markdown("# Population simulation")
    with st.sidebar:
        time_step = st.number_input("Шаг дифференцирования", value=1)
        total_time_interval = st.number_input("Время моделирования", value=1000)
    number_of_species = st.number_input("Введите число видов $$ a_i $$", min_value=1, value=2)
    tab1, tab2 = st.tabs(["Численность популяции и прирост", "Коэффициенты взаимодействия"])

    quantities = np.zeros(number_of_species)
    increases = np.zeros(number_of_species)
    with tab1:
        for i in range(number_of_species):
            quantities[i], increases[i] = quantity_of_specie_form(i)
    print(quantities, increases)

    with tab2:
        b_matrix = interaction_coefficients_form(number_of_species)
    print(b_matrix)

    first_data, second_data = simulate(b_matrix, quantities, increases, total_time_interval, time_step)

    fig, ax = plt.subplots()
    ax.plot(np.arange(0, total_time_interval+2, time_step), first_data)
    ax.plot(np.arange(0, total_time_interval + 2, time_step), second_data)
    st.pyplot(fig)
