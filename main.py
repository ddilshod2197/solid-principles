class ContextManager:
    def __enter__(self):
        print("Context manager ni ochish boshlandi")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Context manager ni yopish boshlandi")

with ContextManager() as cm:
    print("Context manager ichida")
```

```python
import contextlib

@contextlib.contextmanager
def context_manager():
    print("Context manager ni ochish boshlandi")
    try:
        yield
    finally:
        print("Context manager ni yopish boshlandi")

with context_manager():
    print("Context manager ichida")
