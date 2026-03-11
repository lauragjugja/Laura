import streamlit as st
import re
from datetime import datetime
import pytz


def Mitternachtsformel(quadratische_Formel):
    a, b, c = quadratische_Formel
    d = b**2 - 4*a*c

    if d < 0:
        return None, None, "Keine reellen Lösungen"
    elif d == 0:
        x = -b / (2*a)
        return x, x, "Eine doppelte Lösung"
    else:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        return x1, x2, "Zwei Lösungen"


def parse_quadratic(s):
    s = s.replace('−', '-').replace(' ', '')

    def to_num(t):
        if t in ('', '+'):
            return 1.0
        if t == '-':
            return -1.0
        return float(t)

    m_a = re.search(r'([+-]?\d*\.?\d*)x\^2', s, re.IGNORECASE)
    a = to_num(m_a.group(1)) if m_a else 0.0

    m_b = re.search(r'([+-]?\d*\.?\d*)x(?!\^)', s, re.IGNORECASE)
    b = to_num(m_b.group(1)) if m_b else 0.0

    s_rest = re.sub(r'([+-]?\d*\.?\d*)x\^2', '', s, flags=re.IGNORECASE)
    s_rest = re.sub(r'([+-]?\d*\.?\d*)x(?!\^)', '', s_rest, flags=re.IGNORECASE)

    if s_rest == '':
        c = 0.0
    else:
        nums = re.findall(r'[+-]?\d*\.?\d+', s_rest)
        c = sum(float(n) for n in nums) if nums else 0.0

    return [a, b, c]


def main():

    st.title("Mitternachtsformel Rechner")

    if "history" not in st.session_state:
        st.session_state.history = []

    eingabe = st.text_input("Quadratische Formel eingeben (z.B. 2x^2 + 3x - 5)")

    if st.button("Eingeben"):

        quadratische_Formel = parse_quadratic(eingabe)
        x1, x2, text = Mitternachtsformel(quadratische_Formel)

        result = {
            "timestamp": datetime.now(pytz.timezone('Europe/Zurich')),
            "formel": eingabe,
            "x1": x1,
            "x2": x2,
            "beschreibung": text
        }

        st.session_state.history.append(result)

    # letzte Lösung anzeigen
    if st.session_state.history:

        last = st.session_state.history[-1]

        st.subheader("Lösung")

        st.write(last["beschreibung"])

        if last["x1"] is not None:
            st.write(f"x₁ = {last['x1']}")
            st.write(f"x₂ = {last['x2']}")

    # Verlauf
    st.subheader("Berechnungsverlauf")

    for r in reversed(st.session_state.history):

        st.write(f"Zeit: {r['timestamp']}")
        st.write(f"Formel: {r['formel']}")

        if r["x1"] is not None:
            st.write(f"x₁ = {r['x1']}")
            st.write(f"x₂ = {r['x2']}")
        else:
            st.write("Keine reellen Lösungen")

        st.write("---")


if __name__ == "__main__":
    main()