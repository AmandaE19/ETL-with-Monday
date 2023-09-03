# <font color="#C71585">**Desafio de Projeto ETL**</font>

Nesse desafio foi solicitado a criação de um projeto capaz de executar as etapas de um ETL (Extract, Transform, Load)

*******
# <font color="#C71585">**Sumario**</font>
 - [Descrição do projeto](#project_description)
 - [Benefícios do Projeto](#benefits)
 - [Como rodar esse projeto localmente](#initializingapp)
*******

<div id="project_description></div>

#<font color="#C71585">Descrição do projeto</font> 

**Título do Projeto:** Gerador de Mensagens de Cobrança

**Descrição do Projeto:** O projeto que desenvolvido é um Gerador de Mensagens de Cobrança personalizadas. Ele automatiza o processo de criação de mensagens de cobrança para clientes, economizando tempo e garantindo uma abordagem mais personalizada.

**Funcionalidades Principais:**

* **Integração com o Monday.com:** O sistema se conecta diretamente ao Monday.com, uma plataforma de gestão de projetos e tarefas, para coletar informações relevantes sobre os clientes e suas dívidas. Esses dados foram definidos nesse projeto como o nome do cliente, o valor da dívida e a referência da dívida.

![Print Exemplificando Estrutura Monday]([image.png](https://github.com/AmandaE19/ETL-with-Monday/blob/main/src/images/image.png?raw=true))

* **Geração de Mensagens Personalizadas:** Uma vez que os dados são coletados do Monday.com, o sistema utiliza a poderosa tecnologia da OpenAI para criar mensagens de cobrança personalizadas. Isso garante que cada cliente receba uma mensagem adaptada à sua situação específica, melhorando as chances de obter uma resposta positiva.

* **Armazenamento em CSV**: Todas as informações relevantes, incluindo o nome do cliente, o valor da dívida, a referência da dívida e a mensagem de cobrança gerada, são cuidadosamente registradas e armazenadas em um arquivo CSV. Isso permite que o usuário mantenha um histórico organizado de todas as interações com os clientes e rastreie o progresso das cobranças ao longo do tempo. Essa versão ainda não irá juntar as mensagens geradas em diferentes momentos, a cada vez que o projeto for inicializado um novo CSV será gerado, e de acordo com os dados no Monday poderá ou não repetir clientes, para evitar que mensagens para clientes sejam feitas mais de uma vez, basta acessar a plataforma Monday.com e alterar manualmente o status dos cliente que já possuem mensagem para "Feito". Clientes com status "Pendente" terão as mensagens criadas no script.

![Print Mostrando CSV Final]([image_csv.png](https://github.com/AmandaE19/ETL-with-Monday/blob/main/src/images/image_csv.png?raw=true)

<div id="benefits"></div>

#<font color="#C71585">Benefícios do Projeto</font>

**Economia de Tempo:** Elimina a necessidade de criar manualmente mensagens de cobrança, economizando um tempo valioso que pode ser direcionado para outras tarefas importantes.

**Personalização:** As mensagens geradas são altamente personalizadas, aumentando a probabilidade de uma resposta positiva dos clientes.

**Registro Organizado:** O armazenamento em CSV oferece uma maneira organizada de manter um registro completo de todas as transações e interações com os clientes.

**Eficiência:** Automatiza tarefas repetitivas, garantindo uma abordagem consistente e eficiente na cobrança de dívidas.

<div id="initializingapp></div>

#<font color="#C71585">Como rodar locamente esse projeto</font>

Será necessário uma conta na Monday.com em modo desenvolvedor, que tenha acesso as chaves necessárias e uma conta na OpenAI com crédito para que as mensagens possam ser geradas. Para conseguir a apiKey da OpenAI [clique aqui](https://platform.openai.com/account/api-keys) e para conseguir o token de acesso Monday.com no perfil da sua conta (canto superior direito), clique em "developers" depois em "Meus tokens de acesso", caso já possua um token basta clicar em mostrar, se não crie um token.
* Passo 1: Faça um clone desse repositório
```git clone https://github.com/AmandaE19/ETL-with-Monday.git```

* Passo 2: Crie um arquivo .env na pasta src desse projeto e insira as seguintes informações
```
API_KEY=SUA-CHAVE-DE-API-OPENAI
ACCESS_TOKEN=SEU-TOKEN-DE-ACESSO-MONDAY
ID_BOARD=ID-DO-BOARD-QUE-IRÁ-EXTRAIR-AS-INFOS
```

* Passo 3: Instale o pacote necessário. Em um terminal na raiz do projeto use o comando ```pip install openai```

* Passo 4: Com tudo configurado, basta rodar.
