# E-Commerce Product Search with Elasticsearch

This project is a Django-based search application that utilizes Elasticsearch to provide efficient product search functionality.

## Project Structure

```
ECCOMMERCE_ELASTICSEARCH/
│── ecommerce/
│   │── __init__.py
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│── search_app/
│   │── migrations/
│   │── templates/
│   │   │── search.html
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── models.py
│   │── tests.py
│   │── urls.py
│   │── views.py
│── venv/
│── .env
│── .gitignore
│── db.sqlite3
│── docker-compose.yml
│── Dockerfile
│── manage.py
│── requirements.txt
```

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/ecommerce-elasticsearch.git
   cd ecommerce-elasticsearch
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```sh
   cp .env.example .env
   ```
   Modify the `.env` file with your Elasticsearch host and port.

5. Run database migrations:
   ```sh
   python manage.py migrate
   ```

6. Start Elasticsearch using Docker:
   ```sh
   docker-compose up -d
   ```

7. Run the Django development server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

### Search Products
**Endpoint:** `GET /search/?q=<query>`  
**Description:** Searches for products based on the query.

#### Example Request:
```sh
curl -X GET "http://127.0.0.1:8000/search/?q=shirt"
```

#### Example Response:
```json
{
  "products": [
    {
      "product_id": "12345",
      "product_name": "Cotton Shirt",
      "price": "29.99"
    }
  ]
}
```

## Search Query Enhancements

This project includes a robust Elasticsearch query to improve search accuracy. The query supports:
- **Exact Match (Boosted)**: Prioritizes exact matches.
- **Standard Match (Handles hyphens & spaces)**
- **Fuzzy Matching**: Allows minor spelling mistakes.
- **Prefix Matching**: Enables autocomplete.

## Example Search Queries

Try the following search queries to test:
- `shirt - white` (Handles hyphen variations)
- `Jacke` (Fuzzy match for `Jacket`)
- `Nike` (Exact brand match)
- `runing shoes` (Typo correction for `running shoes`)

## Frontend UI

The frontend is built using Bootstrap for a simple and interactive search interface.

## Running with Docker

To run the application with Docker, use the following commands:
```sh
docker-compose up --build
```

Then access the application at:
```
http://127.0.0.1:8000/
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
