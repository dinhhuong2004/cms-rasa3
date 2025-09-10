import os

# Cấu trúc thư mục & file
structure = {
    "rasa-cms": {
        "backend": {
            "app": {
                "core": ["config.py", "security.py", "__init__.py"],
                "api/v1": [
                    "auth.py", "intents.py", "entities.py", "responses.py",
                    "stories.py", "config.py", "training.py", "models.py", "conversations.py", "__init__.py"
                ],
                "services": ["yaml_converter.py", "rasa_client.py", "train_service.py", "__init__.py"],
                "db": {
                    "models": ["__init__.py"],
                    "crud": ["__init__.py"],
                    "__files__": ["mongo.py", "__init__.py"]
                },
                "schemas": ["__init__.py"],
                "workers": ["__init__.py"],
                "tests": ["__init__.py"],
                "__files__": ["main.py", "__init__.py"]
            },
            "__files__": ["Dockerfile", "requirements.txt"]
        },
        "frontend": {
            "src": {
                "pages": ["index.tsx", "login.tsx", "__init__.py"],
                "components": ["__init__.py"],
                "services": ["__init__.py"],
                "store": ["__init__.py"],
                "utils": ["__init__.py"]
            },
            "__files__": ["Dockerfile", "package.json", "tailwind.config.js"]
        },
        "rasa": {
            "data": ["nlu.yml", "stories.yml", "rules.yml"],
            "models": [],
            "actions": ["actions.py"],
            "__files__": [
                "domain.yml", "config.yml",
                "endpoints.yml", "credentials.yml",
                "Dockerfile", "requirements.txt"
            ]
        },
        "infra": {
            "scripts": ["__init__.py"],
            "__files__": ["docker-compose.yml", "nginx.conf"]
        },
        "__files__": ["README.md"]
    }
}


def create_structure(base, struct):
    for name, content in struct.items():
        path = os.path.join(base, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            # xử lý thư mục có __files__
            if "__files__" in content:
                for f in content["__files__"]:
                    open(os.path.join(path, f), "w").close()
                del content["__files__"]
            create_structure(path, content)
        elif isinstance(content, list):
            os.makedirs(path, exist_ok=True)
            for f in content:
                open(os.path.join(path, f), "w").close()


if __name__ == "__main__":
    base_dir = os.getcwd()  # Thư mục hiện tại
    create_structure(base_dir, structure)
    print("✅ Project structure created successfully!")
