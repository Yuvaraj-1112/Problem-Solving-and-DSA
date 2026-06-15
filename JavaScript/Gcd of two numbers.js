function Gcd(m,n){
    let temp = 0;
    let temp2 = 0;
    if(m < n){
        temp = m;
        m = n;
        n = temp;
    }

    while(m % n != 0){
        temp2 = m;
        m = n;
        n = temp%n;
    }
    return n
}

console.log(Gcd(7,14))