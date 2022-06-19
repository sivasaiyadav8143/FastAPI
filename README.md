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
