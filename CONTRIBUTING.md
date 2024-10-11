# Contributing to the Zip Benchmarking Project

First off, thank you for considering contributing to the Zip Benchmarking Project! It's people like you that make this project such a great tool.

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report. Following these guidelines helps maintainers and the community understand your report, reproduce the behavior, and find related reports.

- Use a clear and descriptive title for the issue to identify the problem.
- Describe the exact steps which reproduce the problem in as many details as possible.
- Provide specific examples to demonstrate the steps.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion, including completely new features and minor improvements to existing functionality.

- Use a clear and descriptive title for the issue to identify the suggestion.
- Provide a step-by-step description of the suggested enhancement in as many details as possible.
- Provide specific examples to demonstrate the steps or point out the part of the project where the enhancement should be applied.

### Adding New Implementations

If you want to add a new implementation for a different programming language or library:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-implementation`).
3. Add your implementation in the `implementations/` directory, following the existing structure.
4. Update the benchmark scripts to include your new implementation.
5. Add appropriate documentation for your implementation.
6. Submit a pull request with a clear description of your changes.

### Pull Requests

- Fill in the required template
- Do not include issue numbers in the PR title
- Include screenshots and animated GIFs in your pull request whenever possible.
- Follow the JavaScript styleguide.
- Include thoughtfully-worded, well-structured tests.
- Document new code based on the Documentation Styleguide
- End all files with a newline

## Styleguides

### Git Commit Messages

- Use the present tense ("Adds feature" not "Added feature")
- Describe what the commit does ("Moves cursor to..." not "Move cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

### JavaScript Styleguide

All JavaScript must adhere to [JavaScript Standard Style](https://standardjs.com/).

### Documentation Styleguide

- Use [Markdown](https://daringfireball.net/projects/markdown/).
- Reference methods and classes in markdown with the custom `{}` notation:
- Reference classes with `{ClassName}`
- Reference instance methods with `{ClassName::methodName}`
- Reference class methods with `{ClassName.methodName}`

## Additional Notes

### Issue and Pull Request Labels

This section lists the labels we use to help us track and manage issues and pull requests.

- `bug` - Issues that are bugs.
- `enhancement` - Issues that are feature requests.
- `help-wanted` - Issues that need assistance from the community.

Thank you for your contributions!
