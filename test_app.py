import unittest
from app import app

class TestFlaskApp(unittest.TestCase):

  def test_hello_route(self):
    """Tests the response of the root route."""
    with app.test_client() as client:
      response = client.get("/")
      self.assertEqual(response.status_code, 200)
      self.assertEqual(response.data.decode(), "Hello from Flask App!")

if __name__ == "__main__":
  unittest.main()
