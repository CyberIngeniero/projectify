# Contributing to Projectify! 🤖📦

Thank you for your interest in contributing to Projectify! Whether you're here to report issues, suggest improvements, or contribute code, your help is greatly appreciated. This document provides guidelines and best practices for contributing to the project.

---

## Common Considerations

- **Avoid Redundant Work**: Before starting work on a new feature or bug fix, please check existing issues and projects to avoid duplicating effort.
- **Open an Issue**: For significant changes or new features, please open an issue first to discuss your ideas with the community and ensure alignment.
- **Minimal Changes**: Limit your changes to the necessary lines to avoid conflicts and simplify the review process.
- **Run `pip install -r requirements-dev.txt`**: This ensures you have all the development dependencies, including linters and formatters, to maintain code consistency.
- **Write Tests**: Whenever possible, add tests for your changes. Tests help ensure that new code works as expected and prevent future regressions.

## New Feature

1. **Check Existing Issues**: Ensure there isn't an existing issue or pull request for the feature you want to add.
2. **Open an Issue**: Describe the feature, the files you plan to modify, and any other relevant details.
3. **Community Feedback**: Wait for feedback and approval from the community or maintainers.
4. **Fork the Project**: Fork the repository to your GitHub account.
5. **Create a Branch**: Create a new branch using the naming conventions below.
6. **Write Code and Commit**: Make regular commits following the commit message conventions.
7. **Pull Request**: Submit a pull request to the `main` branch. Use the issue title or a similar one as the pull request title. In the description, link the related issue and use "close #issueNumber" to automatically close the issue upon merging.

## Conventions

### Git Branch Naming

Use the following naming conventions for branches:

- `feat/short-description` for new features
- `fix/short-description` for bug fixes
- `docs/short-description` for documentation improvements
- `chore/short-description` for maintenance tasks
- `refactor/short-description` for code refactoring

> 📘 Example branch naming:
> `feat/add-login-functionality`
> `fix/typo-in-readme`
> `docs/update-contributing-guide`
> `chore/update-dependencies`
> `refactor/improve-code-readability`

### Git Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification:

- Use the present tense ("add feature" not "added feature").
- Use the imperative mood ("move cursor to..." not "moves cursor to...").
- Limit the subject line to 72 characters or less.
- Reference issues and pull requests liberally in the body of the commit message.
- Structure your commit messages as follows:

```plaintext
<type>(<scope>): <short description>
<BLANK LINE>
<optional longer description>
<BLANK LINE>
<optional footer(s)>
```

> 📘 Example commit message:
> feat: add virtual environment setup script
> Adds a script to automate the setup of a virtual environment for the project. This improves the onboarding experience for new contributors and ensures consistency across development environments.
> Closes #123

### Code Quality

Adhere to clean code principles and ensure your code is readable, maintainable, and well-documented.

If you use `VS Code`, consider installing the following extensions:

- **Pylint**: Helps enforce coding standards and detect errors.
- **Python Docstring Generator**: Simplifies the creation of docstrings for your functions and classes.
- **GitLens**: Enhances the Git capabilities within VS Code.

For other IDEs, look for similar extensions to maintain code quality and consistency.

## Running Tests

1. **Install Test Dependencies**: Make sure to install the development dependencies:

```sh
pip install -r requirements-dev.txt
```

2. **Run Tests**: Use `pytest` to run the tests:

```sh
pytest
```

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it to understand the expected behavior in our community.

---

Thank you for contributing to Projectify! Your help is essential in making this project better for everyone.

Happy coding! 🚀
