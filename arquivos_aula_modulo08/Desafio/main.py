
doc = '''
#%RAML 1.0
title: Codenation RAML Challenge
version: v1
mediaType:  application/json
baseUri: http://localhost/codenationapi
securitySchemes:
    JWT:
        description: Esquema para autenticação com Token JWT.
        type: x-jwt
        describedBy:
            headers:
                Authorization:
                    description: Usado para enviar o JSON Web Token no request.
                    type: string
                    required: true
            responses:
                401:
                    description: |
                        Token inválido ou com expirada. Por favor, 
                        autentique novamente seu usuário.
        settings:
            signatures: ['HMAC-SHA256']

types:
    Auth:
        type: object
        discriminator: token
        properties:
            token: string
    User:
        type: object
        discriminator: user_id
        properties:
            user_id: integer
            name:
                type: string
                maxLength: 50
            password:
                type: string
                maxLength: 50
            email:
                type: string
                maxLength: 254
            last_login:
                type: date-only
            group_id: integer

    Group:
        type: object
        discriminator: group_id
        properties:
            group_id: integer
            name:
                type: string
                maxLength: 20
        example:
            group_id: 10
            name: Group Name

    Agent:
        type: object
        discriminator: agent_id
        properties:
            agent_id: integer
            name:
                type: string
                maxLength: 50
            status: boolean
            environment:
                type: string
                maxLength: 20
            version:
                type: string
                maxLength: 5
            address:
                type: string
                maxLength: 39
            user_id: integer
        example:
            agent_id: 15
            name: Agent Name
            status: true
            environment: Environment X
            version: 1.0.2
            address: api.com
            user_id: 20

    Event:
        type: object
        discriminator: event_id
        properties:
            event_id: integer
            level:
                type: string
                maxLength: 20
            payload: string
            shelve: boolean
            date: datetime-only
            agent_id: integer
        example:
            event_id: 23
            level: Critical
            payload: Payload text.
            shelve: true
            date: 2020-07-01T21:00:00
            agent_id: 5

/auth/token:
    post:
        description: Obter o token de autenticação.
        body:
            application/json:
                properties:
                    name:
                        type: string
                        maxLength: 50
                    password:
                        type: string
                        maxLength: 50
        responses:
            201:
                body:
                    application/json:
                        type: Auth
            400:
                body:
                    application/json:
                        example: |
                            {"error": "Erro de autenticação."}

/agents:
    post:
        description: Adiciona novo agente.
        securedBy: [JWT]
        body: 
            application/json:
                example: |
                    {"name": "Agent Name2",
                    "status": true,
                    "environment": "Environment Y",
                    "version": "3.0.2",
                    "address": "api.com.br",
                    "user_id": 20}
        responses:
            201:
                body:
                    application/json:
                        example: |
                            {"agent_id": 36}
            401:
                body:
                    application/json:
                        example: |
                            {"error": "Você não está autorizado para fazer esta ação."}

    get:
        description: Retorna todos os agentes.
        securedBy: [JWT]
        responses:
            200:
                body:
                    application/json: Agent[]

    /{id}:
        get:
            description: Retorna o usuário com id especificado.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json: Agent
                401:
                    body:
                        application/json: |
                            {"error": "Você não está autorizado para fazer esta ação."}
                404:
                    body:
                        application/json: |
                            {"error": "Agente não encontrado."}
        put:
            description: Atualização de agente pelo id.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json: Agent
                401:
                    body:
                        application/json: |
                            {"error": "Você não está autorizado para fazer esta ação."}
                404:
                    body:
                        application/json: |
                            {"error": "Agente não encontrado."}

        delete:
            description: Remoção de agente pelo id.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json: |
                            {"message": "Agente deletado com sucesso."}
                401:
                    body:
                        application/json: |
                            {"error": "Você não está autorizado para fazer esta ação."}
                404:
                    body:
                        application/json: |
                            {"error": "Agente não encontrado."}
                
    /{id}/events:
        post:
            description: Adição de mais de um evento à um agente específico.
            securedBy: [JWT]
            body:
                application/json: Event[]

            responses:
                201:
                    body:
                        application/json: |
                            {"message": "Eventos adicionados com sucesso."}
                401:
                    body:
                        application/json: |
                            {"error": "Você não está autorizado para fazer esta ação."}
                404:
                    body:
                        application/json: |
                            {"error": "Agente não encontrado."}

        get:
            description: Retornar todos eventos de um agente específico.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json: Event[]
                401:
                    body:
                        application/json: |
                            {"error": "Você não está autorizado para fazer esta ação."}
                404:
                    body:
                        application/json: |
                            {"error": "Agente não encontrado."}

        put:
            description: Alteração dos eventos de um agente específico.
            securedBy: [JWT]
            body:
                application/json: Event[]
            responses:
                200:
                    body:
                        application/json: |
                            {"message": "Eventos alterados com sucesso."}
                401:
                    body:
                        application/json: |
                            {"error": "Você não está autorizado para fazer esta ação."}
                404:
                    body:
                        application/json: |
                            {"error": "Agente não encontrado."}

        delete:
            description: Remoção de mais de um evento de um agente específico.
            securedBy: [JWT]
            body:
                application/json: Event[]
            responses:
                200:
                    body:
                        application/json: |
                            {"message": "Eventos deletados com sucesso."}
                401:
                    body:
                        application/json: |
                            {"error": "Você não está autorizado para fazer esta ação."}
                404:
                    body:
                        application/json: |
                            {"error": "Agente não encontrado."}
/users:

    post:
        description: Adição de um novo usuário.
        securedBy: [JWT]
        body:
            application/json:
                properties:
                    name:
                        type: string
                        maxLength: 50
                    password:
                        type: string
                        maxLength: 50
                    email:
                        type: string
                        maxLength: 254
                    last_login:
                        type: date-only
                example: |
                    {"name": "User Name2",
                    "password": "senha123",
                    "email": "mail@mail.com",
                    "last_login": "2020-07-30"
                    }

        responses:
            201:
                body:
                    application/json:
                        example: |
                            {"user_id": 99}
            
            401:
                body:
                    application/json: |
                        {"error": "Você não está autorizado para fazer esta ação."}

    get:
        description: Retorna todos os usuários.
        securedBy: [JWT]
        responses:
            200:
                body:
                    application/json: User[]
            401:
                body:
                    application/json: |
                        {"error": "Você não está autorizado para fazer esta ação."}
            

    /{id}:
        get:
            description: Busca um usuário específico pelo id.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json: User
                401:
                    body:
                        application/json: |
                            {"error": "Você não está autorizado para fazer esta ação."}
                404:
                    body:
                        application/json: |
                            {"error": "Usuário não encontrado."}

        put:
            description: Alteração de um usuário específico pelo id.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json: |
                            {"message": "Usuário alterado com sucesso."}
                401:
                    body:
                        application/json: |
                            {"error": "Você não está autorizado para fazer esta ação."}
                404:
                    body:
                        application/json: |
                            {"error": "Usuário não encontrado."}

        delete:
            description: Remoção de um usuário específico pelo id.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json:  |
                            {"message": "Usuário removido com sucesso."}
                401:
                    body:
                        application/json: |
                            {"error": "Você não está autorizado para fazer esta ação."}
                404:
                    body:
                        application/json: |
                            {"error": "Usuário não encontrado."}

        
/groups:

    post:
        description: Criação de um novo grupo.
        securedBy: [JWT]
        body:
            application/json:
                properties:
                    name:
                        type: string
                        maxLength: 20
                example:
                    name: "Nome do Grupo 2"
        responses:
            201:
                body:
                    application/json:
                        example: |
                            {"group_id": 57}

            401:
                body:
                    application/json: |
                        {"error": "Você não está autorizado para fazer esta ação."}

    get:
        description: Retorna todos os grupos.
        securedBy: [JWT]
        responses:
            200:
                body:
                    application/json: Group[]
            
            401:
                body:
                    application/json: |
                        {"error": "Você não está autorizado para fazer esta ação."}
            

    /{id}:
        get:
            description: Busca um grupo específico pelo id.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json: Group

                401:
                    body:
                        application/json: |
                            {"error": "Você não está autorizado para fazer esta ação."}
                404:
                    body:
                        application/json: |
                            {"error": "Grupo não encontrado."}

        put:
            description: Alteração de um grupo específico pelo id.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json: |
                            {"message": "Grupo alterado com sucesso."}
                401:
                    body:
                        application/json: |
                            {"error": "Você não está autorizado para fazer esta ação."}

        delete:
            description: Remoção de um grupo específico pelo id.
            securedBy: [JWT]
            responses:
                200:
                    body:
                        application/json: |
                            {"message": "Grupo deletado com sucesso."}
                401:
                    body:
                        application/json: |
                            {"error": "Você não está autorizado para fazer esta ação."}

                404:
                    body:
                        application/json: |
                            {"error": "Grupo não encontrado."}

'''
