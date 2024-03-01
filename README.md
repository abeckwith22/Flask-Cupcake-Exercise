## Flask Cupcake Exercise

#### Part 0: Set Up

- [x] Make a virtual environment and install the dependencies
- [x] Make your project a Git repo.

#### Part 1: Cupcake Model

- [x] Create ***Cupcake*** model in ***models.py***
- [x] It should have the following parameters:
  - [x] ***id***: a unique primary key that is an auto-incrementing integer
  - [x] ***flavor***: a not-nullable text column
  - [x] ***size***: a not-nullable text column
  - [x] ***rating***: a not-nullable column that is a float
  - [x] ***image***: a non-nullable text column. If an image is not given, default to `https://tinyurl.com/demo-cupcake`
- [x] Make a database called ***cupcakes***
- [x] Once you've made this, you can run our ***seed.py*** file to add a few sample cupcakes to your database.

#### Part 2: Listing, Getting & Creating Cupcakes

- [ ] Make routes for the following
  - [x] **GET** `/api/cupcakes`: Get data about all cupcakes. Respond with JSON like `{cupcakes: [(id, flavor, size, rating, image), ...]}`. The values should come from each cupcake instance.
  - [x] **GET** `/api/cupcakes/[cupcake-id]`: Get data about a single cupcake. Respond with JSON like: `{cupcake: (id, flavor, size, rating, image)}`. This should raise a 404 if the cupcake cannot be found.
  - [x] **POST** `/api/cupcakes`: Create a cupcake with flavor, size, rating, and image data from the body of the request. Respond with JSON like: `{cupcake: {id, flavor, size, rating, image}}`.
  - [ ] Test that these routes work in Insomnia.

#### Part 3: Update & Delete Cupcakes

- [ ] Make routes for the following:
- [ ] **PATCH** `/api/cupcakes/[cupcake-id]`: Update a cupcake with the id passed in the URL and flavor, size, rating, and image data from the body of the request. you can always assume that the entire cupcake object will be passed to the backend. This should riase a 404 if the cupcake connot be this: `{cupcake: {id, flavor, size, rating, image}}`.
- [ ] **DELETE** `/api/cupcakes/[cupcake-id]`: This should raise a 404 if the cupcake cannot be found. Delete cupcake with the id passed in the URL. Respond with JSON like `{message: "deleted"}`.
- [ ] Test these routes in Insomnia.

#### Part 4: Write More Tests :(

- [ ] Add tests for the PATCH and DELETE routes.

#### Part 5: Start of Front-end

- [ ] Make this route:
  - [ ] **GET** `/`: This should return an HTML page *(via **render_template**)*. This page should be entirely static (the route should just render the template, without providing any information on cupcakes in the database). It should simply show having an empty list where cupcakes should appear and a form where new cupcakes can be added.
- [ ] Write JavaScript *(using axios and jQuery)* that:
  - [ ] Queries the API to get the cupcakes and adds to the page
  - [ ] Handles form submission to both let the API know about the new cupcake and updates the list on the page to show it.

*Note: You do not need to use WTForms to make this form; this is a possibility in the further study.)*
