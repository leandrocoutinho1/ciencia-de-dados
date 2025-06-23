from pathlib import Path
from amostragem import amostragem_sem_reposicao

input_dir = Path("data/input")
input_filename = "student-mat.csv"

output_dir = Path("data/output")
output_dir.mkdir(parents=True, exist_ok=True)

input_path = input_dir / input_filename
output_filename = f"amostra-{input_filename}"
output_path = output_dir / output_filename

tamanho_amostra = 50
semente = 42

amostragem_sem_reposicao(
    input_csv=str(input_path),
    output_csv=str(output_path),
    tamanho_amostra=tamanho_amostra,
    random_state=semente
)
