# ⚡ PythonFu: FastAPI

> A friendly and growing collection of practical FastAPI examples, inspired by the [official FastAPI documentation](https://fastapi.tiangolo.com/).

---

## 🚀 What Is This?

**PythonFu: FastAPI** is a sub-project of [PythonFu](https://github.com/peliw/PythonFu), focused on learning and mastering the [FastAPI](https://fastapi.tiangolo.com/) framework.

This project reimplements and builds upon the **official FastAPI examples** by [@tiangolo](https://github.com/tiangolo), the creator of FastAPI, with annotated code and learning notes for beginners and intermediate Python developers.

---

## 📘 Topics Covered (So Far)

✅ The basics:
- FastAPI app structure
- Path parameters & query parameters
- Request bodies with Pydantic models
- Response models and validation

✅ Intermediate:
- Dependency Injection
- Handling errors and status codes
- Using FastAPI with async / await
- Middleware basics
- CORS configuration

✅ Upcoming / In Progress:
- OAuth2 authentication
- Testing FastAPI applications
- Background tasks
- Deployment strategies

> 📚 **Reference**: Content is aligned with the official FastAPI tutorial: [fastapi.tiangolo.com/tutorial](https://fastapi.tiangolo.com/tutorial/)

---

## 🌟 Why FastAPI?

FastAPI is one of the **fastest-growing web frameworks** for Python. Here's why it's awesome:

- 🏎️ **Blazing fast** performance (Starlette + Pydantic)
- 📦 **Type hinting = validation** with Pydantic
- 🔍 **Built-in automatic docs** with Swagger (OpenAPI)
- ⚙️ **Asynchronous support** with async/await
- ✨ **Great developer experience**

> If you're familiar with Flask or Django, FastAPI will feel like a breath of fresh air — with the power of Python 3.10+ typing and modern async.

---

## 🧠 Who Is This For?

- 🐍 Python beginners who want to build APIs
- 🧪 Learners coming from Flask or Django
- 🔧 Backend developers exploring async and microservices
- 🎓 Students and teachers looking for clean examples

This project is structured so you can learn **progressively** and **experiment freely** with working code.

---

## 📌 Disclaimer

This project **borrows and builds on examples from the official FastAPI documentation** under the terms of the MIT License. All credit to [Sebastián Ramírez (@tiangolo)](https://github.com/tiangolo) for creating FastAPI and its amazing learning resources.

---

## 🛠️ How to Use

```bash
# Clone the repo
git clone https://github.com/peliw/PythonFu_FastAPI.git
cd PythonFu_FastAPI

# Create a virtual environment and activate it
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload
