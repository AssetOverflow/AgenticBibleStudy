# Utility functions for the project

PYARROW_AVAILABLE = False
try:
    import pyarrow as pa
    import pyarrow.parquet as pq
    PYARROW_AVAILABLE = True
except ImportError:
    pass

def ensure_pyarrow_available():
    """Ensure that PyArrow is available, or raise an ImportError."""
    if not PYARROW_AVAILABLE:
        raise ImportError("pyarrow is required but not installed. Please install it using 'pip install pyarrow'.")
