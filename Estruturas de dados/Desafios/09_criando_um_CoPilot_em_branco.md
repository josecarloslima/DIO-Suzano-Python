# Criando um CoPilot em branco
- Criar um Agente em branco
- Customizar um tópico
- Personalizar uma mensagem de erro de tópico
- Aumentar/diminuir a qualidade da resposta com GenAI

## Links Úteis
https://learn.microsoft.com/pt-br/miscrosoft-copilot-studio
https://romaos.com.br/learn

## 1. Criando um Agente em branco

**Passo a passo:**
1. Acesse: https://copilotstudio.microsoft.com
2. Dentro do ambiente acesse: **+ new agent**
3. Defina a linguagem: Português (Brasil)
4. Defina um nome para seu agente
5. Você pode inserir um ícone
6. Na descrição coloque o que o ChatBot irá fazer, sua função (seja conciso e direto)
7. Defina as instruções. Aqui entra a *engenharia de prompt* para você definir tom, temperatura, linguagem, qual o passo a passo do Agente.
8. Conhecimento: adiciona bases de conhecimento.
9. A partir daqui você pode:
	1. criar, usando o botão **CREATE** 
	2. ou usar as configurações avançadas.
		1. Aqui posso configurar aonde eu armazeno as informações do ChatBot, por padrão elas não são armazenadas;
		2. Posso mandar o Agente para um solução para que eu consiga exportar as informações e jogar para outro ambiente.

**Exemplo:**
1. https://copilotstudio.microsoft.com
2. **+ new agent**
3. Linguagem: Português (Brasil)
4. Nome: Agente da DIO
5. Ícone: não usado
6. Descrição: Agente responsável por buscar conteúdos de CoPilot Studio dentro da documentação oficial da Microsoft, sendo que toda resposta dele será como o "Agente da DIO".
7. Instruções: Você é o Agente chamado "Agente da DIO" e vai agir em tom formal, com o idioma em português, para retornar informações relevantes da documentação oficial da Microsoft, o Microsoft Learn. Ao retornar uma resposta para o usuário você deve considerar: - buscar a melhor resposta na documentação; - retornar a resposta apropriada e amigável em tom formal; -retomar uma ou mais citações da documentação.
8. Conhecimento: não usado
9. CREATE.

## 2. Customizar um tópico

**Passo a passo:**
1. Acesse: https://copilotstudio.microsoft.com
2. Dentro do ambiente acesse: **Topics**, no menu superior
3. Dentro de **Topics** clique em **+ Add topic**
	1. Este tópico pode ser em branco
	2. Ou ter como base uma descrição do CoPilot
4. Adicionando um tópico em branco podemos editar/customizar a **frase gatilho**
5. Clique no símbolo de **+** para adicionar uma ação (conectada à frase gatilho)
6. Siga até a parte **avançada** e clique em **generative answers**, para adicionar respostas generativas.
7. Na nova ação clique em **input**
8. Siga para **system** e coloque na caixa de pesquisa: **Activity.Text**
9. Adicione uma nova ação, agora uma **Mensagem**
10. Nomeie este novo tópico
11. Clique em **salvar**, ele está criado.

**Exemplo:**
1. https://copilotstudio.microsoft.com
2. **Topics**
3. **+ Add topic** 
4. **Editar** frase gatilho: buscar informações do AI builder; o que é AI builder; onde encontro informações da ferramenta de AI da Power Plataform
5. Adicionar ação **conversa generativa**
6. Adicione **Activity.Text** no **Input** da **conversa generativa**
7. Adicione uma nova ação, **mensagem**: Tópico AI builder encerrado!
8. Nome do topico: Ai Builder Topic
9. Salvar

## 3. Personalizar uma mensagem de erro de tópico

**Passo a passo:**
1. Acesse: https://copilotstudio.microsoft.com
2. Dentro do ambiente acesse: **Topics**, no menu superior
3. Dentro de **Topics** você tem duas escolhas:
	1. **Conversational boosting** (tópico) - tratamento de erro
	2. **Fallback** (tópico) - lida com todo tipo de erro usando GenAI
4. Para personalizar vamos usar **Conversational boosting**
5. Nele adicione uma ação abaixo de **All other condition**, uma **mensagem**
6. A mensagem pode contar várias formas de lidar com o usuário como usar o nome dele, além disso pode-se criar um outro fluxo para lidar com o erro trabalhando em conjunto com SAC ou até bases de erros.
7. Salve

**Exemplo:**
1. https://copilotstudio.microsoft.com
2. **Topics**
3. **Conversation boosting**
4. **all other condition**
5. **message**: Desculpe mas não foi possível encontrar a resposta que você estava esperando, entre em contato com 000 000 ou contato@dio
6. Salvar

## 4. Aumentar/Diminuir a qualidade da resposta com GenAI

**Passo a passo:**
1. Acesse: https://copilotstudio.microsoft.com
2. Dentro do ambiente acesse: **Topics**, no menu superior
3. Dentro de **Topics** você entra em **Conversational boosting** (tópico)
4. Dentro da ação **Create generative answer** vá até **Data source** e permita que a IA use sua própria base de conhecimento para gerar uma resposta.
5. Vale lembrar que esta base é o GPT então ele pode mudar de assuntos ou usar informações obsoletas já que ele tem um limite de tempo ao qual foi usado para treino.
6. Ainda em **Data source** você pode customizar seu prompt e usar a pergunta do usuário, como uma variável, por exemplo, para a consulta da GenAI
7. Você também pode customizar o nível de temperatura na busca de seus documentos. Quanto mais alto, mais quente, maior a procura dele por documentos com as classificações mais altas (altamente objetivo). Quanto mais baixo ele retornará como referência documentos de qualquer classificação, entendendo que as vezes buscamos coisas que são parcamente relacionadas (altamente criativo).
8. Por fim podemos ir nas **configurações** do **Agente**
9. Acessar a seção **IA generativa**
10. E ali habilitar o **generativo geral** que também nos possibilita definir se ele tenderá ao objetivo, criativo ou balanceado
