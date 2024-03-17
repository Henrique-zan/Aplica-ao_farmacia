from flask import Blueprint, render_template,redirect,url_for, request, flash
from models import Produto, Device, db, Microcontroller
produtos = Blueprint("produtos", __name__, template_folder = './views/admin/', static_folder='./static/', root_path="./")

@produtos.route("/")
def produtos_index():
    return render_template("/produtos/produtos_index.html")

@produtos.route("/register_produto")
def register_produto():
    return render_template("/produtos/register_produto.html")

@produtos.route("/view_produtos")
def view_produtos():
    produtos = Produto.get_produtos()
    return render_template("/produtos/view_produtos.html", produtos = produtos)

@produtos.route("/save_produtos", methods = ["POST"])
def save_produtos():
    name = request.form.get("name")
    type = request.form.get("type")
    sector = request.form.get("sector")
    current_price = request.form.get("current_price")
    available_quantity = request.form.get("available_quantity")
    batch_date = request.form.get("batch_date")

    Produto.save_produto(name, type, sector, current_price , available_quantity,batch_date)

    return redirect(url_for('admin.produtos.view_produtos'))

@produtos.route("/update_produto/<id>")
def update_produto(id):
    produto = db.session.query(Produto).filter(Produto.id == int(id)).first()
    
    return render_template("/produtos/update_produto.html", produto = produto)

@produtos.route("/save_produto_changes", methods = ["POST"])
def save_produto_changes():
    data = request.form.copy()
    Produto.update_produto(data)
    return redirect(url_for("admin.produtos.view_produtos"))

@produtos.route("/delete_produto/<id>")
def delete_produto(id):
    if Produto.delete_produto(id):
        flash("Produto Excluído com sucesso!!", "success")
    else:
        flash("Produto não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.produtos.view_produtos"))