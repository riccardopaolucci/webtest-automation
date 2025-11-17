🎥 **Demo:** [Watch 4 minute and 28 seconds walkthrough](https://www.loom.com/share/c323ab4b38174621ab3ef721d0714a69)

# 🧪 WebTest Automation Suite

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Docker](https://img.shields.io/badge/Containerized-Yes-green)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)
![CI](https://github.com/riccardopaolucci/webtest-automation/actions/workflows/ci.yml/badge.svg)

Automated end-to-end testing framework using **Selenium**, **Pytest**, **Newman**, **Docker**, and **GitHub Actions**.
Built to demonstrate a **production-ready** automation pipeline including UI tests, API tests, CI/CD, reporting, and containerisation.

---

# 🚀 Features

## 1. **UI Automation (Selenium + Pytest)**

- Reusable browser fixture (`conftest.py`)
- Page Object Model (POM) architecture
- UI test coverage for:
  - Wikipedia search flow
  - Herokuapp login validation
- Parallel execution via **pytest-xdist**
- HTML reporting via **pytest-html**

---

## 2. **API Testing (Postman + Newman)**

- GitHub Users API Postman collection (`api_tests.json`)
- Status code + JSON schema validation tests
- Newman integrated into local runs **and** CI workflow

---

## 3. **Reporting**

Generates HTML reports for:

- Selenium UI tests → `report.html`
- Newman API tests → `newman-report.html`

CI artifacts automatically uploaded on every pipeline run.

---

## 4. **CI/CD Pipeline (GitHub Actions)**

Triggers on:

- Push to `main`
- Pull requests
- Nightly cron run (00:00 UTC)

Includes:

- Python + Node setup
- Selenium UI tests (headless)
- Newman API tests
- HTML report uploads
- Dependency audit (`pip-audit`)
- CodeQL analysis
- Dependabot alerts
- Secret scanning
- CI status badge

---

## 5. **Dockerised Test Environment**

Single Docker image that runs:

- **Selenium tests** (Chromium + Chromedriver)
- **Newman API tests**

Installed inside container:

- Python 3.11
- Node 20
- Chromium + drivers
- Stability flags for headless execution

Local smoke test verifies the full suite inside Docker.

---

# 🛠 Tech Stack

**Languages:** Python 3.11, Node 20
**Frameworks:** Pytest, Selenium WebDriver
**Tools:** WebDriverManager, Newman, pytest-xdist, pytest-html
**CI/CD:** GitHub Actions, pip-audit, CodeQL, Dependabot
**Containerisation:** Docker
**Reports:** pytest-html, newman-reporter-htmlextra

---
# ⚙️ Tech Decisions Explained

| **Decision**                          | **Why It Matters (Engineering Reasoning)**                                                                                 |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Python + Pytest**                   | Clean syntax, powerful plugins, enterprise adoption. Fast to write, easy to scale, ideal for CI/CD automation.                   |
| **Selenium with POM architecture**    | Page Object Model makes tests maintainable, reduces duplication, and mirrors real-world automation frameworks used in companies. |
| **pytest-xdist (Parallel Execution)** | Distributes tests across CPU cores →**up to 70% faster pipelines** , identical to real DevOps environments.               |
| **pytest-html**                       | Produces visual, shareable reports for QA/DevOps teams—essential for sprint reviews and debugging.                              |
| **Postman + Newman**                  | Standard API testing workflow in industry; enables contract testing and integrates naturally with CI.                            |
| **GitHub Actions CI/CD**              | Runs tests automatically on every push/PR + nightly schedule, proving the project is stable and deployable.                      |
| **Docker**                            | Guarantees identical test environment across machines; mirrors how tests run in staging/prod.                                    |
| **pip-audit + CodeQL + Dependabot**   | Security standards used by professional teams—scans vulnerabilities, dependencies, and code quality continuously.               |

---
# 📂 Project Structure

```text
webtest-automation/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── pages/
│   ├── login_page.py
│   └── wikipedia_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_open_site.py
│   ├── test_setup_check.py
│   └── test_wikipedia.py
│
├── utils/
│   ├── init.py
│   └── waits.py
│
├── api_tests.json
├── conftest.py
├── Dockerfile
├── LICENSE
├── pytest.ini
├── README.md
├── report.html
└── requirements.txt
```

---

# ▶️ How to Run Tests Locally

## **UI Tests**

```bash
pytest -n auto --html=report.html --self-contained-html
```

## **API Tests**

```bash
newman run api_tests.json
```

---

# ▶️ How to Run via Docker

```bash
docker build -t webtest .
docker run --rm webtest
```
