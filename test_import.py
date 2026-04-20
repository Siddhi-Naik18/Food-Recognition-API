import importlib

for pkg in ("fastapi", "uvicorn", "PIL", "requests", "transformers", "torch", "rapidfuzz"):
    m = importlib.import_module(pkg)
    print(pkg, "ok")
