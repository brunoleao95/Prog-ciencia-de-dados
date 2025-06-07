# Guia de Contribuição

Este guia explica como contribuir com o projeto usando comandos básicos do Git.


### 1. Commits
Para salvar suas alterações:
```bash
# Ver arquivos modificados
git status

# Adicionar arquivos para commit
git add nome_do_arquivo    # Adiciona um arquivo específico
git add .                  # Adiciona todos os arquivos modificados

# Criar commit
git commit -m "Descrição clara das alterações"
```

### 2. Push
Para enviar suas alterações para o GitHub:
```bash
# Enviar alterações para o GitHub
git push origin main
```

### 3. Pull Requests
Para contribuir com o projeto:

1. Faça um Fork do projeto no GitHub
2. Clone seu fork:
```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

3. Crie uma branch para suas alterações:
```bash
git checkout -b nome-da-sua-branch
```

4. Faça suas alterações, commits e push:
```bash
git add .
git commit -m "Descrição das alterações"
git push origin nome-da-sua-branch
```

5. No GitHub:
   - Vá para seu fork
   - Clique em "Pull Request"
   - Selecione sua branch
   - Descreva suas alterações
   - Envie o Pull Request