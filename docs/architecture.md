# System Architecture

```mermaid
graph TD
A[User] --> B[API Docs]
B --> C[OpenAPI Spec]
C --> D[Flask API]
D --> E[Response]