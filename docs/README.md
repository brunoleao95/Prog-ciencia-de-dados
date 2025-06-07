#Listar Documentos

Descrição: Exibe todos os documentos digitais cadastrados no sistema, organizados por categoria (Artigos, Livros, Documentos).Informações exibidas para cada documento:

-Nome do arquivo
-Tipo de arquivo (.pdf, .epub, .txt)
-Categoria (Artigos, Livros, Documentos)
-Tamanho do arquivo (em bytes, KB ou MB)
-Data de criação
-Data da última modificação
-Status do arquivo (Acessível ou Não encontrado)
-Caminho relativo do arquivo na estrutura de pastas

#Adicionar Novo Documento

Descrição: Permite ao usuário adicionar um novo documento ao sistema, copiando o arquivo para a pasta correspondente de acordo com seu tipo. Regras:

-Aceita apenas arquivos com extensões permitidas (.pdf, .epub, .txt)
-O arquivo é copiado para a subpasta correta (artigos/pdf, livros/epub, documentos/txt)
-Exibe mensagem de sucesso ou erro

#Renomear Documento

Descrição: Permite ao usuário renomear um documento já cadastrado, mantendo a extensão original. Regras:

-O usuário seleciona o documento pelo número na lista
-O novo nome não deve conter extensão
-O sistema valida a entrada e exibe mensagens de sucesso ou erro

#Remover Documento

Descrição: Permite ao usuário remover um documento do sistema, excluindo o arquivo do disco. Regras:

-O usuário seleciona o documento pelo número na lista
-O sistema solicita confirmação antes de remover
-Exibe mensagens de sucesso, erro ou cancelamento

#Sair

Descrição: Encerra o sistema de forma segura, exibindo uma mensagem de despedida.

#Organização dos Arquivos

Descrição: Os arquivos são organizados automaticamente em subpastas dentro do diretório data/:

-data/artigos/pdf/ para arquivos PDF
-data/livros/epub/ para arquivos ePUB
-data/documentos/txt/ para arquivos TXT

#Validação e Tratamento de Erros

Descrição: O sistema realiza validações e trata erros em todas as operações:

-Verifica tipos de arquivos permitidos ao adicionar
-Válida entradas do usuário (números, nomes)
-Exibe mensagens claras de erro, sucesso ou cancelamento
-Solicita confirmação para operações destrutivas (remoção)
