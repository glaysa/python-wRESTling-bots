//<script src={{ url_for('static', filename='socket.js') }}></script> when imported.
/*
{% for msg in room.messages %}
            {% if msg.sender == user %}
                <div class="col-md-5 bg-primary mb-3 align-self-end border rounded-pill">
                    <p class="p-0 fs-6 text-md-center m-2">{{ msg.content.message }}</p>
                </div>
            {% else %}
                <div class="col-md-5 bg-secondary mt-3 align-self-start border rounded-pill">
                    <p class="p-0 fs-6 text-md-center m-2">{{ msg.content.message }}</p>
                </div>
            {% endif %}
        {% endfor %}
 */