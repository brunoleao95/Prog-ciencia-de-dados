import os
from pathlib import Path
from typing import List, Dict
from datetime import datetime

class GerenciadorArquivos:
    def __init__(self, diretorio_base: str = "data"):
        self.diretorio_base = Path(diretorio_base)
        self.tipos_permitidos = {'.pdf', '.epub', '.txt'}
    
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

def exibir_menu():
    """Exibe o menu principal do sistema."""
    print("\n=== Sistema de Gerenciamento de Biblioteca Digital ===")
    print("1. Listar todos os documentos")
    print("2. Sair")
    print("=" * 50)

def exibir_documentos(documentos: List[Dict[str, str]]):
    """Exibe a lista de documentos formatada."""
    if not documentos:
        print("\nNenhum documento encontrado!")
        return
    
    print("\nDocumentos encontrados:")
    print("-" * 50)
    for doc in documentos:
        print(f"Nome: {doc['nome']}")
        print(f"Tipo: {doc['tipo']}")
        print(f"Ano: {doc['ano']}")
        print(f"Caminho: {doc['caminho']}")
        print("-" * 50)

def main():
    """Função principal que executa a interface do sistema."""
    gerenciador = GerenciadorArquivos()
    
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção (1-2): ").strip()
        
        if opcao == "1":
            documentos = gerenciador.listar_documentos()
            exibir_documentos(documentos)
            input("\nPressione Enter para continuar...")
        
        elif opcao == "2":
            print("\nObrigado por usar o Sistema de Gerenciamento de Biblioteca Digital!")
            break
        
        else:
            print("\nOpção inválida! Por favor, escolha 1 ou 2.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    main()