use rand::Rng;

/// Generate a random delay within a range (in seconds)
pub fn random_delay(min: u64, max: u64) -> u64 {
    rand::thread_rng().gen_range(min..=max)
}
