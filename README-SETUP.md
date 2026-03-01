Setup & Troubleshooting for this workspace

1) PATH warnings (Windows)
- The installer warned that scripts are installed in:
  C:\Users\triaj\AppData\Roaming\Python\Python314\Scripts
- To add this to your PATH (PowerShell):

  setx PATH "$env:Path;C:\Users\triaj\AppData\Roaming\Python\Python314\Scripts"

  Then restart terminal/VS Code.

2) Safer alternative: virtual environment
- Create venv and activate:

  python -m venv .venv
  .\.venv\Scripts\Activate.ps1   # PowerShell

- Then install packages locally without --break-system-packages:

  pip install -r requirements.txt

3) If you need to reinstall kernel for VS Code/Jupyter
- After activating venv, run:

  python -m ipykernel install --user --name research-ai-agentic --display-name "Python (research-ai-agentic)"

4) Notes about previous installs
- I used a system-managed Python and applied `--break-system-packages` to install packages for the user account. That can be avoided by using a venv/conda.

5) Save/Export Notebook
- The notebook `Untitled-1.ipynb` is in the workspace. Use VS Code's Save As to rename or commit to git.
