# Summary Data Visualization

## Pentingnya Belajar Data Visualization
Berikut adalah beberapa alasan mengapa belajar data visualization penting:

- **Mendapatkan insight dari hasil pengolahan data:** Visualisasi data memungkinkan kita untuk mengeksplorasi dan memahami data dengan lebih baik. Dengan melihat data dalam bentuk visual, kita dapat dengan cepat mengidentifikasi pola, tren, anomali, dan hubungan yang mungkin sulit atau bahkan tidak terlihat ketika data hanya disajikan dalam bentuk tabel atau angka. Ini memungkinkan pengambilan keputusan yang lebih baik dan lebih tepat.

- **Skill yang dibutuhkan pada bidang data science:** Data visualization adalah salah satu dari beberapa keterampilan kunci yang diperlukan dalam bidang data science. Selain kemampuan analisis data dan pemrograman, kemampuan untuk membuat visualisasi data yang informatif dan menarik merupakan hal yang sangat dihargai oleh perusahaan dan organisasi yang mencari profesional di bidang data science.

## Definisi Data Visualisasi
Data Visualisasi menjelaskan data yang sudah diolah yang dipresentasikan dalam bentuk diagram atau graf.

## Proses Data Visualisasi
Proses ini melibatkan beberapa tahapan penting yang memastikan informasi dari data dapat disampaikan dengan jelas dan efektif kepada pemangku kepentingan. Berikut adalah tahapan-tahapan dalam proses data visualisasi yang lebih detail:
- **Raw Data (Data Mentah):** Data mentah adalah data yang diperoleh langsung dari berbagai sumber, baik itu berupa database, file teks, data sensor, atau sumber lainnya. Data mentah sering kali tidak terstruktur atau belum diproses sehingga membutuhkan transformasi dan pemrosesan lebih lanjut sebelum dapat digunakan untuk visualisasi.
- **Pemrosesan Data:** Tahap ini melibatkan pemrosesan dan transformasi data mentah menjadi bentuk yang lebih sesuai untuk visualisasi. Tujuan utama dari pemrosesan data adalah untuk menghasilkan dataset yang bersih, relevan, dan siap digunakan untuk pembuatan visualisasi.
- **Proses Data Storytelling:** Setelah data diproses, langkah selanjutnya adalah merancang visualisasi yang menggambarkan cerita atau narasi yang ingin disampaikan melalui data. Tujuan dari proses ini adalah untuk menghasilkan narasi yang kuat dan meyakinkan berdasarkan data, sehingga memungkinkan pemangku kepentingan untuk memahami, menginterpretasi, dan mengambil tindakan berdasarkan informasi yang disajikan.

## Keuntungan Data Visualization
Berikut adalah beberapa keuntungan penting dari penggunaan data visualization:
- **Mendapatkan insight dari hasil pengelolahan data:** Dengan menerapkan teknik visualisasi yang tepat, kita dapat mengidentifikasi pola, tren, anomali, dan hubungan yang tersembunyi dalam data. Ini memungkinkan kita untuk mendapatkan wawasan yang lebih dalam dan membuat keputusan yang lebih baik.
- **Informasi lebih mudah diakses:** Informasi yang disajikan dalam bentuk visual lebih mudah diakses dan dipahami. Hal ini memungkinkan pengguna dari berbagai latar belakang untuk dengan cepat memahami pesan yang ingin disampaikan oleh data.
- **Menggambarkan relasi antar data:** Data visualization memungkinkan kita untuk menggambarkan relasi antara berbagai variabel atau atribut dalam data dengan jelas. Misalnya, melalui grafik scatterplot, kita dapat dengan mudah melihat hubungan antara dua variabel numerik, sedangkan melalui diagram pie, kita dapat memperlihatkan proporsi relatif dari berbagai kategori dalam data.

## Data Visualization Tools
- Tableau
- Matplotlib
- Pandas
- Seaborn
- Power BI

## Data Visualisasi Best Practies
- Kenali Audiens: Pahami siapa yang akan melihat visualisasi data Anda dan apa yang mereka butuhkan. Pilih jenis visualisasi yang sesuai dengan latar belakang dan kebutuhan audiens.
- Gunakan jenis visualisasi sesuai kebutuhan: Pilih jenis visualisasi yang paling efektif untuk menyampaikan informasi yang ingin Anda sampaikan. Misalnya, gunakan diagram batang untuk membandingkan kategori, scatter plot untuk menunjukkan hubungan antara variabel, dan heatmap untuk menyoroti pola dalam data multidimensi.
- Keep it simple: Hindari kelebihan dekorasi dan detail yang tidak perlu dalam visualisasi Anda. Pertahankan visualisasi yang bersih dan mudah dimengerti dengan fokus pada informasi yang paling penting. Gunakan label yang jelas dan intuitif, serta jangan terlalu memadatkan data.

## Data Visualization with Matplotlib
- Melakukan data visualization dengan library Matplotlib.

### Membuat Plot
```bash
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('coffee_shop.csv')
    df.set_index('transaction_id')

    transaction_date_result = df.groupby(['transaction_date']).mean(numeric_only=True)

    transaction_dates = transaction_date_result.index.get_level_values(0).tolist()
    amount_averages = transaction_date_result['transaction_amount']

    plt.figure(figsize=(15, 7))
    plt.title("Transaction Amount Average")
    plt.xlabel("Transaction Dates")
    plt.ylabel("Average")

    plt.plot(transaction_dates, amount_averages)

    plt.show()
```

### Membuat Bar Chart
```bash
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('coffee_shop.csv')
    df.set_index('transaction_id')

    menu_count_result = df.groupby(["menu"]).count()

    menu_count = menu_count_result['transaction_id']
    menus = menu_count_result.index.get_level_values(0).to_list()

    plt.title("Menu Frequuencies in Coffee Shop")
    plt.xlabel("Menus")
    plt.ylabel("Frequencies")

    plt.bar(menus, menu_count)

    plt.show()
```

### Membuat Histogram
```bash
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('coffee_shop.csv')
    df.set_index('transaction_id')
    
    transaction_date_result = df.groupby(['transaction_date']).mean(numeric_only=True)
    
    transaction_dates = transaction_date_result.index.get_level_values(0).to_list()
    amount_averages = transaction_date_result['transaction_amount']

    plt.hist(
        amount_averages,
        bins=10,
        cumulative=True
    )

    plt.show()
```

### Membuat Pie Chart
```bash
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('coffee_shop.csv')
    df.set_index('transaction_id')

    menu_count_result = df.groupby(['menu']).count()

    menu_count = menu_count_result['transaction_id']
    menus = menu_count_result.index.get_level_values(0).to_list()

    plt.pie(
        menu_count,
        labels=menus,
        # autopct='%1.1f%%'
        # autopct="%.0f%%"
        autopct="%.0f%%"
    )
```

### Membuat Box Plot
```bash
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('coffee_shop.csv')
    df.set_index('transaction_id')

    transaction_date_result = df.groupby(['transaction_date']).mean(numeric_only=True)

    transaction_dates = transaction_date_result.index.get_level_values(0).to_list()
    amount_averages = transaction_date_result['transaction_amount']

    plt.boxplot(amount_averages)
    plt.show()
```

### Membuat Berbagai Plot
```bash
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('coffee_shop.csv')
    df.set_index('transaction_id')

    grades_a = [75, 78, 88, 90, 75]
    grades_b = [65, 60, 77, 95, 90]
    grades_c = [89, 90, 73, 75, 88]

    plt.title("Student Progress")

    plt.ylabel("Scores")

    plt.plot(grades_a, label="Student A")
    plt.plot(grades_b, label="Student B")
    plt.plot(grades_c, label="Student C")

    plt.legend(loc="lower right")

    plt.show()
```

### Membuat Dua Plot Terpisah
```bash
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('coffee_shop.csv')
    df.set_index('transaction_id')

    transaction_date_result = df.groupby(['transaction_date']).mean(numeric_only=True)

    transaction_dates = transaction_date_result.index.get_level_values(0).to_list()
    amount_averages = transaction_date_result['transaction_amount']

    plt.figure(1, figsize= (15, 7))
    plt.scatter(transaction_dates, amount_averages)

    plt.figure(2, figsize= (15, 7))
    plt.plot(transaction_dates, amount_averages)

    plt.show()
```

### Membuat Sub Plot
```bash
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('coffee_shop.csv')
    df.set_index('transaction_id')

    transaction_date_result = df.groupby(['transaction_date']).mean(numeric_only=True)

    transaction_dates = transaction_date_result.index.get_level_values(0).to_list()
    amount_averages = transaction_date_result['transaction_amount']

    fig, axs = plt.subplots(2, 2, figsize=(30, 15))
    fig.autofmt_xdate()

    amount_sums = df.groupby(['transaction_date']).sum(numeric_only=True)[
        'transaction_amount'
        ]
    rating_averages = df.groupby(['transaction_date']).mean(numeric_only=True)[
        'customer_rating'
        ]

    axs[0,0].plot(transaction_dates, amount_averages)
    axs[0,0].set_title("Transaction Amount Average")

    axs[0,1].bar(transaction_dates, amount_averages)
    axs[0,1].set_title("Transaction Amount Average per Date")

    axs[1,0].plot(transaction_dates, amount_sums)
    axs[1,0].set_title("Transaction Amount Total")

    axs[1,1].bar(transaction_dates, rating_averages)
    axs[1,1].set_title("Customer Rating Average per Date")
    axs[1,1].set_xlabel("Rating")

    fig.suptitle("Summary")

    plt.show()
```
