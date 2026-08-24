Markdown
# 🛍️ BimBam Buy — Assistente Inteligente de Atendimento ao Cliente

Projeto desenvolvido para o **Challenge de Inteligência Artificial / Oracle Next Education (ONE)** em parceria com a **Alura**.

---

## 🌐 Demonstração Online

Acesse a aplicação em produção no Streamlit Community Cloud:  
👉 **[https://challenge-alura-agente-uftsjfjqsmp8pf3exnq9d4.streamlit.app/](https://challenge-alura-agente-uftsjfjqsmp8pf3exnq9d4.streamlit.app/)**

---

## 📌 Descrição Geral do Projeto

O assistente foi projetado para atuar como o canal oficial de atendimento e suporte ao cliente da loja virtual fictícia **BimBam Buy**. 

Utilizando a arquitetura **RAG (Retrieval-Augmented Generation)**, o agente responde exclusivamente com base nas políticas oficiais contidas na documentação interna da empresa, eliminando alucinações e fornecendo respostas precisas sobre prazos de entrega, políticas de devolução, formas de pagamento, garantias e programas de afiliados.

---

## 🏗️ Arquitetura da Solução

A arquitetura do sistema segue um pipeline RAG contextual estruturado:

1. **Ingestão e Extração de Documentos:** A base de conhecimento em PDF (`data/BimBam_Buy_Documentacao_Completa.pdf`) é processada e extraída usando a biblioteca `pypdf`, armazenada em memória com cache otimizado via Streamlit.
2. **Engenharia de Prompt e Contexto:** A consulta do usuário é combinada com as regras de atendimento e os trechos da documentação oficial em um prompt estruturado.
3. **Processamento com LLM:** A requisição é processada pela API do **Google Gemini** (`models/gemini-3.6-flash`), garantindo raciocínio rápido e aderência estrita às políticas.
4. **Interface Conversacional (UI):** O cliente interage por meio de uma interface de chat reativa construída com **Streamlit**.
5. **Segurança de Credenciais:** As chaves de API são gerenciadas através do `st.secrets`, impedindo vazamentos em repositórios públicos.

---

## 🛠️ Tecnologias e Ferramentas

* **Linguagem:** Python 3.10+
* **LLM / Inteligência Artificial:** Google Gemini API (`gemini-3.6-flash` via `google-generativeai`)
* **Interface Web:** Streamlit
* **Processamento de Documentos:** PyPDF
* **Conteinerização:** Docker
* **Controle de Versão:** Git e GitHub
* **Nuvem e Deploy:** Oracle Cloud Infrastructure (OCI) / Streamlit Community Cloud

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
* Python 3.10 ou superior instalado.
* Chave de API do Google AI Studio (Gemini).

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Arttek-Dev/challenge-alura-agente.git](https://github.com/Arttek-Dev/challenge-alura-agente.git)
   cd challenge-alura-agente
Instale as dependências:

Bash
pip install -r requirements.txt
Configure a Chave de API:
Crie a pasta .streamlit e dentro dela o arquivo secrets.toml:

Ini, TOML
GOOGLE_API_KEY = "SUA_CHAVE_API_AQUI"
Execute a aplicação:

Bash
python -m streamlit run app.py
Acesse no navegador: http://localhost:8501.

🐳 Execução com Docker
Construir a imagem Docker:

Bash
docker build -t bimbam-agent .
Executar o contêiner:

Bash
docker run -d -p 8501:8501 -e GOOGLE_API_KEY="SUA_CHAVE_API_AQUI" --name bimbam-app bimbam-agent
💬 Exemplos de Perguntas e Respostas
Exemplo 1: Apresentação e Escopo do Agente
Pergunta do Cliente:

"O que vc faz ?"

Resposta do Agente:

"Olá! Sou o assistente virtual oficial de suporte ao cliente da BimBam Buy. Estou aqui para tirar suas dúvidas com base em nossa documentação oficial, ajudando você com informações sobre:

Políticas de reembolsos, trocas e devoluções;

Prazos de envio, modalidades de frete e rastreamento;

Métodos de pagamento, parcelamento e descontos;

Garantias, avarias e trocas de produtos;

Programa de afiliados e parcerias.

Como posso ajudar você hoje?"

Exemplo 2: Política de Reembolso e Devoluções
Pergunta do Cliente:

"Qual o prazo para solicitar a devolução de um produto por arrependimento?"

Resposta do Agente:

"De acordo com as políticas oficiais da BimBam Buy, você tem até 7 (sete) dias corridos a partir da data de recebimento do produto para solicitar a devolução por arrependimento, desde que o item esteja em sua embalagem original e sem sinais de uso."

Exemplo 3: Formas de Pagamento e Descontos
Pergunta do Cliente:

"Quais formas de pagamento vocês aceitam e tem desconto no Pix?"

Resposta do Agente:

"A BimBam Buy aceita cartões de crédito (com parcelamento em até 12x), boleto bancário e Pix. Pagamentos realizados via Pix contam com 5% de desconto no valor final dos produtos."

Exemplo 4: Pergunta Fora do Escopo Oficial
Pergunta do Cliente:

"Vocês vendem passagens aéreas?"

Resposta do Agente:

"A BimBam Buy não possui essa informação cadastrada em sua documentação oficial, pois nosso catálogo é focado exclusivamente no comércio eletrônico de produtos físicos."
