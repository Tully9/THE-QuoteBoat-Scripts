use thirtyfour::prelude::*;
use tokio::time::{sleep, Duration};
use std::error::Error;
use crate::utils;

/// Upload a single quote to the website
pub async fn upload_quote(
    driver: &WebDriver,
    quote: &str,
    context: &str,
    author: &str,
    who_said_it: &str,
) -> Result<(), Box<dyn Error>> {
    driver.goto("https://ise-quoteboat.vercel.app/").await?;
    println!("Navigated to the website.");

    // Locate form fields and buttons
    let quote_field = driver.find_element(By::Id("quote")).await?;
    let context_field = driver.find_element(By::Id("context")).await?;
    let author_field = driver.find_element(By::Id("author")).await?;
    let who_said_it_field = driver.find_element(By::Id("sayer")).await?;
    let submit_button = driver.find_element(By::Css("button[type='submit']")).await?;

    // Fill in the fields with small delays
    quote_field.send_keys(quote).await?;
    sleep(Duration::from_secs(1)).await;

    context_field.send_keys(context).await?;
    sleep(Duration::from_secs(1)).await;

    author_field.send_keys(author).await?;
    sleep(Duration::from_secs(1)).await;

    who_said_it_field.send_keys(who_said_it).await?;
    sleep(Duration::from_secs(1)).await;

    println!("Submitting the form...");
    submit_button.click().await?;
    sleep(Duration::from_secs(1)).await;

    println!("Form submitted. Waiting for a short delay...");
    sleep(Duration::from_secs(utils::random_delay(1, 2))).await;

    Ok(())
}

/// Upload quotes one by one with scheduling
pub async fn scheduled_upload(
    driver: &WebDriver,
    lines: &[String],
    mut current_line_index: usize,
    author: &str,
    who_said_it: &str,
) -> Result<(), Box<dyn Error>> {
    while current_line_index < lines.len() {
        let quote = lines[current_line_index].trim();
        println!("Uploading quote: {}", quote);

        upload_quote(driver, quote, "", author, who_said_it).await?;
        println!("Quote uploaded successfully!");

        current_line_index += 1;
        println!("Next index will be: {}", current_line_index);

        if current_line_index < lines.len() {
            sleep(Duration::from_secs(2)).await; // Wait 2 seconds between uploads
        } else {
            println!("All quotes have been uploaded!");
            break;
        }
    }
    Ok(())
}
