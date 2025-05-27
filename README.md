# 🎧 Dashboard Interativo: Análise de Faixas Musicais com Plotly e Dash

Projeto desenvolvido por **João Vitor Costa Rolim**, aluno do **5º semestre** do curso de **Análise e Desenvolvimento de Sistemas** da **Unichristus**, como parte da disciplina de **Visualização de Dados**.

## 📌 Objetivo

O objetivo deste projeto é fornecer **insights visuais interativos** a partir de dados de faixas musicais do Spotify. A ideia central é auxiliar **produtores musicais** a identificarem padrões de sucesso e tomarem decisões baseadas em dados, com base em atributos como **popularidade, duração, BPM e compasso**.

---

## 📊 Funcionalidades do Dashboard

O dashboard foi construído com **Plotly Dash** e permite:

### 🎼 Seleção de Gêneros

- O usuário pode selecionar **um ou mais gêneros musicais** para análise.

### 📈 Análises Interativas

1. **Popularidade por Gênero**  
   Gráfico de barras que exibe a **popularidade média** de cada gênero selecionado.

2. **Duração da Faixa vs Popularidade**  
   Gráfico de dispersão (scatter plot) mostrando como a duração das faixas (em minutos) se relaciona com a popularidade. Permite descobrir se faixas curtas ou longas tendem a ter mais sucesso.

3. **Distribuição de BPM (Tempo)**  
   Histograma interativo que revela o intervalo de **batidas por minuto (BPM)** mais comum entre as faixas populares.

4. **Assinatura de Compasso Mais Popular**  
   Gráfico de barras exibindo quais assinaturas de compasso (como 4/4, 3/4, etc.) são mais frequentes entre faixas populares.

5. **Recomendações Baseadas em Padrões Populares**  
   Exibição de uma tabela com faixas que **melhor representam os padrões de popularidade** detectados (com base em BPM, duração e compasso).

---

## 🛠️ Tecnologias Utilizadas

- Python 3.12
- Dash
- Plotly Express
- Pandas
- Bootstrap (via Dash Bootstrap Components)

---
