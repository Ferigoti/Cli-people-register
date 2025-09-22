# 🧾 People Register / Cadastro de Pessoas

## 📌 Sobre o Projeto

Este projeto é um sistema de linha de comando (CLI) para cadastro e gerenciamento de pessoas. Desenvolvido originalmente durante o curso de Python do Curso em Vídeo, foi aprimorado para utilizar um banco de dados SQLite, tornando-o mais robusto e escalável. O sistema agora permite o cadastro de múltiplos dados, incluindo nome, data de nascimento, naturalidade e telefone.

---

## 🚀 Funcionalidades

- Listar pessoas cadastradas: Exibe uma tabela organizada com ID, nome, nascimento, naturalidade e telefone.
- Adicionar novas pessoas: Cadastra um novo registro com todos os dados.  
- Remover um cadastro: Exclui uma pessoa do banco de dados de forma segura através de seu ID único.  
- Validação de entrada: Garante que dados como nome e opções do menu sejam inseridos corretamente.
- Persistência de dados com SQLite: Os dados são salvos em um banco de dados (`cadastros.db`), garantindo integridade e eficiência.
- Menu simples e intuitivo: Toda a interação acontece através de um menu claro no terminal.

---

## 🛠️ Tecnologias

- Python 3  
- SQLite 3 (através do módulo nativo `sqlite3`)
- Estrutura de projeto modular

---

## ▶️ Como Rodar
  

### 1. Clone o repositório
```
git clone https://github.com/Ferigoti/Cli-people-register 
```
### 2. Navegue até o diretório
```
cd Cli-people-register 
```
### 3. Execute o script principal
```
python main.py
```


📖 Créditos

Este projeto foi desenvolvido com base nos ensinamentos do curso de Python do Gustavo Guanabara (Curso em Vídeo) e foi posteriormente reestruturado e aprimorado por mim.


🤝 Contato

Fique à vontade para sugerir melhorias, abrir uma issue ou entrar em contato!
