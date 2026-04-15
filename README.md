# Calculadora em Python + Streamlit

Projeto de calculadora com operações matemáticas básicas e avançadas, com duas formas de uso:
- modo terminal (`calculadora.py`)
- interface web com Streamlit (`app_streamlit.py`)

## Funcionalidades

- Soma (`+`)
- Subtração (`-`)
- Multiplicação (`*`)
- Divisão (`/`)
- Divisão inteira (`//`)
- Resto da divisão (`%`)
- Potência (`**`)

## Requisitos

- Python 3.10+

## Instalação

```bash
pip install -r requirements.txt
```

## Executar no terminal

```bash
python calculadora.py
```

## Executar interface Streamlit

```bash
streamlit run app_streamlit.py
```

Depois, abra o endereço exibido no terminal (normalmente `http://localhost:8501`).

## Estrutura principal

- `calculadora.py`: lógica das operações e execução via CLI
- `app_streamlit.py`: interface web com Streamlit
- `requirements.txt`: dependências do projeto
