### Semana 1 - Dia 25/05/2022 - Aulas 001a004 - Atividade Supervisionada

1. Elaborar uma pesquisa sobre o tema "_Rest API_".
2. Elaborar um texto de pelo menos uma página, descrito com suas próprias palavras, destacando:

- As definições dos conceitos envolvidos;
- As principais características deste conceito (pelo menos umas cinco).

- O acrônimo API é a abreviação de Application Programming Interface, que significa “Interface de Programação de Aplicações”. Representa um conjunto de rotinas e padrões estabelecidos e documentados para que uma determinada aplicação de software tenha autorização para utilizar as funcionalidades oferecidas por essa aplicação, sem precisar conhecer as anuências dessa implementação.
- Isso garante segurança de código e, principalmente, das regras de negócio do software e a interoperabilidade entre aplicações, em que essa comunicação ocorra utilizando as requisições HTTP responsáveis pelas operações de manipulação de dados.
  API REST é uma abstração de arquitetura de software que fornece dados em um formato padronizado para modelos de requisições HTTP.
- A arquitetura REST possui um conjunto de regras e princípios que devem ser seguidos. Vamos conhecê-los:
  Cliente-Servidor: Trata a respeito da separação de responsabilidades, ou seja, separar as preocupações de interface do usuário (User Interface) do banco de dados, abstraindo a dependência entre os lados clientes/servidor e permitindo a evolução desses componentes sem impacto e quebra de contrato.
- Interface Uniforme: É a interoperabilidade entre os componentes cliente e servidor. Como o cliente e servidor compartilham da mesma interface, é necessário estabelecer um contrato para a comunicação entre essas partes. Para isso, há quatro princípios a serem seguidos: 1) Identificação dos recursos (por exemplo,Swagger); 2) Representação dos recursos; 3) Mensagens auto-descritivas; 4) Componente HATEOAS.
- Stateless: Cada requisição acionada entre a comunicação cliente-servidor deve possuir toda a informação necessária e compreensível para realizar a origem da requisição, não sendo de responsabilidade do servidor armazenar qualquer tipo de contexto. Isso pode gerar alto tráfego de dados e impacto na performance da aplicação, porém pode-se utilizar recursos de cache nesses casos.
- Cache: É utilizado para melhorar a performance de comunicação entre aplicações, otimizando o tempo de resposta na comunicação entre cliente-servidor. É de responsabilidade do servidor controlar as diretivas de cache através do cabeçalho HTTP (HTTP Header).
- Camadas: A separação de responsabilidades é importante nesse modelo de arquitetura. Os princípios e as boas práticas na arquitetura e design de um projeto, sugerem a construção de camadas independentes e auto gerenciadas, em que cada camada não pode conhecer as demais camadas. Caso ocorra mudanças em uma delas, as demais não serão impactadas. Nesse modelo, o cliente não deve conectar-se diretamente ao servidor da aplicação, porém uma camada de balanceamento de carga deverá ser acionada para essa responsabilidade.
- REST é acrônimo de (REpresentational State Transfer) é uma possibilidade para a criação de web services, cujas principais diferenças em relação ao modelo tradicional (SOAP) estão na utilização semântica dos métodos HTTP o mais utilizados são(GET, POST, PUT e DELETE), outro fator de destaque é a leveza dos pacotes de dados transmitidos na rede e também a simplicidade, não sendo necessário camadas intermediárias.
- No REST, uma requisição HTTP é equivalente a uma chamada de um método (operação) em um objeto (recurso) residente no servidor.
- Em uma requisição HTTP, as mensagens possuem as seguintes partes:
  - 1.O Verbo identifica qual é o tipo de requisição que está sendo enviada, podendo ser GET, PUT, etc.;
  - 2.A URI (Uniform Resource Identifier) especifica o endereço do recurso que se deseja acessar no servidor;
  - 3.Versão HTTP indica qual a versão do protocolo;
  - 4.O cabeçalho da requisição especifica os metadados da requisição no formato de pares chave-valor, por exemplo: tipo de cliente ou navegador, formatos suportados pelo cliente, formato do corpo da mensagem, configurações de cache, etc.
  - 5.O corpo da requisição é o conteúdo da mensagem ou a representação de um recurso.
- Já as mensagens de resposta HTTP possuem as seguintes partes:
  - 1.O código de resposta indica o estado do servidor para o recurso solicitado, por exemplo: 404 significa recurso não encontrado e 200 significa sucesso;
  - 2.Versão HTTP indica qual a versão do protocolo;
  - 3.O cabeçalho da resposta especifica os metadados a respeito da mensagem de resposta no formato de pares chave-valor, por exemplo: tamanho do conteúdo, tipo do conteúdo, data, tipo do servidor, etc.;
  - 4.O corpo da requisição é o conteúdo da mensagem de resposta ou a representação do recurso solicitado.
- Os cabeçalhos e parâmetros de solicitação também são importantes em chamadas de API REST, porque incluem informações importantes do identificador como metadados, autorizações, identificadores de recursos uniformes (URIs), armazenamento em cache, cookies e mais. Cabeçalhos de solicitação e cabeçalhos de resposta, juntamente aos códigos de status HTTP convencionais, são usados dentro de APIs de REST bem projetadas.

- Como principais características de uma requisição REST, podemos destacar:
- O método HTTP é utilizado para determinar a operação a ser realizada em um determinado recurso. Em geral, utiliza-se o GET para recuperar, POST para criar, PUT para alterar e DELETE para apagar;
- O recurso, por sua vez, é indicado na URL da requisição;
  Parâmetros podem ser passados na própria URL e/ou no corpo na requisição;
- Os tipos de dados utilizados na requisição e na resposta devem ser acordados entre o servidor e o(s) cliente(s). JSON e XML estão entre os tipos mais utilizados.
- Além dos famosos GET e POST, o protocolo HTTP define os métodos: CONNECT, HEAD, PUT, DELETE, TRACE e OPTIONS. Ainda é possível criar extensões e consequentemente a adição de novos métodos. A especificação RFC 5789 define o método PATCH, por exemplo.
- Existe certa divergência em relação à função dos métodos HTTP POST e PUT no contexto de serviços REST. Alguns autores defendem o uso do POST para criação e PUT para atualização, já outros pensam o inverso. Temos também o PATCH, que tem o propósito de servir para atualizações parciais de um objeto. Em todo o caso, na prática, o provedor do serviço é quem irá decidir qual abordagem utilizar.

- COUTINHO, Paulo César. REST Tutorial. 2013. Disponível em: https://www.devmedia.com.br/rest-tutorial/28912. Acesso em: 27 maio 2022.
