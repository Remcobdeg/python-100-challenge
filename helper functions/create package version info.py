import subprocess
import sys

# Get the list of installed packages
result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE, text=True)

# Get the Python version
python_version = f"# Python version: {sys.version.split()[0]}"

# Save to requirements.txt
with open('requirements.txt', 'w') as file:
    file.write(f"{python_version}\n\n{result.stdout}")

print("requirements.txt file with Python version created!")
