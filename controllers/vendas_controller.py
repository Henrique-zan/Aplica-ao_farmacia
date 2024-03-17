from flask import Blueprint, render_template,redirect,url_for, request, flash
from models import Vendas, db
venda = Blueprint("vendas", __name__, template_folder = './views/admin/', static_folder='./static/', root_path="./")

@venda.route("/")
def iot_index():
    return render_template("/vendas/vendas_index.html")

@venda.route("/register_venda")
def register_venda():
    return render_template("/vendas/register_venda.html")

@venda.route("/view_vendas")
def view_vendas():
    vendas = Vendas.get_vendas()
    return render_template("/vendas/view_vendas.html", vendas = vendas)


@venda.route("/save_vendas", methods = ["POST"])
def save_vendas():
    id_produtos = request.form.get("id_produtos")
    cpf_cliente = request.form.get("cpf_cliente")
    cpf_funcionario = request.form.get("cpf_funcionario")
    valor = request.form.get("valor")

    Vendas.save_venda(id_produtos, cpf_cliente, cpf_funcionario , valor)

    return redirect(url_for('admin.vendas.view_vendas'))