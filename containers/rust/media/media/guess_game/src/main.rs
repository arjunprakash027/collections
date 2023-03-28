use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    let secret_number = rand::thread_rng().gen_range(1..=50);
    let mut count = 0;
    println!("enter your guess from 1 to 50:");
    loop
    {
        
    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("line not read");

    let guess: u32 = guess.trim().parse().expect("enter a number please!");
    count+=1;

    match guess.cmp(&secret_number){
        Ordering::Less => {
            println!("--------------");
            println!("lesser");
            println!("--------------");
        }
        Ordering::Greater => 
        {
            println!("--------------");
            println!("greater");
            println!("--------------");
        }
        Ordering::Equal => {
            println!("yay you won");
            println!("you got it right in {count} steps");
            break;
        }
    }
    }
    //println!("secret number is {secret_number}");
}
