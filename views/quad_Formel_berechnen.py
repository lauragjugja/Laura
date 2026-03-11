import streamlit as st
from functions.Mitternachtsformel import Mitternachtsformel, parse_quadratic
st.title("Mitternachtsformel berechnen")

st.write("Die Mitternachtsformel, auch bekannt als die quadratische Lösungsformel, ist eine Methode zur Berechnung der Lösungen einer quadratischen Gleichung der Form ax^2 + bx + c = 0. Die Formel lautet: x = (-b ± √(b^2 - 4ac)) / (2a).")

st.write("Hier kannst du die Mitternachtsformel anwenden, um die Lösungen einer quadratischen Gleichung zu berechnen.")

input_string = st.text_input("Gib die quadratische Gleichung ein (z.B. 2x^2 + 3x - 5):")

if input_string:
    quadratische_Formel = parse_quadratic(input_string)
    result = Mitternachtsformel(quadratische_Formel)
    st.write("Das Ergebnis ist:", result)

# --- NEW CODE to display the history table ---
if "data_df" in st.session_state:
    st.dataframe(st.session_state['data_df'])