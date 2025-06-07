import os
import shutil
from pathlib import Path
from typing import List, Dict
from datetime import datetime

class GerenciadorArquivos:
    def __init__(self, diretorio_base: str = "data"):
        self.diretorio_base = Path(diretorio_base)
        self.tipos_permitidos = {'.pdf', '.epub', '.txt'}
        # Mapeamento de tipos para diretórios
        self.diretorios_tipo = {
            '.pdf': 'artigos/pdf',
            '.epub': 'livros/epub',
            '.txt': 'documentos/txt'
        }
    
    def listar_documentos(self) -> List[Dict[str, str]]:
        """
        Lista todos os documentos digitais no diretório base.
        """
        documentos = []
        
        # Verifica se o diretório existe
        if not self.diretorio_base.exists():
            return []
        
        # Lista todos os documentos permitidos
        for tipo in self.tipos_permitidos:
            for arquivo in self.diretorio_base.glob(f'**/*{tipo}'):
                if arquivo.is_file():
                    # Obtém o ano da última modificação do arquivo
                    ano_publicacao = datetime.fromtimestamp(arquivo.stat().st_mtime).year
                    
                    documentos.append({
                        'nome': arquivo.name,
                        'caminho': str(arquivo),
                        'tipo': tipo,
                        'ano': ano_publicacao
                    })
        
        return documentos

    def adicionar_documento(self, caminho_arquivo: str) -> bool:
        """
        Adiciona um novo documento ao sistema.
        
        """
        try:
            arquivo_origem = Path(caminho_arquivo)
            
            # Verifica se é um tipo permitido
            extensao = arquivo_origem.suffix.lower()
            if extensao not in self.tipos_permitidos:
                print(f"\nErro: Tipo de arquivo '{extensao}' não é permitido!")
                print(f"Tipos permitidos: {', '.join(self.tipos_permitidos)}")
                return False
            
            # Define o diretório de destino
            diretorio_destino = self.diretorio_base / self.diretorios_tipo[extensao]
            diretorio_destino.mkdir(parents=True, exist_ok=True)
            
            # Define o caminho completo de destino
            arquivo_destino = diretorio_destino / arquivo_origem.name
            
            # Copia o arquivo para o diretório de destino
            shutil.copy2(arquivo_origem, arquivo_destino)
            print(f"\nDocumento adicionado com sucesso em: {arquivo_destino}")
            return True
            
        except Exception as e:
            print(f"\nErro ao adicionar documento: {str(e)}")
            return False

    def renomear_documento(self, caminho_antigo: str, novo_nome: str) -> bool:
        """
        Renomeia um documento existente.
        """
        try:
            arquivo_antigo = Path(caminho_antigo)
            extensao = arquivo_antigo.suffix
            
            # Cria o novo caminho mantendo a mesma extensão
            novo_arquivo = arquivo_antigo.parent / f"{novo_nome}{extensao}"
            
            # Renomeia o arquivo
            arquivo_antigo.rename(novo_arquivo)
            print(f"\nDocumento renomeado com sucesso para: {novo_arquivo.name}")
            return True
            
        except Exception as e:
            print(f"\nErro ao renomear documento: {str(e)}")
            return False

def exibir_menu():
    """Exibe o menu principal do sistema."""
    print("\n=== Sistema de Gerenciamento de Biblioteca Digital ===")
    print("1. Listar todos os documentos")
    print("2. Adicionar novo documento")
    print("3. Renomear documento")
    print("4. Sair")
    print("=" * 50)

def exibir_documentos(documentos: List[Dict[str, str]]):
    """Exibe a lista de documentos formatada."""
    if not documentos:
        print("\nNenhum documento encontrado!")
        return
    
    print("\nDocumentos encontrados:")
    print("-" * 50)
    for i, doc in enumerate(documentos, 1):
        print(f"{i}. Nome: {doc['nome']}")
        print(f"   Tipo: {doc['tipo']}")
        print(f"   Ano: {doc['ano']}")
        print(f"   Caminho: {doc['caminho']}")
        print("-" * 50)

def main():
    """Função principal que executa a interface do sistema."""
    gerenciador = GerenciadorArquivos()
    
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção (1-4): ").strip()
        
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
            print("\nRenomear documento")
            print("=" * 50)
            documentos = gerenciador.listar_documentos()
            exibir_documentos(documentos)
            
            if documentos:
                try:
                    num_doc = int(input("\nDigite o número do documento a ser renomeado: ").strip())
                    if 1 <= num_doc <= len(documentos):
                        doc = documentos[num_doc - 1]
                        novo_nome = input("Digite o novo nome (sem extensão): ").strip()
                        if novo_nome:
                            gerenciador.renomear_documento(doc['caminho'], novo_nome)
                        else:
                            print("\nNenhum nome fornecido!")
                    else:
                        print("\nNúmero de documento inválido!")
                except ValueError:
                    print("\nPor favor, digite um número válido!")
            
            input("\nPressione Enter para continuar...")
        
        elif opcao == "4":
            print("\nObrigado por usar o Sistema de Gerenciamento de Biblioteca Digital!")
            break
        
        else:
            print("\nOpção inválida! Por favor, escolha 1, 2, 3 ou 4.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()