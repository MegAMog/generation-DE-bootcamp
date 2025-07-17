# anastasiia-portfolio
This repo is for personal mini-project and exercises.

## Repository structure
1. *exercises* - folder for exercises, finished during classes
2. *mini-project* - main repository for personal CAFE mini-project.
  - `mini-project/week-*/data` - includes data used for mini-project (if there are any)
  - `mini-project/week-*/notes` - includes week requirements and some personal notes
  - `mini-project/week-*/source` - source code for python CLI app
    Each week includes the completed code for that week’s requirements.
    The last week may still be in progress.
---

## Cafe mini-project

### Project background
This mini project is about building a simple order management console app that uses a relational database to store and manage cafe data:
-products
-couriers information
-orders history
Users can create, view, update, and delete records directly in the database, making the data persistent between runs.

### Client Requirements (milestones)
**Week 1** - Build the basic user interface for your app: display menus, clear the screen, accept user input, and store simple data in lists using functions to keep code tidy.

**Week 2** - Switch to using dictionaries to store detailed order data like customer info and status, preparing for more complex data handling.

**Week 3** - Add courier management to your app and implement saving/loading data from .txt files, keeping file handling separate from display and logic code.

**Week 4** - Refactor products and couriers to use dictionaries, store order items as lists of product indexes, switch to .csv files for persistence.

**Week 5** - Migrate couriers and products data to a database instead of CSV, and update orders to reference couriers and products by unique IDs rather than list indexes.

**Week 6** - Move all data, including orders and order statuses, into the database by creating dedicated tables and refactoring the app to fully rely on database storage.


---

## How to run the app
### 1. Set up database
**1.1 Create Docker container**
```bash
docker-compose up -d
```

>_**Notes:**_
>- _If you want to have database table populated with data use `docker-compose.yml` as it is:_
>```yml
>db:
>  volumes:
>    -./mini-project/week-*/data/cafe_dump.sql:/docker-entrypoint-initdb.d/cafe_dump.sql
>```
>- _If you only want the schema:_
>```yml
>db:
>  volumes:
>  ./mini-project/week-*/data/init.sql:/docker-entrypoint-initdb.d/init.sql
>```

**1.2 Create server and connect to `cafe_db`**
- Log in to **pgAdmin** running in Docker (by default available at: [http://localhost:8888/](http://localhost:8888/)).
- Click on **Add New Server** and fill in the details:
  - **General** tab: use any name for the server.
  - **Connection** tab:
    - **Host name**: `db`
    - **Maintenance database**: `cafe_db`
    - **Username / Password**: as specified in your `.env` file (by default: `postgres` / `postgres`)


### 2. Run the applictaion:
**Simple way to run application:**
  - Go to the `week-*/source/` directory.
  - Run `main.py`
  ```bash
  python3 main.py
  ```

>_**Notes:**_ 
>_Application can run in venv._

<!-- **2.2 Running project with Docker**
1. Build the Docker Image 
```bash
docker build -t anastasiia-miniproject .
```
2. Run the app interactively
```bash
docker run -it anastasiia-miniproject
```
>_**Notes:**_ 
> _The -it flags ensure that the program can read your input and display output like a normal terminal._ -->


### 3. Run unit tests:
To run unit tests use:

```bash
python3 -m pytest -v -s
```


## Project reflection
If I had more time, I would do the following in my project:

1. Database: Separate product_ids from orders by creating a new table to store order product snapshots, or create a special type product_snapshot in the database.
A "basket" = product snapshot = product info (id, name, price) + quantity.

2. Database: Create another entity called customer.
Implement a menu for it and store all customer data in a separate table. Reference this table in the orders table.

3. Unit tests: Add more tests to cover at least all utility functions.
4. Docker: Fix the Dockerfile to run the entire Python app inside Docker.
5. Improve the README.md file.
6. Create a more user-friendly UI.
7. Add more comments throughout the code.


