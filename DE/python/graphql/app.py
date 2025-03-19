from flask import Flask
from flask_graphql import GraphQLView
import graphene

# Определяем тип данныхъ (Объект User)
class User(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()

# Определяем Query (запросы)
class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        # Тут можно запрос в базу данных
        return [
            User(id=1, name='Алексей', age=25),
            User(id=2, name='Мария', age=34),
        ]

# Создаем схему
schema = graphene.Schema(query=Query)

# Настраиваем Flask приложения
app = Flask(__name__)
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

if __name__ == '__main__':
    app.run(debug=True)