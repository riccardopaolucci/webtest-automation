![CI](https://github.com/riccardopaolucci/webtest-automation/actions/workflows/ci.yml/badge.svg)

# 🧪 WebTest Automation Suite

Automated web testing framework using **Selenium**, **Pytest**, and **pytest-html** — built to demonstrate modern test automation practices and CI/CD readiness.

---

## 📅 Day 1 – Project Setup & First Working Test

### ✅ Deliverables

- Created public GitHub repo: **webtest-automation**
- Configured Python virtual environment with required packages
- Verified environment with a simple sanity test
- Implemented first Selenium test (Wikipedia homepage)
- Added `conftest.py` fixture for reusable browser setup
- Generated HTML test report (`report.html`)
- Committed and pushed all files to GitHub

---
## 📅 Day 2 – Build Page Object Model & Multi-Site Tests

### ✅ Deliverables

- Implemented Page Object Model (POM) for scalable UI automation
- Added tests for:
  - Wikipedia search flow
  - Negative login validation (Herokuapp)
- Introduced parameterisation using `pytest.mark.parametrize`
- Verified parallel execution with `pytest-xdist`
- Configured HTML reporting via `pytest.ini`


### ⚙️ How to Run


```bash
pytest -n auto -v
```

---
## 📅 Day 3 – HTML Reporting & API Test Integration

### ✅ Deliverables

- Added HTML test reporting using `pytest-html`
- Confirmed successful generation of `report.html` for every local run
- Added `report.html` to `.gitignore` to prevent committing generated artifacts
- Created Postman collection for GitHub Users API (`https://api.github.com/users/octocat`)
- Added 2 API test cases:
  - Status code validation
  - JSON field validation
- Exported collection as `api_tests.json` and added it to project root
- Installed Newman and verified API tests run correctly from terminal

---
## 📅 Day 4 – CI/CD Pipeline (GitHub Actions, Artifacts & Security)

### ✅ Deliverables

- Added GitHub Actions CI workflow (`ci.yml`)
- Configured pipeline to run on:
  - Pushes to `main`
  - Pull requests to `main`
  - Nightly scheduled run (00:00 UTC)
- Installed Python + Node environments inside CI
- Ran Selenium UI tests using Pytest with HTML reporting
- Ran Postman API tests using Newman with HTML reporting
- Uploaded CI artifacts:
  - `pytest-report`
  - `newman-report`
- Added automated Python dependency audit (`pip-audit`)
- Enabled GitHub security features:
  - CodeQL analysis
  - Dependabot alerts & security updates
  - Secret scanning
- Added CI badge to the README
- Committed and pushed all changes to activate CI

### ⚙️ How to Run

```bash
pytest -n auto --html=report.html --self-contained-html
newman run api_tests.json
```
---
# 📅 Day 5 – Dockerisation, Stability Improvements & Professional README

## ✅ Deliverables

- **Created full Dockerfile** capable of running Selenium UI tests + Newman API tests in one container  
- **Installed dependencies inside container:** Python 3.11, Node 20, Chromium, Chromedriver, Newman  
- **Successfully built and ran the Docker container locally** with all tests passing headlessly  
- **Added Chrome headless stability flags** for Docker execution  
- **Implemented explicit waits and `safe_find()` retry logic** in Page Object Model (removing flaky tests)  
- **Added Docker smoke test job to CI workflow** for full pipeline compatibility  
- **Updated README** with final project documentation, badges, and test instructions  
- **Committed and pushed all files to GitHub**

---

## 🛠️ Tech Stack

- **Languages:** Python 3.11 (3.10+ compatible), Node.js 20 (for Newman)
- **Test Frameworks:** Pytest, Selenium WebDriver
- **Test Utilities:** WebDriverManager, pytest-html, pytest-xdist
- **API Testing:** Postman collections, Newman CLI
- **CI/CD & Security:** GitHub Actions, pip-audit, CodeQL, Dependabot, secret scanning
- **Containerisation:** Docker (Chromium + Chromedriver headless setup)
- **Version Control:** Git & GitHub

---

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/riccardopaloucci/webtest-automation.git
   cd webtest-automation
   ```
