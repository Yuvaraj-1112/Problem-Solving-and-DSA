let availability = false;

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

async function buyHalwa(){
  try{
      let res = await waitInQueue()
  console.log(res)
  }
  catch(Error){
    console.log(Error);
    
  }

}

buyHalwa(availability)