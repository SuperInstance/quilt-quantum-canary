from setuptools import setup, find_packages
setup(
    name="quilt-quantum-canary",
    version="0.1.0",
    description="Polyformalism canary verified by quantum amplitude (5 quantum schemes)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Casey / SuperInstance",
    packages=find_packages(),
    python_requires=">=3.8",
)
