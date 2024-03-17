from flask import Blueprint, render_template,redirect,url_for, request, flash
from models import Cliente, db
cliente = Blueprint("cliente", __name__, template_folder = './views/admin/', static_folder='./static/', root_path="./")

@cliente.route("/")
def iot_index():
    return render_template("/clientes/clientes_index.html")

@cliente.route("/register_cliente")
def register_cliente():
    return render_template("/clientes/register_cliente.html")

@cliente.route("/view_clientes")
def view_clientes():
    clientes = Cliente.get_clientes()
    return render_template("/clientes/view_clientes.html", clientes = clientes)

@cliente.route("/save_clientes", methods = ["POST"])
def save_clientes():
    cpf = request.form.get("cpf")
    name = request.form.get("name")
    address = request.form.get("address")
    contact = request.form.get("contact")
    birth_date = request.form.get("birth_date")

    Cliente.save_cliente(cpf, name, address, contact , birth_date)

    return redirect(url_for('admin.cliente.view_clientes'))

@cliente.route("/update_cliente/<cpf>")
def update_cliente(cpf):
    cliente = db.session.query(Cliente).filter(Cliente.cpf == int(cpf)).first()
    
    return render_template("/clientes/update_cliente.html", cliente = cliente)

@cliente.route("/save_cliente_changes", methods = ["POST"])
def save_cliente_changes():
    data = request.form.copy()
    Cliente.update_cliente(data)
    return redirect(url_for("admin.cliente.view_clientes"))

@cliente.route("/delete_cliente/<cpf>")
def delete_cliente(cpf):
    if Cliente.delete_cliente(cpf):
        flash("Cliente Excluído com sucesso!!", "success")
    else:
        flash("Cliente não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.cliente.view_clientes"))