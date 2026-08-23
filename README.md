# 🤖 Assistente Virtual - Aziz Concept (Challenge Alura Agente)

Projeto desenvolvido como desafio final da fase Tech Builder do programa ONE (Oracle Next Education), em parceria com a Alura. Consiste em um assistente corporativo com RAG (Retrieval-Augmented Generation) baseado em políticas internas da marca.

## 🏛️ Arquitetura da Solução
A aplicação utiliza uma arquitetura baseada em RAG (Geração Aumentada por Recuperação):
1. **Base de Conhecimento:** Um documento em PDF (`regras_loja.pdf`) contendo as políticas oficiais da loja.
2. **Processamento:** O script lê o PDF dinamicamente usando a biblioteca `PyPDF` para extrair as regras de negócio em tempo de execução.
3. **Motor de IA:** O modelo Google Gemini processa a pergunta do usuário juntamente com o conteúdo extraído do PDF para gerar respostas estritamente baseadas nas diretrizes, evitando alucinações.
4. **Interface e Deploy:** Desenvolvido em Streamlit e hospedado em um servidor dedicado na nuvem (Oracle Cloud Infrastructure).

## 🛠️ Tecnologias e Ferramentas Utilizadas
* **Python** (Linguagem principal)
* **Streamlit** (Interface gráfica do chat)
* **Google Gemini API** (Modelo de Inteligência Artificial)
* **PyPDF** (Extração de texto do documento de regras)
* **Oracle Cloud Infrastructure (OCI)** (Ambiente de nuvem para deploy 24/7)

## 🚀 Instruções para Executar o Projeto

1. Clone o repositório do projeto:

    git clone https://github.com/Carolmenali/agente-ecommerce.git
    cd agente-ecommerce

2. Instale as dependências necessárias:
3. 
    pip install streamlit google-generativeai pypdf

4. Configure a sua chave de API:
    Insira a sua chave do Google Gemini no código fonte (app.py).

5. Execute a aplicação:

    streamlit run app.py


## 📋 Exemplos de Perguntas e Respostas do Agente

### Exemplo 1: Dúvida sobre formas de pagamento
* **Cliente:** "Quais as formas de pagamento? Tem desconto se eu pagar à vista?"
* **Assistente:** "Aceitamos cartões de crédito (com parcelamento em até 3x sem juros para todas as peças), cartão de débito e Pix. E temos uma ótima notícia: pagando via Pix, você garante 5% de desconto no valor total da sua compra! Posso te ajudar a escolher alguma peça?"

### Exemplo 2: Regras de Troca
* **Cliente:** "Comprei uma calça, mas ficou apertada. Como faço pra trocar? Eu pago o frete?"
* **Assistente:** "Fique tranquila, o custo do frete da sua primeira troca é por nossa conta! Você tem até 7 dias corridos após o recebimento para solicitar a troca. Só pedimos que a peça esteja com a etiqueta original fixada, sem odores e sem sinais de uso ou lavagem. Deseja que eu passe o contato do nosso suporte humano para iniciar o processo?"

### Exemplo 3: Cuidados com peças delicadas
* **Cliente:** "Posso lavar minha blusa de renda nova na máquina de lavar roupas?"
* **Assistente:** "Para manter a sua peça sempre linda, itens de renda, tricô e tecidos delicados jamais devem ser lavados na máquina ou colocados em secadoras. A lavagem deve ser feita à mão e a secagem sempre à sombra. Assim, sua peça da Aziz Concept vai durar muito mais tempo!"

## 🌐 Evidência do Deploy (Acesso Público)
* **Link público de acesso:** `http://204.216.189.19:8501`
   
