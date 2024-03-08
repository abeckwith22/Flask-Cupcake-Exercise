const button = document.querySelector('#submit-button');

const flavor_input = document.querySelector('#flavor');
const size_input = document.querySelector('#size');
const rating_input = document.querySelector('#rating');
const image_input = document.querySelector('#image');

button.addEventListener("click", async function add_new_cupcake(event){
    event.preventDefault(); // should stop the page from refreshing when submitting form

    let flavor_value = flavor_input.value;
    let rating_value = rating_input.value;
    let size_value = size_input.value;
    let image_value = image_input.value;

    let obj = {
        'flavor': flavor_value,
        'rating': rating_value,
        'size': size_value,
        'image': image_value
    };
    // console.log(obj); // debugging

    const request = await axios.post('/api/cupcakes', obj);
    update_page(obj);
})

function update_page(obj){
    flavor_list = document.querySelector('.flavors .flavor-ul');

    new_li = document.createElement('li');
    new_li.innerText = `${obj.flavor}, Rating: ${obj.rating}`;

    flavor_list.append(new_li);
}