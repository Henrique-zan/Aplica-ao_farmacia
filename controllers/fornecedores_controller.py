from flask import Blueprint, render_template,redirect,url_for, request, flash
from models import Fornecedor, db
fornecedor = Blueprint("fornecedor", __name__, template_folder = './views/admin/', static_folder='./static/', root_path="./")

@fornecedor.route("/")
def iot_index():
    return render_template("/fornecedores/fornecedores_index.html")

@fornecedor.route("/register_fornecedor")
def register_fornecedor():
    return render_template("/fornecedores/register_fornecedor.html")

@fornecedor.route("/view_fornecedores")
def view_fornecedores():
    fornecedores = Fornecedor.get_fornecedores()
    return render_template("/fornecedores/view_fornecedores.html", fornecedores = fornecedores)

@fornecedor.route("/save_fornecedores", methods = ["POST"])
def save_fornecedores():
    cnpj = request.form.get("cnpj")
    nome = request.form.get("nome")
    endereço = request.form.get("endereço")
    contato = request.form.get("contato")

    Fornecedor.save_fornecedor(cnpj, nome, endereço, contato)

    return redirect(url_for('admin.fornecedor.view_fornecedores'))

@fornecedor.route("/update_fornecedor/<cnpj>")
def update_fornecedor(cnpj):
    fornecedor = db.session.query(Fornecedor).filter(Fornecedor.cnpj == int(cnpj)).first()
    return render_template("/fornecedores/update_fornecedor.html", fornecedor = fornecedor)

@fornecedor.route("/save_fornecedor_changes", methods = ["POST"])
def save_fornecedor_changes():
    data = request.form.copy()
    Fornecedor.update_fornecedor(data)
    return redirect(url_for("admin.fornecedor.view_fornecedores"))

@fornecedor.route("/delete_fornecedor/<cnpj>")
def delete_fornecedor(cnpj):
    if Fornecedor.delete_fornecedor(cnpj):
        flash("Fornecedor Excluído com sucesso!!", "success")
    else:
        flash("Fornecedor não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.fornecedor.view_fornecedores"))