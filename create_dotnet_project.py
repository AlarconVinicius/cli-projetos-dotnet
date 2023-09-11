import os
import subprocess

def criar_pasta(nome_pasta):
    os.mkdir(nome_pasta)
    print(f"Criando pasta {nome_pasta}...")
    
def criar_projeto(nome_sln, nome_pasta, tipo_projeto):
    nome_proj = nome_pasta.split('-', 1)[1].strip()
    projeto_nome = f"{nome_sln}.{nome_proj}"
    os.chdir(nome_pasta)
    subprocess.run(["dotnet", "new", tipo_projeto, "-n", projeto_nome])
    os.chdir("..")
    print(f"Criando projeto {projeto_nome}...")
    
def criar_solucao(nome_sln):
    os.mkdir(nome_sln)
    os.chdir(nome_sln)
    subprocess.run(["dotnet", "new", "sln", "-n", nome_sln])
    os.chdir(".")
    print(f"Criando solução {nome_sln}...")
    
def main():
    pasta_src = "src"
    nome_sln = input("Digite o nome da solução: ")
    criar_solucao(nome_sln)
    criar_pasta(pasta_src)
    os.chdir(pasta_src)
    pastas = ["0-Test", "1-Api", "2-Domain", "3-Infra", "4-Entities"]
    tipos_projetos = ["xunit", "webapi", "classlib", "classlib", "classlib"]
    
    for pasta, tipo_projeto in zip(pastas, tipos_projetos):
        nome_proj = pasta.split('-', 1)[1].strip()
        criar_pasta(pasta)
        criar_projeto(nome_sln, pasta, tipo_projeto)
        print(f"Diretório atual: {os.getcwd()})")
        os.chdir("..")
        print(f"Diretório atual: {os.getcwd()})")
        subprocess.run(["dotnet", "sln", f"{nome_sln}.sln", "add", f"{pasta_src}/{pasta}/{nome_sln}.{nome_proj}/{nome_sln}.{nome_proj}.csproj"])
        os.chdir(pasta_src)
        print(f"Diretório atual: {os.getcwd()})")
    
    os.chdir("..")
    print(f"Gerando gitignore...")
    subprocess.run(["dotnet", "new", "gitignore"])
    subprocess.run(["dotnet", "build"])
    
    print(f"Estrutura do projeto {nome_sln} foi criada com sucesso!")

if __name__ == "__main__":
    main()