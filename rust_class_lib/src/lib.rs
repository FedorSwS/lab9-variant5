use pyo3::prelude::*;

#[pymodule]
fn rust_class_lib(_py: Python<'_>, _: &PyModule) -> PyResult<()> {
    Ok(())
}
