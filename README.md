# Derbie

It's a tool to generate a malicious .deb file, that you can use on mitm attacks.

# Install

```bash
git clone https://github.com/mthbernardes/Derbie.git
cd Derbie
sudo pip3 install -r dependencies.txt
```

# Usage

```bash
python3 Derbie.py package-name payload-file
```

# Directories tree

```bash
.
|-- core
|   |-- __init__.py
|   `-- generator.py 		# Script responsible to generate the package
|-- debs			# Directory where all your .deb files will be stored
|-- Derbie.py			# Debie script
|-- packages			# Directory where all the packages created will be stored
|-- payload.sh			# Script with your malicious code
`-- templates			# Deb's default files templates
    |-- control			# Informations about the package
    `-- postinst		# Script that'll run after install

```
