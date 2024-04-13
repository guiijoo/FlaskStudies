from flask import Blueprint, render_template, request
from database.clientes import CLIENTES

cliente_route = Blueprint('cliente', __name__)

'''
Rota de clientes

    -/clientes/ (GET) -- listar os cliente
    -/clientes/ (POST) -- inserir clientes no servidor
    -/clientes/new (GET) -- renderiza um formulario para cadastro de um cliente
    -/clientes/id (GET) -- obter os dados de um cliente em especifico
    -/clientes/<id>/edit (GET) -- renderiza um formulario para editar um cliente
    -/clientes/<id>/update (PUT) -- atualizar os dados dos clientes
    -/clientes/<id>/delete (DELETE) -- deleta um registro de usuario

'''

@cliente_route.route('/')
def lista_cliente():
    '''listar os clientes'''
    return render_template('lista_clientes.html', clientes=CLIENTES)


@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    '''inserir os dados de um cliente'''
    
    data = request.json
    
    novo_usuario = {
        
        "id": len(CLIENTES)+1,
        "nome": data['nome'],
        "email": data['email']
        
    }
        
    CLIENTES.append(novo_usuario)
    
    return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new')
def form_novo_cliente():
    '''formulario para criar um cliente'''
    return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    '''exibir detalhes do cliente'''
    return render_template('detalhe_cliente.html')


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    '''formulario para alterar dados do cliente'''
    return render_template('form_edit_cliente.html')


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    '''envio dos dados alterados para o servidor'''
    pass


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    global CLIENTES
    CLIENTES=[c for c in CLIENTES if cliente_id != c['id']]
    return  {"delete": 'deletado'}
'''enviar solicitação de delete de um cliente'''

