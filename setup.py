from setuptools import setup, find_packages

setup(
    name="HomeScheduler",
    version="1.0.0",
    description="A Python application to schedule daily tasks and alarms.",
    author="FelipeFTN",
    author_email="your.email@example.com",
    url="https://github.com/FelipeFTN/HomeScheduler",
    packages=find_packages("src"),  # Automatically find Python packages in the 'src' directory
    package_dir={"": "src"},  # Tells setuptools that the source code is in 'src'
    include_package_data=True,  # Include non-Python files
    install_requires=[
        # Add dependencies listed in requirements.txt
        "playsound==1.3.0",  # Example dependency for playing sounds
    ],
    entry_points={
        "console_scripts": [
            "HomeScheduler=main:main",  # Replace 'main:main' with your entry point function
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    package_data={
        "": ["../schedules/*.json", "../songs/*.mp3"],  # Include all JSON and MP3 files
    },
    keywords="scheduler alarms tasks JSON",
)
