# Digit Recognition API

This project provides a simple REST API that uses a pre-trained machine learning model to recognize handwritten digits (0-9) from the [scikit-learn Digits dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html). It is built with FastAPI and Docker for easy deployment.

---

##  Project Structure

```bash
digit-recognition-api/
├── app/
│   ├── main.py              # FastAPI app with prediction route
│   └── model.py             # Loads model and prediction logic
├── digit_model/
│   └── digit_model.pkl            # Trained scikit-learn model
├── test/
│   └── test_model.pkl            # test model
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker build file
├── .github/workflows/
│   └── ci.yml               # GitHub Actions for CI to train, test, build and push to docker hub
│   └── cd.yml               # GitHub Actions for CD to to depkoy the docer cobtiabers to AWS EC2
```

---

##  Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Train the Model (Optional)

If you need to retrain the model:

```python
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
import joblib

X, y = load_digits(return_X_y=True)
model = LogisticRegression(max_iter=10000)
model.fit(X, y)
joblib.dump(model, "model/model.pkl")
```

---

##  Running the API

### Using Uvicorn Locally

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8001
```

### Using Docker

```bash
docker build -t digits-api:latest .
docker run -d -p 8001:8001 --name digits-api digits-api:latest
```

---

## API Endpoints

### POST `/predict`

**Request:**

```json
{
  "image": [64 float values]
}
```

**Response:**

```json
{
  "prediction": 3
}
```

### Sample cURL Request

```bash
curl -X POST http://localhost:8001/predict \
  -H "Content-Type: application/json" \
  -d '{"image": [0, 0, 10, 16, 15, 4, 0, 0, 0, 4, 16, 16, 16, 6, 0, 0, 0, 8, 15, 12, 15, 8, 0, 0, 0, 4, 6, 0, 15, 8, 0, 0, 0, 0, 0, 0, 15, 8, 0, 0, 0, 0, 0, 0, 15, 8, 0, 0, 0, 0, 1, 4, 16, 8, 0, 0, 0, 0, 13, 16, 13, 2, 0, 0]}'
```

---

##  Deployment Steps

- **CI/CD** via GitHub Actions: Auto train, test, build, and push image to Docker Hub
- **Deployed on AWS EC2** using Docker
- **Secured via AWS API Gateway** (optional)

---

##  FastAPI Interactive Docs

Once the app is running:

- Swagger UI: `http://localhost:8001/docs`
- ReDoc: `http://localhost:8001/redoc`

---

## License

MIT License

---

Feel free to contribute, suggest improvements, or request more features!

