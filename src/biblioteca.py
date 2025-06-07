import os
import shutil
from pathlib import Path
from typing import List, Dict
from datetime import datetime

# Classe principal para gerenciar arquivos da biblioteca
class GerenciadorArquivos:
    def __init__(self, diretorio_base: str = "data"):
        self.diretorio_base = Path(diretorio_base)
        self.tipos_permitidos = {'.pdf', '.epub', '.txt'}
        # Mapeamento de tipos para subdiretórios
        self.diretorios_tipo = {
            '.pdf': 'artigos/pdf',
            '.epub': 'livros/epub',
            '.txt': 'documentos/txt'
        }
    
    # Lista todos os documentos digitais cadastrados
    def listar_documentos(self) -> List[Dict[str, str]]:
        documentos = []
        documentos_vistos = set()  # Evita duplicatas
        # Percorre as subpastas de cada tipo
        for pasta in self.diretorios_tipo.values():
            pasta_path = self.diretorio_base / pasta
            for arquivo in pasta_path.glob('**/*'):
                if arquivo.is_file() and arquivo.suffix.lower() in self.tipos_permitidos:
                    caminho_relativo = str(arquivo.relative_to(self.diretorio_base))
                    if caminho_relativo in documentos_vistos:
                        continue
                    documentos_vistos.add(caminho_relativo)
                    # Coleta informações do arquivo
                    stats = arquivo.stat()
                    tamanho = stats.st_size
                    data_criacao = datetime.fromtimestamp(stats.st_ctime)
                    data_modificacao = datetime.fromtimestamp(stats.st_mtime)
                    # Determina categoria
                    categoria = arquivo.parent.name
                    if categoria in ['pdf', 'txt', 'epub']:
                        categoria = arquivo.parent.parent.name
                    # Formata tamanho
                    if tamanho < 1024:
                        tamanho_formatado = f"{tamanho} bytes"
                    elif tamanho < 1024 * 1024:
                        tamanho_formatado = f"{tamanho/1024:.1f} KB"
                    else:
                        tamanho_formatado = f"{tamanho/(1024*1024):.1f} MB"
                    # Adiciona documento à lista
                    documentos.append({
                        'nome': arquivo.name,
                        'tipo': arquivo.suffix.lower(),
                        'ano': data_modificacao.year,
                        'caminho': caminho_relativo,
                        'tamanho': tamanho_formatado,
                        'data_criacao': data_criacao.strftime('%d/%m/%Y %H:%M'),
                        'ultima_modificacao': data_modificacao.strftime('%d/%m/%Y %H:%M'),
                        'categoria': categoria.capitalize(),
                        'status': 'Acessível' if arquivo.exists() else 'Não encontrado'
                    })
        # Ordena por categoria e nome
        documentos.sort(key=lambda x: (x['categoria'], x['nome']))
        return documentos

    # Adiciona um novo documento ao sistema
    def adicionar_documento(self, caminho_arquivo: str) -> bool:
        try:
            arquivo_origem = Path(caminho_arquivo)
            extensao = arquivo_origem.suffix.lower()
            if extensao not in self.tipos_permitidos:
                print(f"\nErro: Tipo de arquivo '{extensao}' não é permitido!")
                print(f"Tipos permitidos: {', '.join(self.tipos_permitidos)}")
                return False
            # Define diretório de destino
            diretorio_destino = self.diretorio_base / self.diretorios_tipo[extensao]
            diretorio_destino.mkdir(parents=True, exist_ok=True)
            arquivo_destino = diretorio_destino / arquivo_origem.name
            # Copia o arquivo
            shutil.copy2(arquivo_origem, arquivo_destino)
            print(f"\nDocumento adicionado com sucesso em: {arquivo_destino}")
            return True
        except Exception as e:
            print(f"\nErro ao adicionar documento: {str(e)}")
            return False

    # Renomeia um documento existente
    def renomear_documento(self, caminho_antigo: str, novo_nome: str) -> bool:
        try:
            arquivo_antigo = Path(caminho_antigo)
            extensao = arquivo_antigo.suffix
            novo_arquivo = arquivo_antigo.parent / f"{novo_nome}{extensao}"
            arquivo_antigo.rename(novo_arquivo)
            print(f"\nDocumento renomeado com sucesso para: {novo_arquivo.name}")
            return True
        except Exception as e:
            print(f"\nErro ao renomear documento: {str(e)}")
            return False

    # Remove um documento do sistema
    def remover_documento(self, caminho_arquivo: str) -> bool:
        try:
            arquivo = Path(caminho_arquivo)
            arquivo.unlink()
            print(f"\nDocumento removido com sucesso: {arquivo.name}")
            return True
        except Exception as e:
            print(f"\nErro ao remover documento: {str(e)}")
            return False

# Exibe o menu principal
def exibir_menu():
    print("\n=== Sistema de Gerenciamento de Biblioteca Digital ===")
    print("1. Listar todos os documentos")
    print("2. Adicionar novo documento")
    print("3. Renomear documento")
    print("4. Remover documento")
    print("5. Sair")
    print("=" * 50)

# Exibe a lista de documentos formatada
def exibir_documentos(documentos: List[Dict[str, str]]) -> None:
    if not documentos:
        print("\nNenhum documento encontrado.")
        return
    print("\nDocumentos encontrados:")
    categoria_atual = None
    for i, doc in enumerate(documentos, 1):
        if categoria_atual != doc['categoria']:
            categoria_atual = doc['categoria']
            print("\n" + "=" * 50)
            print(f"Categoria: {categoria_atual}")
            print("=" * 50)
        print(f"\n{i}. Nome: {doc['nome']}")
        print(f"   Tipo: {doc['tipo']}")
        print(f"   Tamanho: {doc['tamanho']}")
        print(f"   Criado em: {doc['data_criacao']}")
        print(f"   Última modificação: {doc['ultima_modificacao']}")
        print(f"   Status: {doc['status']}")
        print(f"   Caminho: {doc['caminho']}")
        print("-" * 50)

# Função principal do sistema
def main():
    gerenciador = GerenciadorArquivos()
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção (1-5): ").strip()
        if opcao == "1":
            documentos = gerenciador.listar_documentos()
            exibir_documentos(documentos)
            input("\nPressione Enter para continuar...")
        elif opcao == "2":
            print("\nAdicionar novo documento")
            print("=" * 50)
            print("Tipos de arquivo permitidos:", ", ".join(gerenciador.tipos_permitidos))
            caminho = input("\nDigite o caminho completo do arquivo: ").strip()
            if caminho:
                gerenciador.adicionar_documento(caminho)
            else:
                print("\nNenhum caminho fornecido!")
            input("\nPressione Enter para continuar...")
        elif opcao == "3":
            menu_renomear(gerenciador)
        elif opcao == "4":
            menu_remover(gerenciador)
        elif opcao == "5":
            print("\nObrigado por usar o Sistema de Gerenciamento de Biblioteca Digital!")
            break
        else:
            print("\nOpção inválida! Por favor, escolha 1, 2, 3, 4 ou 5.")
            input("Pressione Enter para continuar...")

# Menu para renomear documentos
def menu_renomear(biblioteca: GerenciadorArquivos) -> None:
    print("\nRenomear documento")
    print("=" * 50)
    documentos = biblioteca.listar_documentos()
    exibir_documentos(documentos)
    try:
        num_doc = int(input("\nDigite o número do documento a ser renomeado: "))
        if num_doc < 1 or num_doc > len(documentos):
            print("\nNúmero de documento inválido!")
            return
        novo_nome = input("Digite o novo nome (sem extensão): ").strip()
        if not novo_nome:
            print("\nNome inválido!")
            return
        documento = documentos[num_doc - 1]
        biblioteca.renomear_documento(documento['caminho'], novo_nome)
    except ValueError:
        print("\nEntrada inválida! Digite um número.")

# Menu para remover documentos
def menu_remover(biblioteca: GerenciadorArquivos) -> None:
    print("\nRemover documento")
    print("=" * 50)
    documentos = biblioteca.listar_documentos()
    exibir_documentos(documentos)
    try:
        num_doc = int(input("\nDigite o número do documento a ser removido: "))
        if num_doc < 1 or num_doc > len(documentos):
            print("\nNúmero de documento inválido!")
            return
        documento = documentos[num_doc - 1]
        confirmacao = input(f"\nTem certeza que deseja remover '{documento['nome']}'? (s/n): ").lower()
        if confirmacao == 's':
            biblioteca.remover_documento(documento['caminho'])
        else:
            print("\nOperação cancelada!")
    except ValueError:
        print("\nEntrada inválida! Digite um número.")

if __name__ == "__main__":
    main()