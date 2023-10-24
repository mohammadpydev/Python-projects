# Making HTTP Requests in Python

![Requests Python Logo](Requests_Python_Logo.png)

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
    "userId": 1} 
    ```
- ### Send the request:
  Use the appropriate requests method (e.g., requests.get(), requests.post()) to send the request.
  ```py
  response = requests.post(url, params=data)
  # You can see that the URL has been correctly encoded by printing the URL:
  print(response.url)
  # https://example.com/api/data?name=xxx&userId=1
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

## Handling Response Content

- ### Handling JSON Response:
  To handle a JSON response, you can use the `.json()` method provided by the requests library. It automatically parses the JSON response into a Python dictionary.

  ```py
  import requests

  url = "https://jsonplaceholder.typicode.com/posts/1"
  response = requests.get(url)

  if response.status_code == 200:
      # Parse JSON response
      data = response.json()
      print("JSON Response:")
      print(data)
  else:
      print(f"Request failed with status code: {response.status_code}")

  ```

- ### Handling Binary Response:

  To handle binary content, such as downloading an image or a file, you can use the `.content` attribute of the response, which returns the response content as bytes.

  ```py
  import requests

  url = "https://example.com/some-image.jpg"
  response = requests.get(url)

  if response.status_code == 200:
      # Access binary content
      binary_data = response.content
      with open("downloaded_image.jpg", "wb") as file:
          file.write(binary_data)
      print("Binary data saved as downloaded_image.jpg")
  else:
      print(f"Request failed with status code: {response.status_code}")

  ```
- ### Handling Text Response:

  To handle text content, you can use the `.text` attribute of the response, which returns the response content as a string.

  ```py
  import requests

  url = "https://example.com/some-text-file.txt"
  response = requests.get(url)

  if response.status_code == 200:
      # Access text content
      text_data = response.text
      print("Text Response:")
      print(text_data)
  else:
      print(f"Request failed with status code: {response.status_code}")

  ```

  > :bulb: **Tip:** Depending on the response content type and your application's needs, you can use the appropriate method to work with JSON, binary data, or text. Make sure to check the Content-Type header in the response to ensure you are handling the content correctly.
  >
  <details>
    <summary> Check the Content-Type header to your code: </summary>
      You can check the Content-Type header in the response using the headers attribute of the response object in the requests library. Here's how you can do it:

      ```py
        import requests

      url = "https://example.com/some-resource"
      response = requests.get(url)

      if response.status_code == 200:
          content_type = response.headers.get('Content-Type')
          if content_type is not None:
              print(f"Content-Type: {content_type}")
          else:
              print("Content-Type header not found in the response.")
      else:
          print(f"Request failed with status code: {response.status_code}")
      ```

  </details>

## Set custom headers in an HTTP request
  You can set custom headers in an HTTP request made using the requests library in Python by passing a dictionary with the headers you want to include as the headers parameter. Here's how to set header values in a request:
  ```py
  import requests

url = "https://example.com/some-resource"

# Define custom headers in a dictionary
headers = {
    "User-Agent": "MyCustomUserAgent/1.0",
    "Authorization": "Bearer YourAccessToken",
    "Content-Type": "application/json",
}

# Make the request with custom headers
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Process the response here
    print("Request successful")
else:
    print(f"Request failed with status code: {response.status_code}")

  ```
  In this example, we set three custom headers: "User-Agent", "Authorization", and "Content-Type". These headers can be used to identify your application, provide authentication tokens, or specify the content type of the request.

You can customize the headers to meet the specific requirements of the API or service you are interacting with. Just include the desired headers in the headers dictionary when making the request.

## Timeouts
The timeout parameter in the requests library allows you to set both the connection timeout and the read timeout for an HTTP request. You can specify a single timeout value or a tuple with two values to set both timeouts. Here's how to use the timeout parameter:

 - ### Single Timeout Value:
    When you provide a single timeout value, it sets both the connection timeout and the read timeout to the same value. If either the connection or the response doesn't occur within this time, a timeout exception is raised.
    ```py
    # A single timeout value of 10 seconds
    response = requests.get(url="https://example.com/some-resource", timeout=10)  
    ```
 - ### Tuple with Two Timeout Values:
    You can provide a tuple with two values to set different timeouts for the connection and the read. The first value is the connection timeout, and the second value is the read timeout. This allows you to specify different time limits for establishing a connection and for receiving the response.
    ```py
    # Connection timeout of 5 seconds, read timeout of 10 seconds
    response = requests.get(url, timeout=(5, 10))  
   ```
## Proxies
  If you need to use a proxy, you can configure individual requests with the proxies argument to any request method:

  ```py
  import requests

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}

requests.get('http://example.org', proxies=proxies)
  ```
  
## ***References***  
[Requests: HTTP for Humans™](https://web.archive.org/web/20220809124220/https://requests.readthedocs.io/en/latest/
"Requests is an elegant and simple HTTP library for Python, built for human beings.")