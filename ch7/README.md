# Manhattan Distance API

A microservice that calculates the Manhattan distance between two DataFrames provided as JSON input.


## Running the app
In your terminal, navigate to the `ch7` directory and run the following command:

```bash
python app.py
```

This starts a Flask server on http://localhost:5000

### Sample request
You can test the API using `curl` or any HTTP client. Here's an example using `curl`:

```bash
curl -X POST http://127.0.0.1:5000/manhattan \
  -H "Content-Type: application/json" \
  -d '{"df1": [[1, 2], [3, 4]], "df2": [[2, 0], [1, 3]]}'
```

### Sample response

>{
  "distance": 7.0
}

## Running with Docker

To run the application in a Docker container, follow these steps:
build the Docker image:

```bash
docker build -t manhattan-distance-api .
```

Run the Docker container:

```bash
docker run -p 5000:5000 manhattan-distance-api
```

You can then access the API at http://127.0.0.1:5000

# Todos
- [ ] Add test cases
- [ ] Add logging
- [ ] Add error handling
- [ ] Add documentation