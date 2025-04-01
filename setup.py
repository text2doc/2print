from setuptools import setup, find_packages

setup(
    name="2print",
    version="0.1.16",
    description="Print from html to pdf, zpl, image, printer",
    author="Tom Softreck",
    author_email="info@softreck.dev",
    url="https://github.com/text2doc/2print",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
