#!/usr/bin/env python3
"""
Setup script for Heart Disease Prediction Project
Run this script to automatically set up the project environment.
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is adequate"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7 or higher is required")
        return False
    print(f"✅ Python {version.major}.{version.minor} detected")
    return True

def main():
    """Main setup function"""
    print("🚀 Setting up Heart Disease Prediction Project")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install packages
    if not run_command("pip install -r requirements.txt", 
                      "Installing required packages"):
        print("⚠️  Package installation failed. Trying with --break-system-packages...")
        if not run_command("pip install --break-system-packages -r requirements.txt",
                          "Installing packages with system override"):
            print("❌ Failed to install packages. Please install manually.")
            sys.exit(1)
    
    # Verify heart.csv exists
    if not os.path.exists("heart.csv"):
        print("⚠️  heart.csv not found. Downloading from UCI repository...")
        download_script = '''
from ucimlrepo import fetch_ucirepo
import pandas as pd

heart_disease = fetch_ucirepo(id=45)
X = heart_disease.data.features
y = heart_disease.data.targets
data = pd.concat([X, y], axis=1)
data.to_csv("heart.csv", index=False)
print("Dataset downloaded successfully")
'''
        if not run_command(f'python3 -c "{download_script}"', 
                          "Downloading heart disease dataset"):
            print("❌ Failed to download dataset")
            sys.exit(1)
    else:
        print("✅ heart.csv already exists")
    
    # Verify setup
    verify_script = '''
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn

data = pd.read_csv("heart.csv")
print(f"✅ Setup verification successful!")
print(f"Dataset: {len(data)} rows, {len(data.columns)} columns")
'''
    
    if run_command(f'python3 -c "{verify_script}"', 
                  "Verifying setup"):
        print("\n🎉 Setup completed successfully!")
        print("\nNext steps:")
        print("1. Start Jupyter: jupyter notebook")
        print("2. Open: HeartCSV (2).ipynb")
        print("3. Run the cells to explore the analysis")
        print("\nFor help, see README.md")
    else:
        print("❌ Setup verification failed")
        sys.exit(1)

if __name__ == "__main__":
    main()