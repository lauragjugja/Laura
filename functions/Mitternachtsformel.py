import re
def Mitternachtsformel (quadratische_Formel):
    a = quadratische_Formel[0]
    b = quadratische_Formel[1]
    c = quadratische_Formel[2]

    d = b**2 - 4*a*c

    if d < 0:
        return "Keine reellen Lösungen"
    elif d == 0:
        x = -b / (2*a)
        return f"Eine doppelte Lösung: x = {x}"
    else:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        return f"Zwei Lösungen: x1 = {x1}, x2 = {x2}"
    
def parse_quadratic(s):
    """Parst Eingaben wie '2x^2+3x-5', 'x^2-x+1' oder ' -x^2 +4x - 4' -> [a, b, c]"""
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
# ...existing code...