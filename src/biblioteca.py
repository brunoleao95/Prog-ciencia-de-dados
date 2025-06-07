import os
from pathlib import Path
from typing import List, Dict

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
                    documentos.append({
                        'nome': arquivo.name,
                        'caminho': str(arquivo),
                        'tipo': tipo
                    })
        
        return documentos

# Exemplo de uso:
if __name__ == "__main__":
    gerenciador = GerenciadorArquivos()
    documentos = gerenciador.listar_documentos()
    
    print("\nDocumentos encontrados:")
    for doc in documentos:
        print(f"Nome: {doc['nome']}")
        print(f"Tipo: {doc['tipo']}")
        print(f"Caminho: {doc['caminho']}")
        print("-" * 50)