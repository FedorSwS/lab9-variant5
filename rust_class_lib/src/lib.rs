use pyo3::prelude::*;

#[pyclass]
struct DataProcessor {
    name: String,
    processed_count: u32,
}

#[pymethods]
impl DataProcessor {
    #[new]
    fn new(name: String) -> Self {
        DataProcessor {
            name,
            processed_count: 0,
        }
    }
    
    fn process(&mut self, data: String) -> String {
        self.processed_count += 1;
        format!("[{}] Processed: {}", self.name, data)
    }
    
    fn get_count(&self) -> u32 {
        self.processed_count
    }
    
    fn reset(&mut self) {
        self.processed_count = 0;
    }
    
    fn __repr__(&self) -> String {
        format!("DataProcessor(name='{}', count={})", self.name, self.processed_count)
    }
}

#[pyfunction]
fn fast_compute(numbers: Vec<i64>) -> i64 {
    numbers.iter().map(|x| x * x).sum()
}

#[pymodule]
fn rust_class_lib(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_class::<DataProcessor>()?;
    m.add_function(wrap_pyfunction!(fast_compute, m)?)?;
    Ok(())
}
