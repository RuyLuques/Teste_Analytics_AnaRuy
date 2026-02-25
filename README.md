# Teste Técnico – Estágio Analytics – Quod

## Estrutura do Projeto
Teste_Analytics_AnaRuy/

├── data/  
│   ├── raw/  
│   │   └── data_simulated.csv  
│   └── processed/  
│       └── data_clean.csv  

├── src/  
│   ├── simulacao_dados.py  
│   ├── limpeza_dados.py  
│   └── analise_exploratoria.py  

├── sql/  
│   └── consultas_sql.sql  

├── reports/  
│   └── relatorio_insights.md  

├── requirements.txt  
└── README.md  

---

## Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/RuyLuques/Teste_Analytics_AnaRuy.git
cd Teste_Analytics_AnaRuy
```
### 2. Criar e ativar ambiente virtual
Windows
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Executar os scripts na seguinte ordem
```bash
python src/simulacao_dados.py
```
```bash
python src/limpeza_dados.py
```
```bash
python src/analise_exploratoria.py
```

### 5. Suposições
- O dataset foi simulado para o período de 01/01/2023 a 31/12/2023.
- A consulta SQL referente a junho considera o mês de junho de 2023.
- Foram inseridos valores faltantes e duplicatas propositalmente para atender aos requisitos de limpeza do teste.

Documentações: https://drive.google.com/file/d/1Hc6-8o01TqFiApWJNjGd_HENv2S81bnQ/view?usp=sharing
