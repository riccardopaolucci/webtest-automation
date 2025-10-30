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

## 🛠️ Tech Stack

- **Language:** Python 3.10 +
- **Frameworks:** Pytest, Selenium
- **Tools:** WebDriverManager, pytest-html
- **Version Control:** Git & GitHub

---

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/riccardopaloucci/webtest-automation.git
   cd webtest-automation
   ```
