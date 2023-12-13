from setuptools import setup, find_packages

setup(
    name='project_diabetic',  # Replace with your project's name
    version='0.1.0',  # Your project's version
    author='Mahlet',  # Your name
    author_email='formahlet@gmail.com',  # Your email
    description='This is simple setup for diaetic project ',  # Short description
    long_description=open('README.md').read(),  # Long description read from the the readme file
    long_description_content_type='text/markdown',  # Type of the long description
    url='https://github.com/@mahlettaye/project_diabetic',  # Link to your project's repository
    packages=find_packages(),  # Automatically find all packages
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum version requirement of the package
    install_requires=[
        # List all dependencies:
        'fastapi'
        'uvicorn'
        'scikit-learn==1.2.2'
        'pandas'
        'joblib'
        'pydantic'
        'numpy'
    ],
    include_package_data=True,  # Include non-code files specified in MANIFEST.in
   
)