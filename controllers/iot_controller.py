from flask import Blueprint, render_template,redirect,url_for, request, flash,jsonify
from models import Sensor, Device, db, Microcontroller,Read
iot = Blueprint("iot", __name__, template_folder = './views/admin/', static_folder='./static/', root_path="./")
from models.mqtt import mqtt_client
@iot.route("/")
def iot_index():
    return render_template("/iot/iot_index.html")

@iot.route('/messages')
def check_messages():
    return render_template("/iot/list_reads.html",reads=Read.query.order_by(Read.id.desc()).first())

@iot.route('/publish_1', methods=['POST'])
def publish_1():
    mqtt_client.publish('/pharmhub/botao','1')
    return redirect(url_for("admin.iot.check_messages"))

@iot.route('/publish', methods=['GET','POST'])
def publish_message():
    request_data = request.get_json()
    publish_result = mqtt_client.publish(request_data['topic'], request_data['message'])
    return jsonify(publish_result)



@iot.route("/register_sensor")
def register_sensor():
    return render_template("/iot/register_sensor.html")

@iot.route("/view_sensors")
def view_sensors():
    sensors = Sensor.get_sensors()
    return render_template("/iot/view_sensors.html", sensors = sensors)

@iot.route("/save_sensors", methods = ["POST"])
def save_sensors():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    description = request.form.get("description")
    measure = request.form.get("measure")
    voltage = request.form.get("voltage")
    is_active = True if request.form.get("is_active") == "on" else False

    Sensor.save_sensor(name, brand, model, description ,voltage, is_active, measure)

    return redirect(url_for('admin.iot.view_sensors'))

@iot.route("/update_sensor/<id>")
def update_sensor(id):
    sensor = db.session.query(Device, Sensor)\
                        .join(Sensor, Sensor.id == Device.id)\
                        .filter(Sensor.id == int(id)).first()
    
    return render_template("/iot/update_sensor.html", sensor = sensor)

@iot.route("/save_sensor_changes", methods = ["POST"])
def save_sensor_changes():
    data = request.form.copy()
    data["is_active"] = data.get("is_active") == "on"
    Sensor.update_sensor(data)
    return redirect(url_for("admin.iot.view_sensors"))

@iot.route("/delete_sensor/<id>")
def delete_sensor(id):
    if Sensor.delete_sensor(id):
        flash("Dispositivo Sensor Excluído com sucesso!!", "success")
    else:
        flash("Dispositivo Sensor não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.iot.view_sensors"))


#####################################################################################################################################


@iot.route("/register_microcontroller")
def register_microcontroller():
    return render_template("/iot/register_microcontroller.html")

@iot.route("/view_microcontrollers")
def view_microcontrollers():
    microcontrollers = Microcontroller.get_microcontrollers()
    return render_template("/iot/view_microcontrollers.html", microcontrollers = microcontrollers)

@iot.route("/save_microcontrollers", methods = ["POST"])
def save_microcontrollers():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    description = request.form.get("description")
    voltage = request.form.get("voltage")
    ports = request.form.get("ports")
    is_active = True if request.form.get("is_active") == "on" else False

    Microcontroller.save_microcontroller(name, brand, model, description ,voltage, is_active, ports)

    return redirect(url_for('admin.iot.view_microcontrollers'))

@iot.route("/update_microcontroller/<id>")
def update_microcontroller(id):
    microcontroller = db.session.query(Device, Microcontroller)\
                        .join(Microcontroller, Microcontroller.id == Device.id)\
                        .filter(Microcontroller.id == int(id)).first()
    
    return render_template("/iot/update_microcontroller.html", microcontroller = microcontroller)

@iot.route("/save_microcontroller_changes", methods = ["POST"])
def save_microcontroller_changes():
    data = request.form.copy()
    data["is_active"] = data.get("is_active") == "on"
    Microcontroller.update_microcontroller(data)
    return redirect(url_for("admin.iot.view_microcontrollers"))

@iot.route("/delete_microcontroller/<id>")
def delete_microcontroller(id):
    if Microcontroller.delete_microcontroller(id):
        flash("Dispositivo Microcontroller Excluído com sucesso!!", "success")
    else:
        flash("Dispositivo Microcontroller não pode ser excluído pois está relacionado a leituras salvas no banco!!", "danger")
    return redirect(url_for("admin.iot.view_microcontrollers"))