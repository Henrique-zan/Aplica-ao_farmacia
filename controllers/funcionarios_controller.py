from flask import Blueprint, render_template,redirect,url_for, request, flash
from models import Funcionarios, db,Device
funcionario = Blueprint("funcionario", __name__, template_folder = './views/admin/', static_folder='./static/', root_path="./")

@funcionario.route("/")
def iot_index():
    return render_template("/funcionarios/funcionarios_index.html")

@funcionario.route("/register_funcionario")
def register_funcionario():
    return render_template("/funcionarios/register_funcionario.html")

@funcionario.route("/view_funcionarios")
def view_funcionarios():
    funcionarios = Funcionarios.get_funcionarios()
    return render_template("/funcionarios/view_funcionarios.html", funcionarios = funcionarios)

@funcionario.route("/save_funcionarios", methods = ["POST"])
def save_funcionarios():
    cpf = request.form.get("cpf")
    name = request.form.get("name")
    numero_carteira = request.form.get("numero_carteira")
    contato = request.form.get("contato")
    salario = request.form.get("salario")
    birth_date = request.form.get("birth_date")

    Funcionarios.save_funcionario(cpf, name, numero_carteira, contato ,salario, birth_date)

    return redirect(url_for('admin.funcionario.view_funcionarios'))

@funcionario.route("/update_funcionario/<cpf>")
def update_funcionario(id):
    funcionario = db.session.query(Device, Funcionarios)\
                        .join(Funcionarios, Funcionarios.id == Device.id)\
                        .filter(Funcionarios.cpf == int(id)).first()
    
    return render_template("/funcionarios/update_funcionario.html", funcionario = funcionario)

@funcionario.route("/save_funcionario_changes", methods = ["POST"])
def save_funcionario_changes():
    data = request.form.copy()
    data["is_active"] = data.get("is_active") == "on"
    Funcionarios.update_funcionario(data)
    return redirect(url_for("admin.funcionario.view_funcionarios"))

@funcionario.route("/delete_funcionario/<cpf>")
def delete_funcionario(cpf):
    if Funcionarios.delete_funcionario(cpf):
        flash("Funcionarios Excluído com sucesso!!", "success")
    else:
        flash("Funcionarios não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.funcionario.view_funcionarios"))