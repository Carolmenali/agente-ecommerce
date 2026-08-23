# 🤖 Assistente Virtual - Aziz Concept (Challenge Alura Agente)

Projeto desenvolvido como desafio final do curso de Agentes de Inteligência Artificial da Alura (ONE), consistindo em um assistente corporativo com RAG (Retrieval-Augmented Generation) baseado em políticas internas.

## 🛠️ Tecnologias Utilizadas
* Python e Streamlit
* Google Gemini (Modelo `gemini-3.7-flash`)
* PyPDF para leitura do documento de regras
* Oracle Cloud Infrastructure (OCI) para deploy em nuvem

## 📋 Regras da Base de Conhecimento
O agente responde estritamente às diretrizes do documento interno da loja:
* **Política de Trocas:** Prazo de 7 dias corridos, etiqueta original intacta e sem sinais de uso[cite: 1].
* **Fretes e Envios:** Envio via Correios nas modalidades PAC e Sedex[cite: 1].
* **Cuidados Especiais:** Lavagem à mão para peças de tricô, renda e tecidos delicados[cite: 1].
* **Medidas:** Tabela de manequins para tamanhos P, M e G[cite: 1].

## 🌐 Evidência do Deploy
* **Link público de acesso:** `http://204.216.189.19:8501`
