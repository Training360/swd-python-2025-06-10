FROM python:3.13.3
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["pytest", "-v", "-s", "tests/employees_test.py::test_save"]