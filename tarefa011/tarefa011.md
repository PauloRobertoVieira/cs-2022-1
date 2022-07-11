# **Padrões de Codificação**
### Conceito:
- Definir padrões é utilizado para garantir uniformidade na equipe e estabelecer boas práticas.

### Uma descrição de quando, onde e porque utilizá-lo
- Existem diversas “regras” que podem serem estabelecidas, um exemplo muito comum em empresas e equipes, são os comentários no código, existe discussões sobre o assunto, alguns alegam que um código bem produzido dispensa comentários, porém há quem defenda, pois, comentários podem auxiliar na construção da documentação do sistema.

### Exemplo
- Como exemplo de utilização podemos citar a identação, vale ressaltar que linguagens como python a atenção à identação faz uma total diferença, pois, a mesma não utiliza por exemplo {} para definir um escopo de bloco, isso é feito através da identação, ou seja, a identação impactará diretamente na forma de se construir o código.


# **Reflexão**
### Conceito:
- A programação reflexiva é um mecanismo que permite um processo de recursos introspectivos. As APIs de reflexão incorporadas às linguagens de programação são usadas para examinar ou modificar o comportamento de métodos, classes e interfaces em tempo de execução. Você pode usar essa capacidade para aprender sobre a base de código circundante e seu conteúdo.

### Uma descrição de quando, onde e porque utilizá-lo
- A reflexão nos dá informações sobre a classe à qual um objeto pertence e também os métodos dessa classe que podem ser executados usando o objeto. Por meio da reflexão, podemos invocar métodos em tempo de execução, independentemente do especificador de acesso usado com eles.

### Um exemplo de utilização
- Um uso comum para reflexão é durante o teste. A reflexão pode ajudá-lo a simular as aulas, expondo seus comportamentos internos. Um método de classe protegido ou privado normalmente não seria testável; usando reflexão, você pode substituir a restrição de visibilidade para que ela se torne pública em seus testes de unidade.

# **Programação Defensiva**
### Conceitos:
- A programação defensiva é a criação de código para software de computador projetado para evitar questões problemáticas antes que elas surjam e tornar o produto mais estável. A ideia básica por trás dessa abordagem é criar um programa que seja capaz de funcionar adequadamente mesmo em processos imprevistos ou quando entradas inesperadas são feitas por usuários.

### Uma descrição de quando, onde e porque utilizá-lo
- Uma entrada de dados de forma incorreta pode acarretar diversos erros.
Para que seu código possa ser utilizado, existem certos métodos e classes que são públicos, destinados a se comunicarem com o mundo externo, e outros que só precisam ser utilizados internamente. Todos esses métodos e classes públicos são as portas de entrada para seu código, e estão lidando com território desconhecido.
Uma maneira inteligente de garantir que o fluxo esperado dos dados seja seguido é validar qualquer dado que seja enviado pelas fontes externas, criando uma barreira de proteção. Se essa barreira funcionar direitinho, os métodos e classes internas não precisarão fazer outras validações, pois os dados que serão repassados a eles são limpos e confiáveis.

### Um exemplo de utilização.
- Um exemplo bem simples e comum, imagine uma classe que cuida do registro de usuários. Ela possui um método que cadastra um novo usuário na base.
O método CreateUser recebe o nome do usuário, email e cpf. Apesar de várias linguagens serem fortemente tipadas não garantem que um email e um cpf válidos serão passados. Essas duas variáveis precisam ser validadas antes de serem armazenadas.
O método ValidateEmail retorna false caso caso o email tenha formato diferente de ‘algumacoisa@dominio.com’ e o método ValidateCpf retorna false caso o CPF tenha um formato válido (xxx.xxx.xxx-xx).
Esse exemplo é extremamente simples, mas já aplica princípios de programação defensiva. Caso essas validações não fossem feitas nesse momento, elas teriam de ocorrer em outros diversos pontos da aplicação para garantir que os valores estejam sempre corretos.
