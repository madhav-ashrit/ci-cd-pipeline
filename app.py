from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
  """Returns a greeting message."""
  return "Hello from Flask App!"

if __name__ == "__main__":
  app.run(debug=True)
