### Tarefa 003: Git Exercícios - 03/06/2021.

Responda as questões abaixo (exercite os comandos do git correspondentes). Lembre-se de que o “interessante” não é exatamente o conjunto de respostas, mas o processo de obtê-las e a experiência obtida com a execução dos comandos.

1. Qual o comando para obter a versão instalada do Git?
  <br/># git --version

2. Qual o efeito da execução de cada um dos comandos abaixo?
  - a. git help
    <br/># Irá exibir o manual de ajuda do git, normalmente é utilizado com algum comando.
  - b. git help checkout
    <br/># Apresenta o manual de ajuda do comando git checkout e as possibilidades que podemos utilizar neste comando
  - c. git help merge
    <br/># Apresenta o manual de ajuda do comando git merge, explicações de seu uso e as possibilidades
  - d. git init
    <br/># Cria um repositório vazio ou reinicializa um existente
  - e. git add --all
    <br/># Adiciona todos os arquivos (modificados, alterados e removidos) na área de preparação (staging area) e os deixa preparado para o commit e indica ao git que esses arquivos serão rastreados.
  - f. git add -u
    <br/># Atualize o índice exatamente onde ele já possui uma entrada correspondente a <pathspec>. Isso remove e modifica as entradas de índice para corresponder à árvore de trabalho, mas não adiciona novos arquivos.
  - g. git config -l
    <br/># Liste todas as variáveis definidas no arquivo de configuração, juntamente com seus valores.
  - h. git mv a.txt b.txt
    <br/># Renomeia o arquivo a.txt para b.txt (Mova ou renomeie um arquivo, diretório ou link simbólico.)
  - i. git reset --hard
    <br/># O git reset opera nas "três árvores do Git". Essas árvores são o Histórico de commits (HEAD), o Índice de staging e o Diretório de trabalho.
  - j. git log -27
    <br/># Especifica o numero de linha absoluto (Mostra logs de commit)
    
3. O fluxo “clássico” de interação com o Git é algo como “alterar um ou mais arquivos”, “acrescentar essas mudanças para serem contemplados no próximo commit” e, finalmente, executar um “commit”. Quais os comandos necessários para realizar os dois últimos “passos” desse fluxo?
  <br/># git add nomeDoArquivo.ExtensaoDoArquivo (adicionar um por um) ou git add --all (adiciona todos simultaneamente deixando os arquivos prontos para serem comitados)
  <br/># git commit -m "faça um comentários explicando o que foi feito"

4. Qual o comando deve ser executado para identificar o que foi alterado desde o último “commit”?
  <br/># git status

5. Em um dado repositório, arquivos simplesmente copiados para lá, ou seja, _untracked_, podem ser exibidos/identificados com que comando?
  <br/># git status -u

6. Qual o comando para efetuar um _commit_?
  <br/># git commit -m "Inserir um comentário explicando o que foi feito"

7. Qual o comando que devemos empregar para descartar mudanças ocorridas no arquivo teste.txt, por exemplo?
  <br/># git revert numeroDaHashAnterior
  <br/># git revert 39edd9d4e3e91ca6ca0620f40c1a2e8d4a6230a8

8. O que deve ser feito para que um determinado diretório do seu repositório seja ignorado pelo Git? Faça uma busca por **.gitignore**.
<br/># Criar o arquivo .gitignore
<br/># Adicionar a pasta no arquivo
<br/>ex: .Exercicios/

9. O que acontece se o seu repositório local for acidentalmente removido?
<br/># Todos os arquivos serão perdidos, considerando que foram efetuados os commites isso pode ser revertido utilizando o repositório remoto.

10. Como clonar um repositório remoto?
<br/># Acessar o repositório remoto, clicar em code e depois em SSH, copiar endereço
<br/># Ir para o diretório onde será feito o clone e utlizar seguinte comando
<br/># git clone enderecoSSHcopiado (git clone git@github.com:PauloRobertoVieira/cs-2022-1.git)

11. Em alguns cenários **git log** pode produzir extensos resultados. Se houver interesse em visualizar o histórico de um repositório, onde cada mudança é fornecida exatamente em uma única linha, qual o comando que deve ser empregado?
<br/># git log --oneline

12. Em qual arquivo o Git armazena informações de configuração empregadas por usuário?
<br/># ~/.gitconfig ou ~/.config/git/config

13. Qual o comando para criar um repositório local?
<br/># git init

14. Qual o nome do diretório criado pelo Git quando se executa o comando **git init**?
<br/># .git

15. Qual o comando para adicionar todos os arquivos modificados? (Aqueles para os quais **git status** identificam como **modified**?)
<br/># git add .

16. O Git faz uso do valor de hash conhecido por SHA1. O que isto significa? Qual o propósito? O que é SHA1?
<br/># A sigla "SHA'' significa secure hash algorithm (algoritmo de hash seguro). O SHA1 embaralha determinado arquivo, imagem ou texto para que seja gerado um conjunto de caracteres identificadores, caracteres esses que possuem 40 dígitos. Esses quarenta dígitos são sempre únicos. Se você pegar um texto enorme e passar ele por esse algoritmo, ele vai gerar esse conjunto de caracteres, se você alterar uma vírgula que seja desse texto, já será gerado outro conjunto.
<br/># Em criptografia, SHA-1 é uma função de dispersão criptográfica (ou função hash criptográfica) projetada pela Agência de Segurança Nacional dos Estados Unidos. Os hashes são utilizados para validar a integridade de um conteúdo digital, sendo eles parte de qualquer certificado digital.

17. Qual a palavra para indicar o último _commit_ em vez do valor de hash SHA1 correspondente?
<br/># Podemos utilizar git log -1 (mostrará último commit) ou utilizar uma formatação:
<br/># git log --pretty=format: %an

18. Quando se cria dois arquivos usando um editor de texto qualquer e, na sequência, executamos o comando **git add -u**, os dois arquivos criados passam de _untracked_ para _new file_?
<br/># Não, isso funcionaria somente se os arquivos já estivessem sendo rastreado, como são arquivos novos, o git simplesmente só atualiza o índice sem adicionar esses novos arquivos.

19. Qual o efeito da execução dos dois comandos abaixo, nesta ordem, em um dado repositório?
**git reset --soft HEAD~1**
**git reset --hard**
<br/># Ao usar git reset --soft HEAD~1, iremos remover o último commit da ramificação atual.
<br/># Redefine o índice e a árvore de trabalho. Quaisquer alterações nos arquivos rastreados na árvore de trabalho desde <commit> são descartadas. Quaisquer arquivos ou diretórios não rastreados na maneira de gravar qualquer arquivo rastreado são simplesmente excluídos.

20. Após o emprego de um ambiente integrado de desenvolvimento (IDE), é comum a criação de arquivos e diretórios. Qual o comando que podemos empregar para remover arquivos e diretórios _untracked_?
<br/># git clean -fxd

21. Qual o nome do arquivo no qual podemos inserir a indicação para o Git de arquivos e diretórios a serem ignorados?
<br/># .gitignore
22. Quando se cria o arquivo _MinhaClasse.class_ em um dado diretório e desejamos que arquivos com a extensão .class, como neste caso, sejam ignorados por todos os membros de uma equipe que estão contribuindo com um dado projeto, como devemos proceder?
<br/># Caso não exista, devemos criar o arquivo .gitignore
<br/># Incluir nele todas extensões que devem ser ignoradas pelo git, neste caso *.class

23. jQuery é uma famosa biblioteca em JavaScript. Consulte detalhes em [jQuery](http://jquery.com). O repositório correspondente encontra-se em [gitRep](https://github.com/jquery/jquery.git). Faça o clone deste repositório.
<br/># git clone git@github.com:jquery/jquery.git

24. No repositório **jqueryrepo**, criado no passo anterior, qual o efeito do comando
**git shortlog -sne**?
<br/># Apresenta a quantidade de contribuição (commit) o nome e o e-mail da pessoa.

25. No repositório **jqueryrepo**, qual o efeito de **git remote -v**?
<br/># Retorna um estagio e fica aguardando para commit
<br/># Git também sugere limpeza de cache (git rm --cached jquery)

26. Um repositório Git pode ser etiquetado ao longo do tempo. Ou seja, _commits_ específicos podem ser “marcados” ou “etiquetados” para facilitar referências posteriores. Para listar todas as “etiquetas” (_tags_) estabelecidas para um dado repositório, qual comando deve ser executado?
<br/># git tag

27. Caso um dado repositório retorne muitas “marcas” ou “etiquetas” para o comando **git tag**, como retornar apenas aquelas que atendem a determinado padrão, por exemplo, iniciadas por 2.0?
<br/># git tag -l "2.0"

28. Qual o efeito do comando **git tag -a 3.4-gold -m “minha versão ouro”**?
<br/># fatal: too many arguments
<br/># Se fizermos git tag -a 3.4-gold e depois escrevermos "minha versão ouro" e fechar o arquivo, o sistema irá criar uma tag 3.4-gold

29. Após executado o comando acima, qual o efeito de **git show 3.4-gold**?
<br/># Apresenta tag 3.4-gold
<br/># Apresenta também o comentário e outras informações do commit (Tagger, Date, Hash, Author)

30. O que o comando **git push origin 3.4-gold** teria como efeito?
<br/># enviaria do branch local para o remoto com a tag 3.4-gold

31. Após executar um commit, qual o efeito de **git commit --amend**?
<br/># Permite modificar o commit mais recente

32. Após executar **git add x.txt**, qual o efeito de **git reset HEAD x.txt**?
<br/># Retorna uma condição, ou seja, o arquivo não poderá ser comitado, devemos fazer novamente git add xt.txt

33. Após alterar o conteúdo de um arquivo committed em passo anterior, qual o efeito do comando **git checkout -- a.txt**?
<br/># Não ocorre nenhuma alteração, arquivo foi comitado

34. Qual a diferença entre os comandos **git reset HEAD a.txt** e **git checkout -- a.txt**?
<br/># Retorna uma condição, tira o arquivo a.txt do Stage
<br/># Descarta as alterações efetuadas no arquivo.

35. Veja como interpretar o resultado de git diff [aqui](https://medium.com/therobinkim/how-to-read-a-git-diff-6c87a9dc47c5). Execute, em um dos seus projetos, o comando **git diff HEAD~1 HEAD** e certifique-se de que entende o resultado apresentado.
<br/># Git diff apresenta as mudanças/alterações antes de fazermos o commit
<br/># Git diff HEAD~1 HEAD compara as versões antes do último commit e o último commit

</DIV/>
