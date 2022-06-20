# FastAPI

FastAPI is a modern, high-performance web framework for building APIs with Python based on standard type hints. It has the following key features:

1. Fast to run: It offers very high performance, on par with NodeJS and Go, thanks to Starlette and pydantic.
2. Fast to code: It allows for significant increases in development speed.
3. Reduced number of bugs: It reduces the possibility for human-induced errors.
4. Intuitive: It offers great editor support, with completion everywhere and less time debugging.
5. Straightforward: It’s designed to be uncomplicated to use and learn, so you can spend less time reading documentation.
6. Short: It minimizes code duplication.
7. Robust: It provides production-ready code with automatic interactive documentation.
8. Standards-based: It’s based on the open standards for APIs, OpenAPI and JSON Schema.

# Install FastAPI
$ pip install "fastapi[all]"

# To Run 
$ uvicorn filenem:FastAPI variable --reload <br />
EX : uvicorn main:app --reload

# To Check the Response
Open your browser to http://127.0.0.1:8000

# Imp Topics:
# Query Parameters
In FastAPI, when we declare a function with parameters that are not present as path parameters, they are interpreted as query parameters. <br>
Best practice for RESTful API design is that path params are used to identify a specific resource or resources, while query parameters are used to sort/filter those resources.

EX: <br>
@app.get("/users/{user_id}/items/{item_id}")<br>
async def read_user_item(user_id: int, item_id: str, short: bool = False):<br>
    return something <br>
   
Here, user_id and item_id are path parameters. short is a query parameter.
