"use strict";

async function start() {
    console.log("helloo")
    let response = await axios.get("/api/cupcakes");
    let cupcakes = response.data.cupcakes
    console.log(response)
    displayCupcakes(cupcakes)
}


function displayCupcakes(cupcakes){
    for (let cupcake in cupcakes) {
        let flavor = cupcake.flavor;
        let size = cupcake.size;
        let rating = cupcake.rating;
        let image = cupcake.image;
        $ul.append(`<li>${flavor} cupcakes are ${size} and have a 
                    rating of ${rating}. <img src="${image}">`)
    }
}
console.log("I read this")
start();