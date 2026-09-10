# Relatorio de Implementacao dos CDUs de Eventos

## Objetivo

Este documento registra a implementacao dos seguintes casos de uso:

- CDU-014: Visualizar evento.
- CDU-016: Deletar evento.

O comportamento implementado permite que um usuario autenticado clique em um evento para consultar seus dados. A exclusao e exibida e executada somente quando o usuario e administrador do calendario associado.

## Arquivos criados

### `mysite/apps/eventos/templates/eventos/visualizar_evento.html`

Tela de detalhes do evento. Exibe:

- Nome do evento.
- Descricao.
- Data.
- Horario de inicio e fim.
- Calendario associado.
- Link para voltar ao calendario.
- Link para deletar o evento, somente quando `usuario_eh_admin` for verdadeiro.

Codigo criado:

```html
{% extends 'core/base.html' %}

{% block title %}{{ evento.nome }}{% endblock %}

{% block content %}
<section class="evento-detalhes" aria-labelledby="evento-titulo">
    <a href="{% url 'calendario' evento.calendario.id %}">Voltar ao calendário</a>
    <h1 id="evento-titulo">{{ evento.nome }}</h1>

    <dl>
        <dt>Descrição</dt>
        <dd>{{ evento.conteudo|default:"Sem descrição." }}</dd>

        <dt>Data</dt>
        <dd>{{ evento.inicio|date:"d/m/Y" }}</dd>

        <dt>Horário</dt>
        <dd>{{ evento.inicio|date:"H:i" }} - {{ evento.fim|date:"H:i" }}</dd>

        <dt>Calendário</dt>
        <dd>{{ evento.calendario.nome }}</dd>
    </dl>

    {% if usuario_eh_admin %}
        <a href="{% url 'eventos:deletar_evento' evento.id %}">Deletar evento</a>
    {% endif %}
</section>
{% endblock %}
```

### `mysite/apps/eventos/templates/eventos/deletar_evento.html`

Tela de confirmacao da exclusao. A operacao exige `POST` e token CSRF. O usuario pode confirmar ou cancelar.

Codigo criado:

```html
{% extends 'core/base.html' %}

{% block title %}Deletar evento{% endblock %}

{% block content %}
<section class="evento-confirmacao" aria-labelledby="confirmacao-titulo">
    <h1 id="confirmacao-titulo">Deletar evento</h1>
    <p>Tem certeza que deseja deletar o evento <strong>{{ evento.nome }}</strong>?</p>
    <p>Essa ação não poderá ser desfeita.</p>

    <form method="post">
        {% csrf_token %}
        <button type="submit">Deletar evento</button>
        <a href="{% url 'eventos:visualizar_evento' evento.id %}">Cancelar</a>
    </form>
</section>
{% endblock %}
```

## Arquivos alterados

### `mysite/apps/eventos/views.py`

Foram adicionados os imports:

```python
from django.shortcuts import get_object_or_404, redirect, render
from apps.calendarios.models import MembroDeCalendario
```

Foi adicionada a view de visualizacao:

```python
@login_required
def visualizar_evento(request, id):
    evento = get_object_or_404(
        Evento.objects.select_related('calendario'),
        id=id,
        calendario__usuarios=request.user,
    )
    membro = get_object_or_404(
        MembroDeCalendario,
        calendario=evento.calendario,
        usuario=request.user,
    )

    return render(
        request,
        'eventos/visualizar_evento.html',
        {'evento': evento, 'usuario_eh_admin': membro.eh_admin},
    )
```

Foi adicionada a view de exclusao:

```python
@login_required
def deletar_evento(request, id):
    evento = get_object_or_404(
        Evento.objects.select_related('calendario'),
        id=id,
        calendario__usuarios=request.user,
    )
    membro = get_object_or_404(
        MembroDeCalendario,
        calendario=evento.calendario,
        usuario=request.user,
    )

    if not membro.eh_admin:
        return redirect('eventos:visualizar_evento', id=evento.id)

    if request.method == 'POST':
        calendario_id = evento.calendario_id
        evento.delete()
        return redirect('calendario', id=calendario_id)

    return render(request, 'eventos/deletar_evento.html', {'evento': evento})
```

Regras implementadas:

1. O usuario precisa estar autenticado por causa do decorator `login_required`.
2. O evento precisa pertencer a um calendario do usuario.
3. O usuario precisa ser membro do calendario.
4. Apenas membros com `eh_admin=True` podem excluir.
5. A exclusao ocorre somente com requisicao `POST`.
6. Depois da exclusao, o usuario volta para o calendario do evento.
7. Usuarios comuns sao redirecionados para a visualizacao e o evento permanece salvo.

### `mysite/apps/eventos/urls.py`

Foram adicionadas as rotas:

```python
from .views import criar_evento, deletar_evento, visualizar_evento

urlpatterns = [
    path('criar/', criar_evento, name='criar_evento'),
    path('<int:id>/', visualizar_evento, name='visualizar_evento'),
    path('<int:id>/deletar/', deletar_evento, name='deletar_evento'),
]
```

URLs resultantes:

- `/eventos/<id>/`: visualizar um evento.
- `/eventos/<id>/deletar/`: confirmar ou executar a exclusao de um evento.

### `mysite/apps/core/views/inicio.py`

O contexto dos eventos do calendario geral passou a incluir os dados necessarios para gerar o link de detalhes:

```python
eventos_context.append({
    'id': evento.id,
    'nome': evento.nome,
    'conteudo': evento.conteudo,
    'inicio': evento.inicio,
    'fim': evento.fim,
    'calendario_id': calendario.id,
    'paleta': membro_calendario.numero_paleta,
})
```

### `mysite/apps/core/templates/core/calendario_geral.html`

Cada evento do calendario geral deixou de ser uma `div` sem acao e passou a ser um link para a visualizacao:

```html
<a href="{% url 'eventos:visualizar_evento' evento.id %}"
   class="evento-calendario paleta-{{ evento.paleta }}"
   data-data="{{ evento.inicio|date:'Y-m-d' }}"
   data-inicio="{{ evento.inicio|date:'H:i' }}"
   data-fim="{{ evento.fim|date:'H:i' }}"
   aria-label="Visualizar evento {{ evento.nome }}">
    <div class="conteudo-evento">
        <div class="evento-titulo">{{ evento.nome }}</div>
        <div class="evento-horario">
            {{ evento.inicio|date:'H:i' }} - {{ evento.fim|date:'H:i' }}
        </div>
    </div>
</a>
```

### `mysite/apps/calendarios/views.py`

A view do calendario passou a gerar `eventos_json`, usado pela grade semanal em JavaScript:

```python
eventos_json = json.dumps([
    {
        'id': evento.id,
        'title': evento.nome,
        'description': evento.conteudo,
        'date': evento.inicio.strftime('%Y-%m-%d'),
        'start': evento.inicio.hour + evento.inicio.minute / 60,
        'end': evento.fim.hour + evento.fim.minute / 60,
        'detail_url': reverse(
            'eventos:visualizar_evento', args=[evento.id]
        ),
    }
    for evento in eventos
])
```

Esse valor foi incluído no contexto:

```python
'eventos_json': eventos_json,
```

Essa alteracao tambem corrige a ausencia do contexto `eventos_json`, que ja era esperado pelo JavaScript da pagina semanal.

### `mysite/apps/calendarios/templates/calendarios/calendario.html`

O bloco visual de cada evento agora e acessivel por teclado e redireciona para os detalhes ao receber clique, `Enter` ou `Espaco`:

```javascript
const block = document.createElement('div');
block.className = 'calendar-event-block';
block.setAttribute('role', 'link');
block.tabIndex = 0;

block.addEventListener('click', () => {
    window.location.href = event.detail_url;
});

block.addEventListener('keydown', (keyboardEvent) => {
    if (keyboardEvent.key === 'Enter' || keyboardEvent.key === ' ') {
        keyboardEvent.preventDefault();
        window.location.href = event.detail_url;
    }
});
```

Tambem foi usado valor padrao para evitar erro quando nao existirem eventos:

```javascript
window.calendarEvents = {{ eventos_json|default:'[]'|safe }};
```

### `mysite/apps/core/static/core/css/calendario_geral.css`

Os eventos do calendario geral agora mantem a aparencia de bloco mesmo sendo elementos `<a>`:

```css
color: inherit;
text-decoration: none;
```

## Testes adicionados

### `mysite/apps/eventos/tests.py`

Foi criada a classe `EventoViewTests` com tres testes:

1. `test_visualizar_evento_exibe_informacoes`
   - Verifica status HTTP 200.
   - Verifica nome e descricao do evento.
   - Verifica que o administrador ve a opcao de deletar.

2. `test_deletar_evento_remove_evento_e_redireciona`
   - Envia `POST` para a rota de exclusao.
   - Verifica o redirecionamento para o calendario.
   - Verifica que o evento foi removido do banco.

3. `test_membro_comum_nao_pode_deletar_evento`
   - Autentica um membro que nao e administrador.
   - Tenta excluir o evento.
   - Verifica que ele volta para a visualizacao.
   - Verifica que o evento continua salvo.

## Validacao

### Diagnostico dos eventos nao exibidos

Foi verificado que os eventos existentes no banco estavam nestas datas:

- `01/01/2026`.
- `01/03/2026`.

O calendario geral abre inicialmente na semana atual, que no momento da verificacao era de `06/09/2026` a `12/09/2026`. Como a view filtra os eventos pelos sete dias da semana selecionada, os eventos antigos nao aparecem nessa semana inicial.

Os eventos aparecem quando o usuario navega ate a semana correspondente usando os botoes de semana anterior/proxima, ou quando cria um evento dentro da semana atualmente exibida.

A consulta usada pela view e equivalente a:

```python
eventos = Evento.objects.filter(
    calendario=calendario,
    inicio__date__in=[data.isoformat() for data in datas]
)
```

Tambem foi confirmado que os eventos estavam associados ao calendario do usuario e que esse calendario nao estava oculto. Portanto, o comportamento observado foi causado pela data dos eventos em relacao a semana em foco, e nao por perda ou falha no salvamento dos eventos.

### Correcao posterior no fluxo de criacao

Depois da implementacao inicial, a criacao de um evento em um usuario sem calendario pessoal revelou o erro:

```text
IntegrityError: NOT NULL constraint failed: calendarios_membrodecalendario.eh_admin
```

O problema estava em `mysite/apps/eventos/views.py`: o codigo usava `calendario.usuarios.add(request.user)`, mas o relacionamento usa o modelo intermediario `MembroDeCalendario`, que exige os campos `eh_admin` e `numero_paleta`.

O trecho foi substituido por:

```python
MembroDeCalendario.objects.create(
    usuario=request.user,
    calendario=calendario,
    eh_admin=True,
    numero_paleta=request.user.paleta_menos_usada(),
)
```

Tambem foi corrigido o redirecionamento apos a criacao para retornar ao calendario usado:

```python
return redirect('calendario', id=calendario.id)
```

O teste especifico do fluxo passou:

```text
Ran 1 test in 0.497s
OK
```

A verificacao de erros do editor nao apontou erros nos arquivos Python alterados.

A compilacao de sintaxe Python foi executada com sucesso nos modulos alterados.

Os testes Django nao puderam ser executados neste ambiente porque o pacote Django nao esta instalado. O comando usado foi:

```bash
cd 2026-CAP-main\(1\)/2026-CAP-main/mysite
python manage.py test apps.eventos
```

Erro encontrado:

```text
ModuleNotFoundError: No module named 'django'
```

Para executar os testes, instale as dependencias do projeto:

```bash
cd 2026-CAP-main\(1\)/2026-CAP-main
pip install -r requirements.txt
cd mysite
python manage.py test apps.eventos
```

## Resumo final das alteracoes

- 2 arquivos novos de template.
- 2 novas views Django.
- 2 novas rotas.
- Integracao do clique no calendario geral.
- Integracao do clique na visualizacao semanal.
- Serializacao dos eventos para JavaScript.
- Regra de autorizacao para exclusao por administrador.
- Confirmacao de exclusao via tela separada.
- Cancelamento sem alteracao no banco.
- 3 testes automatizados adicionados.
