# Reinos de Ferro Blog

**Reinos de Ferro Blog** é um projeto desenvolvido para documentar e compartilhar o histórico de aventuras de um grupo de RPG, com foco no universo fantástico dos **Reinos de Ferro**. Este blog oferece uma plataforma intuitiva e funcional para organizar, exibir e gerenciar conteúdos relacionados às aventuras, como narrativas, personagens, mapas e mais. 

## 🏗️ Estrutura do Projeto

O blog foi desenvolvido utilizando **Django**, o que permite uma organização modular e extensível. A estrutura inclui os seguintes principais componentes:

### 🗂️ Categorias
- As postagens são organizadas por categorias, facilitando a navegação e a segmentação do conteúdo.
- Exemplo de categorias: *Histórias*, *Personagens*, *Missões*, *Mapas Interativos*.

### ✍️ Postagens
- O sistema de postagens é completo, permitindo o cadastro, edição e exclusão de conteúdos.
- A interface de administração permite a moderação e o controle das publicações.
- Opções para agendamento de postagens, rascunhos e publicações visíveis apenas para administradores ou usuários registrados.

### 🔑 Controle de Usuários
- Sistema de autenticação com login e senha para diferentes tipos de usuários:
  - **Administrador**: Gerencia todo o conteúdo e usuários.
  - **Contribuidor**: Pode adicionar novas postagens, mas necessita de aprovação para publicação.
  - **Leitor**: Pode visualizar conteúdos públicos ou privados (mediante autorização).
- Segurança robusta com gerenciamento de senhas e recuperação de contas.

### 📚 Aplicativos Incluídos
- **Core App**: Gerencia a estrutura principal do blog, incluindo as categorias e postagens.
- **User Management**: Implementa o sistema de login, registro e perfis de usuários.
- **Frontend**: Interface para exibição do conteúdo com design responsivo e elegante.
- **Admin Panel**: Administração para gerenciar dados, usuários e configurações.

## ⚙️ Funcionalidades
1. **Publicação e Gerenciamento de Conteúdo**:
   - Publicação de histórias e aventuras.
   - Controle de status das postagens (rascunho, publicado, privado).
2. **Comentários**:
   - Sistema de comentários nas postagens, com moderação.
   - Opção de ativar ou desativar comentários por postagem.
3. **Busca e Filtros**:
   - Pesquisa por título, categoria ou data.
   - Filtros para exibir postagens específicas.
4. **Autenticação e Autorização**:
   - Registro e login de usuários com autenticação segura.
   - Painel de usuário para gerenciar informações e preferências.
5. **Design Responsivo**:
   - Totalmente responsivo, ajustando-se a dispositivos móveis, tablets e desktops.
6. **SEO-Friendly**:
   - URLs otimizadas para melhorar a indexação nos mecanismos de busca.

## 🎨 Tecnologias Utilizadas
- **Django**: Framework principal para desenvolvimento backend.
- **SQLite**: Banco de dados padrão (pode ser substituído por outro, como PostgreSQL).
- **Bootstrap**: Estilização frontend para um design elegante e responsivo.
- **jQuery**: Adicionado para interatividade e dinamismo no frontend.

## 🛠️ Configuração e Execução
### Pré-requisitos
- Python 3.8 ou superior
- Pip (gerenciador de pacotes)
- Virtualenv (recomendado)

### Passos para Configuração
1. Clone o repositório:
   ```bash
   git clone https://github.com/carlosalbertoprojetos/reinosdeferro.git
   cd reinosdeferro
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure o banco de dados:
   ```bash
   python manage.py migrate
   ```
5. Crie um superusuário:
   ```bash
   python manage.py createsuperuser
   ```
6. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

Acesse o blog em: `http://127.0.0.1:8000`

## 💡 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

## 📄 Licença
Este projeto está licenciado sob a licença [MIT](LICENSE).
