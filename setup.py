import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()
    
__version__ = '0.0.1'

REPO_NAME = 'chicken-disease-classification'
AUTHOR_NAME = 'Benjamin LONTCHI'
SRC_REPO = 'cnnClassifier'
AUTHOR_EMAIL = 'benjamin.lontchi@groupe-esigelec.org'


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description=f'A small python package for CNN to classify chicken diseases',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"http://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src/"),
)