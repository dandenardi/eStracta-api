# eStracta-api

### Olá!

Agradeço pela oportunidade em participar do processo seletivo. Esta API foi desenvolvida de acordo com as especificações do documento enviado por e-mail. Destas, creio ser importante destacar:

- Foi utilizada a framework Flask para desenvolvimento de APIs  em conjunto com bibliotecas suplementares.
- O desenvolvimento foi realizado em um ambiente virtual criado com Pipenv. O intuito é garantir que não haja problemas de compatibilidade com outras bibliotecas instaladas.
- Foram desenvolvidas endpoints para funcionalidades de criação, inserção, atualização e remoção (CRUD).
- Optou-se, neste momento, por manter um registro *dummy* de exemplo no próprio código da API (chamado "companies_data"). As funcionalidades implementadas, no entanto, podem ser adaptadas, sem prejuízos, para bancos de dados diversos.
- Ainda seguindo os requisitos, foi utilizada a biblioteca Flask_RESTSX de modo a ter documentação compatível com o padrão Swagger.

## Modo de uso
Conforme mencionado, a API foi desenvovida utilizando um ambiente virtual em Pipenv. Por este motivo é importante seguir os seguintes passos:

- Navegar até a pasta do projeto
- Abrir um terminal
- Executar pipenv shell
- Executar pipenv install (isto instalará os requisitos do projeto)
- Executar python main.py

O servidor estará ativo e acessível no endereço http://localhost:3000/api/v1. Ao navegar para esta endpoint serão apresentados todos os dados contidos na base de dados. As demais rotas são detalhadas a seguir.

## CRUD


### Criação (Create)
É possível criar um registro de empresa através da endpoint '127.0.0.1:3000/api/v1/' utilizando o método POST. É preciso incluir no corpo da requisição os dados na seguinte estrutura:

    {
        "CNPJ": "74122759400991",
        "nome_razao": "Exemplo",
        "nome_fantasia": "Exemplo Fantasia",
        "CNAE": ["12344", "44553"]
    }

Os retornos serão:
    200 - em caso de sucesso
    500 - em caso de falha

### Leitura (Read)

Existe a possibilidade de ver todas as empresas cadastradas através de uma requisição GET para o endpoint 127.0.0.1:3000/api/v1/. Neste caso todas as empresas são listadas por CNPJ e em ordem crescente. 

Ainda é possível obter uma listagem ordenada com paginação definida (padrão 25), categorizadas por quaisquer das colunas/campos e em ordem crescente (padrão) ou decrescente. Para tanto, deve ser utilizada a endpoint /companies seguida dos atributos, conforme exemplo:

    127.0.0.1:3000/api/v1/companies?start=0&limit=25&sort=CNPJ&dir=asc

Os retornos serão:
    200 - lista dos registros, em caso de sucesso
    500 - em caso de falha

Uma terceira possibilidade é obter informações sobre uma empresa em particular, com base no CNPJ, conforme exemplo:
    127.0.0.1:3000/api/v1/company/02653350513779

Os retornos possíveis serão:
    200 - o registro da empresa, em caso de sucesso
    404 - seguido da mensagem: *Company with ID <built-in function id> does not exist. You have requested this URI [/api/v1/company/0265335051377] but did you mean /api/v1/company/<string:cnpj> or /api/v1/companies ?* - em caso de empresa inexistente
    500 - Em caso de falha

### Atualização (Update)

É possível atualizar os dados de uma empresa com base em seu CNPJ. Apenas os campos nome fantasia e CNAE podem ser alterados. Isso é feito através de uma requisição do tipo PUT para o endpoint 127.0.0.1:3000/api/v1/company/<cnpj> seguida dos novos dados, conforme exemplo:

    {
        "nome_fantasia": "Exemplo Fantasia 2",
        "CNAE": ["12344", "1111111"]
    }

Os retornos possíveis são:
    200 - o registro atualizado, em caso de sucesso
    500 - em caso de falha

### Remoção (Delete)

Por fim, é possível remover o registro de uma empresa realizando uma requisição do tipo DELETE utilizando o CNPJ.

Os retornos possíveis são:
    200 - Ok, em caso de sucesso
    404 - Em caso de CNPJ invádilo
    500 - Em caso de falha


## O que está por vir:

Esta é apenas a versão inicial. O planejamento para futuras versões inclui tratamento de erros em particular, com mensagens personalizadas e amigáveis (i.e. quando o usuário insere dados inválidos). Também está no planejamento a inclusão de validação ao chegar a requisição, uma forma de complementar o procedimento quando os dados chegam do frontend.

Agradeço novamente e fico à disposição!