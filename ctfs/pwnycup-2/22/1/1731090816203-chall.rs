use std::io::{self, BufRead};
fn rand_gen(seed: &mut u32) -> u32 {
    *seed = seed.wrapping_mul(1103515245).wrapping_add(12345);
    (*seed >> 16) & 0x7FFF % 0x42
}

fn main() { 
    let mut secret = String::new();
    let stdin = io::stdin();
    // stdin.lock().read_line(&mut secret).unwrap();
    secret = secret.trim().to_string();

    // if secret.len() != 47 {
    //     println!("length of your secret must be 47.");
    //     return;
    // }
    let corrupted = [
        803, 710, 706, 767, 767, 736, 677, 823, 727, 819, 832, 704, 798, 825, 813, 670, 799, 588, 237, 594, 655, 462, 362,681, 820,503,726,710,552, 505, 645,380, 358, 819, 860, 642, 382, 775, 701, 641, 726, 583, 791, 781, 632, 439, 878

    ];

    let mut seed: u32 = 1;
    let mut curr;

    for i in 0..47 {
        curr = rand_gen(&mut seed);
        // let c = secret.chars().nth(i).unwrap() as u32;
        println!("{:?}",((corrupted[i] ^ curr)  / 7) as u32)
    }
    println!("Got it.");
}


// use std::io::{self, BufRead};
// fn rand_gen(seed: &mut u32) -> u32 {
//     *seed = seed.wrapping_mul(1103515245).wrapping_add(12345);
//     (*seed >> 16) & 0x7FFF % 0x42
// }

// fn main() { 
//     let mut secret = String::new();
//     let stdin = io::stdin();
//     stdin.lock().read_line(&mut secret).unwrap();
//     secret = secret.trim().to_string();

//     if secret.len() != 47 {
//         println!("length of your secret must be 47.");
//         return;
//     }
//     let corrupted = [
//         803, 710, 706, 767, 767, 736, 677, 823, 727, 819, 832, 704, 798, 825, 813, 670, 799, 588, 237, 594, 655, 462, 362,681, 820,503,726,710,552, 505, 645,380, 358, 819, 860, 642, 382, 775, 701, 641, 726, 583, 791, 781, 632, 439, 878
//     ];

//     let mut seed: u32 = 1;
//     let mut curr;

//     for i in 0..47 {
//         curr = rand_gen(&mut seed);

//         let c = secret.chars().nth(i).unwrap() as u32;
//         if ((c * 7) ^ curr) != corrupted[i] {
    // corrupted[i] ^ 7
//             println!("Nope.");
//             return;
//         }      
//     }
//     println!("Got it.");
// }