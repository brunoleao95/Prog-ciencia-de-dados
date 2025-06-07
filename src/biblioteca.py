import os
from pathlib import Path
from typing import List, Dict

class GerenciadorArquivos:
    def __init__(self, diretorio_base: str = "data"):

        self.diretorio_base = Path(diretorio_base)
        self.tipos_permitidos = {'.pdf'}
    
    def listar_pdfs(self, subdiretorio: str = None) -> List[Dict[str, str]]:

        # Constrói o caminho completo
        if subdiretorio:
            diretorio = self.diretorio_base / subdiretorio
        else:
            diretorio = self.diretorio_base
        
        # Verifica se o diretório existe
        if not diretorio.exists():
            return []
        
        # Lista os PDFs
        pdfs = []
        for arquivo in diretorio.glob('**/*.pdf'):
            if arquivo.is_file():  # Garante que é um arquivo, não um diretório
                pdfs.append({
                    'nome': arquivo.name,
                    'caminho': str(arquivo)
                })
        
        return pdfs

# Exemplo de uso:
if __name__ == "__main__":
    # Cria uma instância do gerenciador
    gerenciador = GerenciadorArquivos()
    
    # Lista todos os PDFs na pasta de artigos
    pdfs = gerenciador.listar_pdfs('artigos/pdf')
    
    # Mostra os resultados
    print("\nPDFs encontrados:")
    for pdf in pdfs:
        print(f"Nome: {pdf['nome']}")
        print(f"Caminho: {pdf['caminho']}")
        print("-" * 50)