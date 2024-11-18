mod scripts;
mod uploader;
mod utils;

use thirtyfour::prelude::*;
use tokio;
use std::error::Error;

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    // Load the script from the text file
    let file_path = "assets/TextInput.txt"; // Path to the input file
    let lines = scripts::load_script(file_path)?;

    if lines.is_empty() {
        println!("No lines loaded from the script. Exiting.");
        return Ok(());
    }

    // Set fixed values for author and who_said_it
    let author = " ";
    let who_said_it = " ";

    // Initialize WebDriver
    let caps = DesiredCapabilities::chrome();
    let driver = WebDriver::new("http://localhost:4444", caps).await?;

    // Upload quotes one by one
    uploader::scheduled_upload(&driver, &lines, 0, author, who_said_it).await?;
    
    println!("Quote bot is running. Press Ctrl+C to stop.");

    // Prevent program from closing
    loop {
        tokio::time::sleep(std::time::Duration::from_secs(1)).await;
    }
}
