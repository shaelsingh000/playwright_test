# 🚀 Playwright Automation Framework (Python)

A production-ready **end-to-end test automation framework** built using **Playwright + Pytest**, fully integrated with **CI/CD on GitLab**, and live reporting using **Allure Reports hosted on GitLab Pages**.

---

## 🔗 Live Demo

👉 **Allure Report (Latest Run)**
https://playwright-tests-91d4df.gitlab.io/

---

## 📌 Key Features

* ✅ Playwright with Python (modern UI automation)
* ✅ Pytest-based scalable framework
* ✅ Page Object Model (POM) design
* ✅ Parallel execution using `pytest-xdist`
* ✅ Allure Reporting (rich UI reports)
* ✅ GitLab CI/CD pipeline integration
* ✅ GitLab Pages for report hosting
* ✅ Dockerized test execution
* ✅ Test tagging & selective execution
* ✅ Automatic screenshots on failure
* ✅ Video recording for debugging
* ✅ Allure history & trend tracking

---

## 🧱 Tech Stack

* **Automation**: Playwright (Python)
* **Test Runner**: Pytest
* **Reporting**: Allure
* **CI/CD**: GitLab CI
* **Containerization**: Docker
* **Language**: Python 3.10

---

## 📂 Project Structure

```
playwright-ecommerce/
│── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_api_health.py
│
│── pages/
│   ├── base_page.py
│   ├── login_page.py
│   └── dashboard_page.py
│
│── fixtures/
│   └── browser_fixture.py
│
│── utils/
│   ├── config.py
│   └── logger.py
│
│── data/
│   └── test_data.json
│
│── requirements.txt
│── pytest.ini
│── Dockerfile
│── .gitlab-ci.yml
```

---

## ⚙️ Setup & Execution

### 1️⃣ Install Dependencies

```
pip install -r requirements.txt
playwright install
```

---

### 2️⃣ Run Tests

```
pytest --alluredir=allure-results
```

---

### 3️⃣ Generate Report (Local)

```
allure serve allure-results
```

---

## 🧪 Test Tagging & Selective Execution

Run specific test groups:

```
pytest -m smoke
pytest -m regression
pytest -m "smoke and not slow"
```

---

## 🐳 Docker Execution

Build Image:

```
docker build -t playwright-tests .
```

Run Tests:

```
docker run playwright-tests
```

---

## 🔄 CI/CD Pipeline

Pipeline Stages:

* **Test Stage** → Executes Playwright tests
* **Report Stage** → Generates Allure report
* **Pages Stage** → Publishes report to GitLab Pages

---

## 📊 Allure Report Features

* 📈 Trend history (previous runs)
* 📸 Screenshots on failure
* 🎥 Video recording
* 🧾 Detailed logs & steps
* 📊 Test categorization (smoke/regression)

---

## 🖼️ Sample Report

👉 Live Report: https://playwright-tests-91d4df.gitlab.io/#behaviors

*(Add screenshot here for better visibility)*

---

## 🏆 Why This Project?

This project demonstrates:

* Real-world automation framework design
* CI/CD integration skills
* Debugging via screenshots & videos
* Scalable test architecture
* Industry-level reporting and visibility

---

## 👨‍💻 Author

**Shael Singh**

* GitLab: https://gitlab.com/shaelsingh000
* GitHub: https://github.com/shaelsingh000

---

## ⭐ Future Improvements

* Slack/Email notifications on failure
* Cloud execution (GCP / Kubernetes)
* API + UI combined test strategy
* Performance testing integration

---

## 💡 Note

This framework is designed to simulate a **real production-level QA automation setup** with CI/CD and reporting — suitable for enterprise environments.

---
