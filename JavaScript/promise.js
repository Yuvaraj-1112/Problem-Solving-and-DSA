let availability = true;

function waitInQueue() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {

            if(availability){
                resolve("Halwa successfully purchased");
            }
            else{
                reject("Halwa not purchased");
            }
        }, 1000)
    })
}

function buyHalwa(){
    waitInQueue().then((msg) =>{
        console.log(msg)
    })
    .catch((Error) => {
        console.log(Error);
    })
}

buyHalwa(availability)