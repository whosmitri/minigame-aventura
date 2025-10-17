"""
módulo: run.py

Este módulo contém as linhas de código que iniciam o programa.

Dependências:
- main
"""

import main

# --- INICIAR O PROGRAMA ---
if __name__ == "__main__":
    app = main.AppJogo()
    app.mainloop()