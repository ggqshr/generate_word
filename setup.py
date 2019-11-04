import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_desc = f.read()

setuptools.setup(
    name="generate_week_report",
    version="0.0.1",
    author="ggq",
    author_email="ggq18663278150@gmail.com",
    description='一个python脚本，用来生成每周周报的word文档',
    long_description=long_desc,
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['generate_word = generate_word.generate_week_report:main']
    },
)
