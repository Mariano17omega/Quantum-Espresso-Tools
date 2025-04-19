import numpy as np

def parse_cell_parameters(cell_str):
    lines = cell_str.strip().split('\n')[1:]
    return [list(map(float, line.split())) for line in lines]

def generate_kpoint_mesh(cell_str, n1_min, n1_max, output_file="kpoints_uniform_spacing.txt"):
    cell_params = parse_cell_parameters(cell_str)
    a1, a2, a3 = np.array(cell_params)
    volume = np.dot(a1, np.cross(a2, a3))

    b1 = 2 * np.pi * np.cross(a2, a3) / volume
    b2 = 2 * np.pi * np.cross(a3, a1) / volume
    b3 = 2 * np.pi * np.cross(a1, a2) / volume

    b1_len = np.linalg.norm(b1)
    b2_len = np.linalg.norm(b2)
    b3_len = np.linalg.norm(b3)

    output_lines = ["### K_POINTS uniformes com base em n1:\n"]
    seen = set()

    for n1 in range(n1_min, n1_max + 1):
        # Determine n2 e n3 para manter espaçamento uniforme
        delta_k = b1_len / n1
        n2 = max(1, round(b2_len / delta_k))
        n3 = max(1, round(b3_len / delta_k))
        k_tuple = (n1, n2, n3)

        if k_tuple not in seen:
            seen.add(k_tuple)
            output_lines.append(f"# Espaçamento aproximado = {delta_k:.3f} Å⁻¹\n")
            output_lines.append("K_POINTS automatic\n")
            output_lines.append(f"{n1} {n2} {n3} 0 0 0\n\n")

    with open(output_file, 'w') as f:
        f.writelines(output_lines)

# CELL_PARAMETERS
cell_parameters = """CELL_PARAMETERS angstrom
      5.1535000000       0.0000000000       0.0000000000
      0.0316812498       8.9418438763       0.0000000000
     -1.9185587907      -0.2415925816       7.1331433149"""

# Faixa de valores para n1
n1_min = 4
n1_max = 12


generate_kpoint_mesh(cell_parameters, n1_min, n1_max)

