# Making HTTP Requests in Python

In Python, you can interact with web services, APIs, and websites by making HTTP requests. This is commonly done using libraries like **`requests`**, which simplifies the process of sending HTTP requests and handling responses. This document will guide you through the process of making HTTP requests in Python.

## Prerequisites
Before you start making HTTP requests in Python, you should have the **`requests`** library installed. If you don't have it installed, you can do so using **`pip`**:

```bash
pip install requests
```

## Making a request with Requests

- ### Import the requests library:
  First, you need to import the requests library in your Python script.

  ```py
    import requests
  ```
- ### Determine the HTTP method: 
  HTTP (Hypertext Transfer Protocol) methods, also known as HTTP verbs, are the standardized actions that define the intended operation to be performed on a resource identified by a URL. HTTP methods determine how a client (e.g., a web browser) interacts with a web server and what action should be taken with the resource identified in the URL. Here are some of the most common HTTP methods and their meanings:

  1. #### GET:
      - Purpose: Retrieve data from the server.
      - Idempotent: Yes (Multiple identical GET requests will have the same result.)
      - Safe: Yes (GET requests should not have any side effects on the server.)
      - Example: Loading a web page, fetching data from a REST API.
  2. #### POST:
        - Purpose: Send data to the server to create a new resource or perform a non-idempotent operation.
        - Idempotent: No (Multiple identical POST requests may create different resources.)
        - Safe: No
        - Example: Submitting a web form, creating a new record in a database.
  3. #### PUT:
        - Purpose: Update an existing resource or create a new resource if it doesn't exist.
        - Idempotent: Yes (Multiple identical PUT requests should have the same result.)
        - Safe: No
        - Example: Updating an existing user's profile.
  4. #### PATCH:
        - Purpose: Partially update an existing resource.
        - Idempotent: Yes (Multiple identical PATCH requests should have the same result.)
        - Safe: No
        - Example: Updating specific fields of a user's profile.
  5. #### DELETE:
        - Purpose: Remove a resource from the server.
        - Idempotent: Yes (Multiple identical DELETE requests will have the same result, but the resource is ultimately removed.)
        - Safe: No
        - Example: Deleting a user account.

- ### Set the URL:
  Specify the URL of the resource you want to interact with.
  ```py
  url = "https://example.com/api/data"
  ```
- ### (Optional) Define request parameters or data:
  Depending on the request type, you may need to include query parameters, request headers, or data in the request.
  ```py
  data = {
    "name": "xxx",
    "userId": 1}```
- ### Send the request:
  Use the appropriate requests method (e.g., requests.get(), requests.post()) to send the request.
  ```py
  response = requests.post(url, data=data)
  ```
- ### Handle the response:
  Once you receive a response, you can access the response data, status code, headers, and more.
  ```py
  if response.status_code == 200:
    # Successful response
    data = response.json()  # Parse JSON response
    print("Response Data:")
    print(data)
  else:
    # Error handling for unsuccessful response
    print(f"Request failed with status code: {response.status_code}")
  ```
  And you can write too
  ```py
  response.raise_for_status()
  data = response.json()
  ```
  <details>
  <summary> Responses HTTP code </summary>
    HTTP response status codes are three-digit codes that indicate the outcome of an HTTP request. These status codes are grouped into different classes, each of which has a specific meaning. Here are some of the most common HTTP response status codes and their meanings:

    **1xx Informational:**

    `100 Continue`: The server has received the initial part of the request, and it's waiting for the client to send the remainder.

    **2xx Successful:**

    `200 OK`: The request was successful, and the server has fulfilled it.

    `201 Created`: The request has been successfully processed, resulting in the creation of a new resource.

    `204 No Content:` The request was successful, but there is no data to return (often used for DELETE requests).

    **3xx Redirection:**

    `301 Moved Permanently:` The requested resource has been moved to a different URL permanently.

    `302 Found (or 303 See Other):` The requested resource is temporarily located at a different URL.

    `307 Temporary Redirect:` Similar to 302, indicating a temporary redirection.

    **4xx Client Errors:**

    `400 Bad Request:` The request is malformed or contains invalid syntax.

    `401 Unauthorized:` The request requires authentication, and the provided credentials are invalid.

    `403 Forbidden:` The server understood the request but refuses to fulfill it (often due to insufficient permissions).

    `404 Not Found:` The requested resource could not be found on the server.

    `405 Method Not Allowed:` The HTTP method used in the request is not allowed for the specified resource.

    **5xx Server Errors:**

    `500 Internal Server Error:` A generic error message indicating that the server encountered an unexpected condition.

    `501 Not Implemented:` The server does not support the functionality required to fulfill the request.

    `503 Service Unavailable:` The server is temporarily unable to handle the request, often due to being overloaded or undergoing maintenance.

    These status codes are an essential part of the HTTP protocol, and they provide information about the outcome of a request, allowing the client to respond appropriately. When making HTTP requests in your code, it's crucial to check the response status code to determine whether the request was successful and how to handle any errors or redirections.
  </details>  
