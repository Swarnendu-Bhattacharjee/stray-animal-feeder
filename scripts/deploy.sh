#!/bin/bash
# ==========================================================
# Stray Animal Feeder Project - Deployment Script
# Author: Swarnendu Bhattacharjee
# Description: Sets up virtual environment, installs dependencies, 
#              and initializes the StrayMate AI Bot environment
# ==========================================================

echo "==============================="
echo "Starting deployment..."
echo "==============================="

# 1. Create Python virtual environment
echo "[Step 1] Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# 2. Upgrade pip
echo "[Step 2] Upgrading pip..."
pip install --upgrade pip

# 3. Install dependencies from requirements.txt
echo "[Step 3] Installing required packages..."
pip install -r requirements.txt

# 4. Initialize AI model (placeholder)
echo "[Step 4] Downloading NLP model (GPT2)..."
python - <<END
from transformers import AutoTokenizer, AutoModelForCausalLM
AutoTokenizer.from_pretrained("gpt2")
AutoModelForCausalLM.from_pretrained("gpt2")
END

# 5. Confirm setup
echo "[Step 5] Deployment completed successfully!"
echo "Activate environment with: source venv/bin/activate"
echo "Run the bot with: python src/main.py"
echo "==============================="
