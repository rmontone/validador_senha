# 🔐 Validador de Senhas Fortes

Um projeto web simples desenvolvido com **Python + Flask + Bootstrap** para validar a segurança de senhas com base em critérios de complexidade, entropia e verificação contra vazamentos públicos (API HaveIBeenPwned).


---

## 📊 Funcionalidades

- ✅ Verificação de **complexidade mínima** (letras, números, símbolos, tamanho).
- 🔢 Cálculo da **entropia** da senha com feedback visual (barra de força).
- 🧠 Tooltip explicativo sobre como a entropia é calculada.
- 🔍 Verificação de vazamento da senha via [HaveIBeenPwned](https://haveibeenpwned.com/API/v3).
- 🎨 Interface responsiva com **Bootstrap 5**, incluindo logo e favicon.

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/rmontone/validador_senha.git
cd validador-senhas
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
python app.py
```

Acesse em `http://127.0.0.1:5000`.

---

## 📁 Estrutura

```
validador-senhas/
│
├── app.py                  # Arquivo principal Flask
├── requirements.txt        # Dependências do projeto
├── static/
│   ├── logo.png            # Logo do projeto
│   └── favicon.ico         # Ícone do navegador
└── templates/
    └── index.html          # Página principal
```

---

## 🧠 Como funciona o cálculo da entropia?

A entropia mede o quão imprevisível é a senha, baseada na fórmula:

```
entropia = comprimento * log2(tamanho do conjunto de caracteres)
```

Exemplo:
- Senha com 12 caracteres que usa letras, números e símbolos → charset = 94
- log2(94) ≈ 6.55
- Entropia = 12 * 6.55 = ~78.6 bits

🔒 Quanto maior a entropia, mais difícil quebrar a senha por força bruta.

---

## 🛠 Tecnologias Utilizadas

- Python 3.8+
- Flask
- Bootstrap 5
- Bootstrap Icons
- API HaveIBeenPwned
- HTML/CSS

---


## 👨‍💻 Autor

Desenvolvido por rmontone(https://github.com/rmontone) 🚀  
Sinta-se livre para usar, estudar, melhorar e compartilhar!

---
