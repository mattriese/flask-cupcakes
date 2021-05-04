"use strict";
const $ul = $("ul");
const $flavor = $("#flavorInput");
const $size = $("#sizeInput");
const $rating = $("#ratingInput");
const $image = $("#imageInput")
const $form = $("form")

async function start() {
    console.log("helloo");
    let response = await axios.get("/api/cupcakes");
    let cupcakes = response.data.cupcakes;
    console.log("axios response=", response);
	console.log("cupcakes= ", cupcakes);
	console.log("ARray.isArray cupcakes= ", Array.isArray(cupcakes));
	console.log("typeof cupcakes[0]= ", typeof cupcakes[0]);
    displayCupcakes(cupcakes);
}


function displayCupcakes(cupcakes){
    for (let cupcake of cupcakes) {
		let {flavor, size, rating, image} = cupcake;
        // let flavor = cupcake.flavor;
        // let size = cupcake.size;
        // let rating = cupcake.rating;
        // let image = cupcake.image;
        $ul.append(`<li>${flavor} cupcakes are ${size} and have a
                    rating of ${rating}. <img src="${image}" width="100">`)
    }
}


async function handleFormSubmit(evt) {
	evt.preventDefault();

	const flavor = $flavor.val()
	const size = $size.val()
	const rating = $rating.val()
	const image = $image.val()

	await submitCupcakeToAPI(flavor, size, rating, image);
}

$form.on("submit", handleFormSubmit);


// makes post request to API with data from form submission for new cupcake
async function submitCupcakeToAPI(flavor, size, rating, image) {
	console.log("submitCupcakeToAPI flavor= ", flavor)
	const response = await axios({
	  url: "/api/cupcakes",
	  method: "POST",
	  data: { "flavor": flavor,
	  		 "size": size,
			 "rating": rating,
			 "image": image }
	});
	newCupcake = response.data.cupcake;
	appendNewCupcake(newCupcake)
	console.log("axios post response.data.cupcake= ", response.data.cupcake)

}

// takes API response on adding new cupcake to database and appends to html
function appendNewCupcake(newCupcake){
	let flavor = newCupcake.flavor;
	let size = newCupcake.size;
	let rating = newCupcake.rating;
	let image = newCupcake.image;
	$ul.append(`<li>${flavor} cupcakes are ${size} and have a
                    rating of ${rating}. <img src="${image}" width="100">`)
}

console.log("I read this")
start();
