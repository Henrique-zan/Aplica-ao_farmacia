from flask import Blueprint, render_template, redirect,url_for
from flask_login import current_user, login_required
from controllers.iot_controller import iot
from controllers.produtos_controller import produtos
from controllers.clientes_controller import cliente
from controllers.funcionarios_controller import funcionario
from controllers.fornecedores_controller import fornecedor
from controllers.vendas_controller import venda
from models.vendas.vendas import Vendas
admin = Blueprint("admin", __name__, 
                    template_folder="./views/", 
                    static_folder='./static/', 
                    root_path="./")

admin.register_blueprint(produtos, url_prefix='/produtos')
admin.register_blueprint(cliente, url_prefix='/clientes')
admin.register_blueprint(fornecedor, url_prefix='/fornecedores')
admin.register_blueprint(funcionario, url_prefix='/funcionarios')
admin.register_blueprint(iot, url_prefix='/iot')
admin.register_blueprint(venda, url_prefix='/vendas')


@admin.route("/")
@admin.route("/admin")
#@login_required
def admin_index():
    vendas = Vendas.get_ultimas_vendas()
    soma = Vendas.get_soma_vendas()
    soma_hoje = Vendas.get_soma_vendas_hoje()
    return render_template("admin/admin_index.html",vendas = vendas,all_sales = soma,soma_hoje = soma_hoje)