use std::collections::HashMap;

fn main() {
    let divs = [(3, "Fizz"), (5, "Buzz"), (7, "Bazz")] // add more divisors here
        .into_iter()
        .collect::<HashMap<_, _>>();

    for n in 0..100 {
        let mut s = String::new();
        for (div, word) in &divs {
            if n % div == 0 {
                s.push_str(word);
            }
        }
        if s.is_empty() {
            s = n.to_string();
        }
        println!("{}", s);
    }
}
