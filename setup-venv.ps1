# Create and activate a virtual environment (safer than --break-system-packages)
# Run this in PowerShell to set up a clean isolated environment

Write-Host "Creating virtual environment .venv..." -ForegroundColor Green
python -m venv .venv

Write-Host "Activating virtual environment..." -ForegroundColor Green
.\.venv\Scripts\Activate.ps1

Write-Host "Installing packages from requirements.txt..." -ForegroundColor Green
pip install -r requirements.txt

Write-Host "Installing ipykernel for Jupyter..." -ForegroundColor Green
python -m ipykernel install --user --name research-ai-agentic --display-name "Python (research-ai-agentic)"

Write-Host "Setup complete! Virtual environment is active." -ForegroundColor Green
Write-Host "To deactivate later, run: deactivate" -ForegroundColor Yellow
