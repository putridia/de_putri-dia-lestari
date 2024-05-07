<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">DE_PUTRI-DIA-LESTARI</h1>
</p>
<p align="center">
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/putridia/de_putri-dia-lestari?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/putridia/de_putri-dia-lestari?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/putridia/de_putri-dia-lestari?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/putridia/de_putri-dia-lestari?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat&logo=Jupyter&logoColor=white" alt="Jupyter">
	<img src="https://img.shields.io/badge/.ENV-ECD53F.svg?style=flat&logo=dotenv&logoColor=black" alt=".ENV">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/PowerShell-5391FE.svg?style=flat&logo=PowerShell&logoColor=white" alt="PowerShell">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=flat&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON">
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Repository Structure](#-repository-structure)
> - [ Modules](#-modules)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running de_putri-dia-lestari](#-running-de_putri-dia-lestari)
>   - [ Tests](#-tests)
> - [ Project Roadmap](#-project-roadmap)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

Repository ini berisi panduan dan kode untuk praktek materi Data Engineer dari Alterra Academy. Materi yang dibahas meliputi fundamental Data Engineer, pemrograman Python, Pandas, RDBMS (PostgreSQL), Git, Github, CLI Linux, Docker, REST API, konsep dasar Data Engineering, pengambilan data, transformasi data, dan Data Engineering di cloud.

---

##  Repository Structure

```sh
└── de_putri-dia-lestari/
    ├── 01_Pengenalan Data Engineer Part 1
    │   ├── Praktikum
    │   │   ├── Ekplorasi.md
    │   │   ├── Prioritas 1.md
    │   │   └── Prioritas 2.md
    │   └── Readme.md
    ├── 02_Introduction Algorithm
    │   ├── Praktikum
    │   │   └── Readme.md
    │   └── Readme.md
    ├── 03_Version Control System (Git and Github)
    │   ├── Praktikum
    │   │   ├── Soal_Eksplorasi.md
    │   │   ├── Soal_Prioritas_1.md
    │   │   └── Soal_Prioritas_2.md
    │   └── Readme.md
    ├── 04_Basic Programming with Python
    │   ├── Praktikum
    │   │   ├── Soal Ekplorasi_no.1.py
    │   │   ├── Soal Prioritas 1_no.1.py
    │   │   ├── Soal Prioritas 1_no.2.py
    │   │   ├── Soal Prioritas 1_no.3.py
    │   │   ├── Soal Prioritas 2_no.1.py
    │   │   └── Soal Prioritas 2_no.2.py
    │   └── Readme.md
    ├── 05_Basic Programming with Python and Virtual Envoronment
    │   ├── Praktikum
    │   │   └── .gitkeep
    │   └── Readme.md
    ├── 06_Object Oriented Programming
    │   ├── Praktikum
    │   │   ├── Soal_Eksplorasi.py
    │   │   ├── Soal_Prioritas1.py
    │   │   └── Soal_Prioritas2.py
    │   └── Readme.md
    ├── 07_Data Structure and Algorithm
    │   └── Praktikum
    │       └── Praktikum
    │           └── Praktikum
    │               └── Praktikum
    ├── 08_Relational Database
    │   ├── Praktikum
    │   │   └── Task_Relational Database.md
    │   └── Readme.md
    ├── 09_REST API
    │   ├── Praktikum
    │   │   ├── Prioritas 1 & 2 - REST API.postman_collection.json
    │   │   ├── RentABook API.postman_collection.json
    │   │   └── Task_REST API.md
    │   └── Readme.md
    ├── 10_Docker
    │   ├── Praktikum
    │   │   ├── Ekplorasi
    │   │   │   ├── .dockerignore
    │   │   │   ├── .env
    │   │   │   ├── .env.example
    │   │   │   ├── Dockerfile
    │   │   │   ├── docker-compose.yml
    │   │   │   ├── main.py
    │   │   │   ├── readme-step_eksplorasi.md
    │   │   │   └── requirements.txt
    │   │   ├── Prioritas1
    │   │   │   ├── Dockerfile
    │   │   │   ├── data.csv
    │   │   │   ├── main.py
    │   │   │   ├── readme-step_prioritas1.md
    │   │   │   └── requirements.txt
    │   │   └── Prioritas2
    │   │       ├── .dockerignore
    │   │       ├── .env
    │   │       ├── .env.example
    │   │       ├── Dockerfile
    │   │       ├── docker-compose.yml
    │   │       ├── main.py
    │   │       ├── readme-step_prioritas2.md
    │   │       └── requirements.txt
    │   └── Readme.md
    ├── 11_Fundamental Data Engineer Part 2
    │   ├── Praktikum
    │   │   ├── Soal_Ekplorasi.md
    │   │   ├── Soal_Prioritas1.md
    │   │   └── Soal_Prioritas2.md
    │   └── Readme.md
    ├── 12_Data Warehouse dan Data Lake(Part 1)
    │   ├── Praktikum
    │   │   ├── Soal_Ekplorasi.md
    │   │   ├── Soal_Prioritas1.md
    │   │   ├── Soal_Prioritas2.md
    │   │   ├── eksplorasi-query.sql
    │   │   └── prioritas2.sql
    │   └── Readme.md
    ├── 13_Code Compentence 1 DE
    │   ├── Praktikum
    │   │   ├── Readme.md
    │   │   ├── sentiment_bad.csv
    │   │   ├── sentiment_chatgpt.sql
    │   │   ├── sentiment_counts.csv
    │   │   ├── sentiment_good.csv
    │   │   ├── sentiment_neutral.csv
    │   │   └── venv_code
    │   │       ├── .gitignore
    │   │       ├── Lib
    │   │       │   └── site-packages
    │   │       ├── Scripts
    │   │       │   ├── activate
    │   │       │   ├── activate.bat
    │   │       │   ├── activate.fish
    │   │       │   ├── activate.nu
    │   │       │   ├── activate.ps1
    │   │       │   ├── activate_this.py
    │   │       │   ├── deactivate.bat
    │   │       │   ├── pip-3.12.exe
    │   │       │   ├── pip.exe
    │   │       │   ├── pip3.12.exe
    │   │       │   ├── pip3.exe
    │   │       │   ├── pydoc.bat
    │   │       │   ├── python.exe
    │   │       │   └── pythonw.exe
    │   │       ├── data_source
    │   │       │   └── file.csv
    │   │       ├── database_manager.py
    │   │       ├── pyvenv.cfg
    │   │       └── sentiment_classifier.py
    │   └── Readme.md
    ├── 14_Data Warehouse dan Data Lake Part 2
    │   └── Readme.md
    ├── 15_Data Ingestion with Python from Various Sources
    │   ├── Praktikum
    │   │   ├── Prioritas1
    │   │   │   ├── Prioritas_1.ipynb
    │   │   │   ├── customers.sql
    │   │   │   ├── output_fileprioritas1.parquet
    │   │   │   ├── products.xlsx
    │   │   │   └── transactions.csv
    │   │   └── Prioritas2
    │   │       ├── Prioritas_2.ipynb
    │   │       └── barenbliss_products.csv
    │   ├── Readme.md
    │   └── Screenshot
    │       └── Prioritas1.png
    ├── 16_Data Transformation
    │   ├── Praktikum
    │   │   ├── Prioritas1
    │   │   │   ├── Soal Prioritas 1.ipynb
    │   │   │   └── house_listings.csv
    │   │   └── Priotitas2
    │   │       ├── Soal Prioritas 2.ipynb
    │   │       └── house_listings.csv
    │   ├── Readme.md
    │   └── Screenshot
    │       ├── Prioritas1
    │       │   ├── no.1.png
    │       │   ├── no.2.png
    │       │   └── no.3.png
    │       └── Prioritas2
    │           ├── no.1-1.png
    │           ├── no.1-2.png
    │           ├── no.1-3.png
    │           ├── no.1-4.png
    │           ├── no.1-5.png
    │           ├── no.2-1.png
    │           ├── no.2-2.png
    │           ├── no.2-3.png
    │           └── no.3.png
    ├── 17_Workflow Orchestration with Apache Airflow
    │   ├── Praktikum
    │   │   ├── Prioritas 1
    │   │   │   ├── Soal&Jawaban.md
    │   │   │   ├── prioritas1_no.1.py
    │   │   │   └── prioritas1_no.2.py
    │   │   └── Prioritas 2
    │   │       ├── Soal&Jawaban.md
    │   │       └── prioritas2.py
    │   └── Readme.md
    ├── 19_Data Engineering in the Cloud
    │   └── Readme.md
    ├── 20_Big Data Technologies
    │   ├── Praktikum
    │   │   ├── Prioritas 1
    │   │   │   └── jawaban_prioritas1.md
    │   │   └── Prioritas 2
    │   │       ├── input1.txt
    │   │       ├── input2.txt
    │   │       ├── input3.txt
    │   │       ├── mapper.py
    │   │       └── reducer.py
    │   └── Readme.md
    ├── 21_Pemahaman tentang Data Quality dan Data Governance
    │   ├── Praktikum
    │   │   ├── Prioritas 1
    │   │   │   └── Jawaban_Prioritas1.md
    │   │   └── Prioritas 2
    │   │       ├── jawaban_prioritas2.ipynb
    │   │       └── tx_data.csv
    │   └── Readme.md
    ├── 22_Data Visualization
    │   ├── Praktikum
    │   │   ├── Prioritas 1
    │   │   │   ├── bakery.csv
    │   │   │   ├── electronic_shop.csv
    │   │   │   └── jawaban.ipynb
    │   │   └── Prioritas 2
    │   │       ├── e-commerce.json
    │   │       ├── jawaban.ipynb
    │   │       └── survey.csv
    │   └── Readme.md
    ├── 23_Introduction AI on Data Engineer
    │   ├── Praktikum
    │   │   ├── input&output_prioritas1.txt
    │   │   ├── input&output_prioritas2.txt
    │   │   ├── soal&jawaban_prioritas1.md
    │   │   └── soal&jawaban_prioritas2.md
    │   └── Readme.md
    ├── 24_Implemention AI on Data Engineer
    │   └── Readme.md
    └── README.md
```

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version x.y.z`

###  Installation

1. Clone the de_putri-dia-lestari repository:

```sh
git clone https://github.com/putridia/de_putri-dia-lestari
```

2. Change to the project directory:

```sh
cd de_putri-dia-lestari
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running de_putri-dia-lestari

Use the following command to run de_putri-dia-lestari:

```sh
python main.py
```

###  Tests

To execute tests, run:

```sh
pytest
```

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/putridia/de_putri-dia-lestari/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/putridia/de_putri-dia-lestari/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/putridia/de_putri-dia-lestari/issues)**: Submit bugs found or log feature requests for De_putri-dia-lestari.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/putridia/de_putri-dia-lestari
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.
  - Putri Dia Lestari for her invaluable contributions.
  - Alterra Academy for their support and inspiration.

[**Return**](#-quick-links)

---
