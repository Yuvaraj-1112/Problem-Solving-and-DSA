function prime(n){
    if(n > 3 && (n % 2 == 0)|| (n % 3 == 0)){
        return "Not prime number"
    }
    else{
        for(let i = 5; i*i <= n; i+=6){

            if(n % i == 0 || n % i+2 == 0){
                return "Not prime number"
            }
        }
        return "Prime number"
    }
}

console.log(prime(23))