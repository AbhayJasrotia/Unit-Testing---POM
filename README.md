# Selenium Automation Project - Login and Logout

🚀 A small Selenium automation project to perform login and logout actions on the [OrangeHRM Demo Site](https://opensource-demo.orangehrmlive.com/).

---

## 📂 Project Structure

```
Selenium/
├── Unit/
│   ├── Locators.py
│   ├── Pages/
│   ├── Tests/
├── Reports/
├── README.md
```

- **Locators**: All element locators.
- **Pages**: Page Object Model (POM) classes.
- **Tests**: Unittest-based test scripts.
- **Reports**: Automatically generated HTML reports after test run.

---

## 📸 Preview

*(Coming Soon - Small video demo will be added here!)*

---

## 🧪 How to Run

1. Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
```

2. Install required Python libraries:

```bash
pip install selenium
pip install html-testRunner
```

3. Run the test:

```bash
python -m Unit.Tests.test_login_logout
```

4. After running, HTML test report will be generated inside `Reports/` folder.

---

## 📑 HTML Report

- After execution, a detailed HTML report will be available at:
  
  ```
  Selenium/Reports/
  ```

---

## 📚 Technologies Used

- Python 3.12
- Selenium WebDriver
- Unittest Framework
- HtmlTestRunner (for HTML reports)

---

## 🌟 Future Plans

- Add multiple test cases (like Add Employee, Search, Delete)
- Create a short video demonstration
- Add Docker support

---

# 🙏 Thanks for visiting!
