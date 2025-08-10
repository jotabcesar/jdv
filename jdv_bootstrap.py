# jdv_bootstrap.py - recria diretórios e arquivos do projeto JDV (backend + app).
import os, sys, pathlib, json, textwrap
DATA = {}
def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,'w',encoding='utf-8') as f: f.write(content)
base = sys.argv[1] if len(sys.argv)>1 else 'JDV_project_out'
os.makedirs(base, exist_ok=True)
for rel, txt in DATA.items():
    write(os.path.join(base, rel), txt)
print(f'Projeto recriado em: {base} (arquivos: {len(DATA)})')