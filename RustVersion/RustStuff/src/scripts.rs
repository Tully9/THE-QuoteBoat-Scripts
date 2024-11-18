use std::fs;
use std::error::Error;

/// Load script from a file and return it as a vector of lines
pub fn load_script(file_path: &str) -> Result<Vec<String>, Box<dyn Error>> {
    match fs::read_to_string(file_path) {
        Ok(content) => {
            println!("Script loaded successfully.");
            Ok(content.lines().map(|line| line.to_string()).collect())
        }
        Err(e) => {
            println!("Error loading script: {}", e);
            Err(Box::new(e))
        }
    }
}
