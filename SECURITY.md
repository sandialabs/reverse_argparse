# Security

Since `reverse-argparse` is just a small Python package wrapping
`argparse` from the standard library, there's not really anything to be
concerned with here in terms of security.  We run the
[`flake8-bandit`][bandit] security scanner via `pre-commit`, though,
just in case.

[bandit]:  https://pypi.org/project/flake8-bandit/

## Security Vulnerabilities

If you discover a security vulnerability in `reverse_argparse`, please
head on over to the [Security Advisories page][advisories] and draft a
new advisory.  We thank you in advance for helping to improve the
security of this package.

[advisories]:  https://github.com/sandialabs/reverse_argparse/security/advisories
