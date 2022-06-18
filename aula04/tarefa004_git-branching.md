### Tarefa 004: Git Branching - 03/06/2021

1. Qual o nome do branch padrão do Git?
    <br /> *master (apesar de estar descrito na documentação como master, por questões historico culturais agora esta adotando o nome *main)
2. O que o comando **<code>git branch nome</code>** realiza?
    <br /> Cria uma nova branch chamada nome
3. Como criar um branch a partir de um commit específico?
   <br /> Primeiro devemos descobri o ID do commit (git log) copiamos esse ID e usamos o comando git checkout -b BRANCH_NAME COMMIT_ID
    <br /> ex: git checkout -b bugfix/234 0cc88e867e90546158c73bd2acc8f981ef11009f
4. Em um repositório, qual o efeito do comando **<code>git checkout -b bugfix/234</code>**?
    <br /> cria uma nova branch chamada bugfix/234 e move o ponteiro para ela
5. Qual o comando para se alternar para um branch de nome **experimento2**?
    <br /> Se a branch existir use o git checkout experimento2. Se a branch não existir usamos git checkout -b experimento2 para criar e mover para ela.
6. Em um repositório com dois branches, **b1** e **b2**, onde b1 é o corrente, qual o efeito do comando **<code>git branch</code>**?
    <br /> Simplesmeste apresenta as branches identificando que b1 é a branch corrente
7. O que o comando **<code>git checkout -b</code>** nome faz?
    <br /> Cria uma nova branch chamada nome e move o ponteiro para ela
8. Qual a função do comando **<code>git branch -d teste</code>**?
    <br /> Considerando que exista uma branch chamada teste, o comanda irá excluir esta branch, desde que tenha feito o push e o merge, para forçar a exclusão podemos utilizar -D (git branch -D teste)
9. Durante o desenvolvimento de um software é comum, por exemplo, utilizar um novo recurso por meio de experimentação. Talvez uma nova tecnologia, uma nova biblioteca que pode ser útil ao que está em desenvolvimento, ou até mesmo uma nova versão de um produto já empregado. Para que o uso deste novo recurso não interfira com o que é considerado pronto, um branch pode ser criado para a experimentação. Código que for criado para a experimentação existirá apenas no branch criado. Se eventualmente o experimento demonstrar um resultado satisfatório, as alterações realizadas no branch poderão ser incorporadas no que é considerado pronto, ou seja, no branch principal (master). Esta última ação é conhecida por merge. Neste item, crie uma sequência de comandos que simula um caso simples de criação e uso seguido de merge empregando um branch para ilustrar uma experimentação conforme acima. A sequência deve incluir, obrigatoriamente: (a) criação de um ou mais branches; (b) chaveamento para pelo menos dois branches e (c) merge.
    <br/> - criar uma branch nova e ir para ela (git checkout -b novaFeature)
    <br/> - editar o(s) arquivo(s) na branch novaFeature()
    <br/> - adicionar o(s) arquivo(s) (git add <arquivo>)
    <br/> - comitar o(s) arquivo(s) (git commit - m "comentário")
    <br/> - volte para branch main (git checkout main)
    <br/> - faça o merge da branch criada para a branch atual (git merge novaFeature)
    <br/> - agora pode excluir a branch criada (git branch -d novaFeature)

</DIV/>
