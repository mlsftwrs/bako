## Python Coding Standards and Guidelines

This document outlines the coding standards and guidelines for the development of Bako Package. Following these guidelines will ensure consistent, readable, and maintainable code.

**Before we start: It is imperative to read the Zen of Python, run the following code**

```python
>>> import this
```

**Core Principles:**

* **Readability:** Prioritize clear, concise code for easy comprehension (for you and others).
* **Consistency:** Maintain a uniform coding style throughout the project.
* **Maintainability:** Write code that's adaptable and easy to extend as the project evolves.

**Style Guide:**

* **Indentation:** Use 4 spaces for indentation (never tabs).
* **Line Length:** Limit lines to a maximum of 79 characters.
* **Spacing:** Include spaces around operators (except for `**` for exponentiation) and after commas.

**Naming Conventions:**

* **Variables & Functions:** Use lowercase with underscores (snake_case) for descriptive names (e.g., `total_count`, `calculate_area`).
* **Classes:** Use PascalCase for class names (e.g., `MyClass`, `DataProcessor`).
* **Constants:** Use UPPERCASE_SNAKE_CASE for constants (e.g., `PI`, `MAX_VALUE`).

**Comments:**

* Add comments to explain complex code sections or non-obvious logic.
* Use docstrings to document functions and classes thoroughly.

**Code Structure:**

* **Imports:**
    * Organize imports alphabetically.
    * Use absolute imports (e.g., `from module import function`).
    * Avoid wildcard imports (`from module import *`).
* **Functions:**
    * Keep functions focused and modular.
    * Use descriptive names reflecting their purpose.
    * Document functions with docstrings.
* **Classes:**
    * Use clear and descriptive class names.
    * Document classes with docstrings.
* **Formatting:**
    * Use blank lines to separate logical sections of code.
    * Maintain consistent formatting for control flow statements (if, for, etc.).

**Additional Guidelines:**

* **Version Control:** Repo `https://github.com/mlsftwrs/bako.git`.
* **Testing:** Write unit tests to ensure code functionality, TDD is recommended.
* **Linting:** Utilize linters like Pylint, Tox are used for linting.
* **Error Handling:** Use internal Exception Handling module or inherit to write own.
* **Documentation:** Document your code clearly using comments and docstrings. Consider Sphinx for extensive documentation. 
* **Python Version:** Specify the supported Python version(s) for your project.

**Resources:**

* **PEP 8:** The official Python style guide: [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)

**Enforcing Standards:**

* Integrate linters into your build process to catch style violations automatically.

By following these standards, you'll contribute to a well-written, maintainable, and collaborative Python project.