# TodoFlask

## Routes

collezioni: tasks <br>
risorse: task(titolo, contenuto, data, id, stato)


### Operazioni

- creazione di un task: `POST /tasks`
- cancellazione di un task: `DELETE /tasks/<id>`
- modificare un task: `PUT /tasks/<id>`
- leggi tasks: `GET /tasks`
- dettagli del tasks: `GET /tasks/<id>`

### Per eseguire il server flask 
python3 -m flask --app app.py run
