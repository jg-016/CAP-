# Documento de Visão

## Histórico de Revisões

| Data | Versão | Descrição | Autores |
| :--: | :----: | :-------: | :-----: |
| 10/04/2026 | 1.0 | Versão inicial |  Carlos Danilo |
| 14/05/2026 | 2.0 | Requisitos |  Carlos Danilo  |


## 1. Visão Geral do Sistema Proposto

O sistema proposto tem como objetivo centralizar, em um único ambiente, todas as informações acadêmicas importantes para os alunos, prazos, materiais e cronogramas. Ele funciona como um sistema desenvolvido especificamente para a organização estudantil, oferecendo aos alunos um espaço unificado de consulta e planejamento.
Além disso, o sistema busca facilitar o acompanhamento das responsabilidades acadêmicas, reduzindo a dispersão de informações entre diferentes plataformas e melhorando a organização pessoal dos estudantes. A proposta também incentiva a colaboração entre os membros de uma mesma turma, permitindo que informações relevantes sejam compartilhadas e mantidas atualizadas de forma coletiva.


## 2. Descrição do Problema
| - | - |
| :-: | :-: |
| **Problema** |Ausência de um local adequado para organizar informações acadêmicas, levando os estudantes a utilizarem aplicativos que não foram pensados para esse fim |
| **Afeta** |Estudantes que precisam lidar com materiais de aula, atividades , mudanças no cronogramas publicados em locais distintos |  
| **Impacta** | organização acadêmica,cumprimento de prazos e acompanhamento das aulas |
| **Solução** | Criar um sistema que permita aos alunos centralizarem e organizarem todas as informações de forma independente da plataforma utilizada pelos docentes| 

## 3. Descrição dos Usuários 

| Usuário | Descrição | Responsabilidades |
| :--- | :--- | :--- |
| Aluno | Estudantes que desejam ver as atividades, materiais e cronogramas de aula | Utilizar o sistema, consultar informações prontas e organizar seu calendário pessoal. |
| Representante / Líder de Turma | Alunos responsáveis por organizar e manter atualizadas as informações principais do sistema, garantindo que o conteúdo base esteja pronto para todos os colegas. | Organizar e atualizar o conteúdo base, validar informações e manter o sistema completo para a turma |

## 4. Descrição do Ambiente dos Usuários

| Usuário | Ambiente operacional |
| :--- | :--- |
| Aluno | Computadores |


## 5. Principais Necessidades dos Usuários

> Apresentadas no formato de tópicos
1. **Aluno**
   - Unificar atividades e prazos em um só lugar.
   - Acessar todos os materiais de aula facilmente.
   - Receber avisos de prazos importantes.
   - Visualizar mudanças de horário ou sala rapidamente.
   - Visualizar um calendário completo e organizado.
1. **Representante / Líder de Turma**
   - Validar informações adicionadas pelos colegas.
   - Atualizar cronogramas conforme avisos dos professores
   - Facilitar a comunicação entre os estudantes


## 6. Alternativas Concorrentes

1. **Google Classroom**
   - Ótima organização para materiais e atividades
   - Depende do engajamento do professor para suprir as necessidades dos alunos
1. **SUAP**
   - Plataforma institucional oficial com funcionalidades acadêmicas
   - Uso inconsistente pelos professores

## 7. Regras de Negócio

| ID  | Regra | Descrição |
| :-: | :---: | :-------: |
| RN01 | Associação de Evento ao Calendário | Todo evento deve estar associado a exatamente um calendário |
| RN02 | Herança de Cor do Calendário | Todo calendário deve ter uma cor, da qual todos os seus eventos herdam |
| RN03 | Existência de Administrador | Toda turma e todo calendário deve ter pelo menos um administrador |

## 8. Requisitos Funcionais

| Código | Nome | Descrição | Prioridade |
| :----: | :--: | :-------: | :--------: |
| RF01 | Gerir conta | Permitir que o usuário crie, visualize, atualize e exclua sua conta | Alta |
| RF02 | Atutenticação | Permitir que o usuário entre e saia do sistema | Alta |
| RF03 | Gerir calendário | Permitir criar, visualizar, atualizar e excluir calendários (pessoais e acadêmicos)| Alta |
| RF04 | Gerir calendário da turma | Permitir adicionar e remover e listas calendários de turma | Alta |
| RF05 | Gerir evento de calendário | Permitir adicionar, remover e listar calendários de uma turma | Alta |
| RF06 | Gerir turma | Permitir que o estudante crie, visualize, atualize e exclua turmas | Alta |
| RF07 | Gerir membro de turma | Permitir adicionar, remover e alterar permissões de participantes da turma. Permitir também listar os participantes | Alta |
| RF08 | Gerir suas inscrições em turma | Permitir que o aluno entre e saia de turmas e atualize suas preferencias de turma | Alta |
> **Prioridade**: alta, média ou baixa

## 9. Requisitos Não-Funcionais
| Código | Nome | Descrição | Categoria | Classificação |
| :----: | :--: | :-------: | :-------: | :-----------: |
| NF01 | Tempo de resposta | O sistema deve carregar os eventos em até 10 segundos | Performance | Desejável |
| NF02 | Interface objetiva | O layout deve permitir que o usuário identifique seus compromissos principais rapidamente após o login | Usabilidade | Obrigatório |
| NF03 | Autenticação | O usuário deve ser autenticado no sistema para poder usá-lo | Suportabilidade | Obrigatório |
| NF04 | Segurança de dados | Dados pessoais e materiais devem ser armazenados e transmitidos de forma segura | Segurança | Obrigatório |
| NF05 | Disponibilidade do site | O tempo de atividade deve ser de 24 horas por dia | Confiabilidade | Obrigatório |


> **Categoria**: usabilidade, confiabilidade, performance, suportabilidade, restrição de projeto, implementação, interface e requisito físico - segundo classificação [FURP+](https://pt.wikipedia.org/wiki/FURPS).

> **Classificação**: desejável ou obrigatório.
