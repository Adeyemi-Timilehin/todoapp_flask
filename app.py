from crypt import methods
from email.policy import default
from flask import Flask, redirect,render_template,request, url_for,jsonify,abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tolu1992@localhost:5432/todoapp'
db=SQLAlchemy(app)

migrate=Migrate(app,db)

class Todo(db.Model):
    __tablename__='todos'
    id=db.Column(db.Integer,primary_key=True)
    description=db.Column(db.String(),nullable=False)
    completed=db.Column(db.Boolean,nullable=False,default=False)

def __repr__(self):
        return f'<Todo {self.id}> {self.description}>'
@app.route('/todos/create',methods=['POST'])

def create_todo():
  error = False
  body = {}
  try:
    description = request.get_json()['description']
    todo = Todo(description=description)
    db.session.add(todo)
    db.session.commit()
    body['description'] = todo.description
  except:
    error = True
    db.session.rollback()
    print(sys.exc_info())
  finally:
    db.session.close()
  if error:
    abort (400)
  else:
    return jsonify(body)

    # return redirect(url_for('index'))
    

@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):
  try:
    completed = request.get_json()['completed']
    print('completed', completed)
    todo = Todo.query.get(todo_id)
    todo.completed = completed
    db.session.commit()
  except:
    db.session.rollback()
  finally:
    db.session.close()
  return redirect(url_for('index'))


@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
  try:
    Todo.query.filter_by(id=todo_id).delete()
    db.session.commit()
   
  except:
    db.session.rollback()
  finally:
    db.session.close()
  return jsonify({ 'success': True })


@app.route('/')

def index():
     return render_template('index.html', data=Todo.query.all())
if __name__=='__main':
    app.run(host='0.0.0.0')
