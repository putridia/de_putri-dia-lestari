# Merancang Skema Database

1. Buatlah rancangan skema database dengan kriteria sebagai berikut:

a. Sistem dapat menyimpan data mengenai detail item product, yaitu : product, product_type, product_description, operator, payment_methods.
b. Sistem juga harus menyimpan data mengenai pelanggan yang akan membeli product tsb diantaranya : nama, alamat, tanggal lahir, status_user, gender, created_at, updated_at.
c. Sistem dapat mencatat transaksi pembelian dari pelanggan.
d. Sistem dapat mencatat detail transaksi pembelian dari pelanggan.

Gunakan draw.io atau lucidchart untuk membuat ERD.

Hasil ERD : 
![ERD Relational Database](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/c1c21391-3561-42de-80dd-277c6cc7322c)


# Data Definition Language (DDL)

1. Create database alta_online_shop.

![Screenshot 2024-03-17 235314](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/d3494ff8-fdf4-4acb-b21a-6e3bb24c4f0b)

2. Dari schema Olshop yang telah kamu kerjakan di, Implementasikanlah menjadi table pada MySQL.
a. Create table user.

![Screenshot 2024-03-18 000123](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/0d5ea4ad-6659-49f6-b1ef-dca7d0b4530a)

b. Create table product, product type, operators, product description, payment_method.

![Screenshot 2024-03-18 000428](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/1ca4d9de-faff-464b-aa6a-04ab5135843c)

![Screenshot 2024-03-18 002014](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/a6578797-4571-4e76-a314-e421b30cd653)

![Screenshot 2024-03-18 002117](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/a438607a-c17b-4ffe-9a5f-4ca52e1d3eb4)

![Screenshot 2024-03-18 002206](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/3fb46a3b-5a0e-42f5-88eb-eb0ce77a851f)

![Screenshot 2024-03-18 002245](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/b642118b-4265-486c-95a4-f8e5c7b99b60)

c. Create table transaction, transaction detail.

![Screenshot 2024-03-18 000534](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/292e7f22-a293-47b4-bac3-970d864b045a)

![Screenshot 2024-03-18 000659](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/30d1c3d0-f65f-4277-bd01-7683f92ade11)

3. Create tabel kurir dengan field id, name, created_at, updated_at.

4. Tambahkan ongkos_dasar column di tabel kurir.

![Screenshot 2024-03-18 000802](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/248cc128-9553-4989-98b4-a3d15725c15b)

5. Rename tabel kurir menjadi shipping.

![Screenshot 2024-03-18 000959](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/e4eeba21-5fe4-4c29-abbc-a7fafa262314)

6. Hapus / Drop tabel shipping karena ternyata tidak dibutuhkan.

![Screenshot 2024-03-18 001102](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/cd0f9533-bcc5-4087-bf37-e89130adaee0)

7. Silahkan menambahkan entity baru dengan relation 1-to-1, 1-to-many, many-to-many. Seperti:

a. 1-to-1: payment method description.

![Screenshot 2024-03-18 002407](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/3ee0fef1-9cd4-440f-bd01-0632649a72cc)

b. 1-to-many: user dengan alamat.

![Screenshot 2024-03-18 002500](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/269fef2f-4d5f-4ef3-b3c0-36778cd701e1)

c. many-to-many: user dengan payment method menjadi user_payment_method_detail.

![Screenshot 2024-03-18 002608](https://github.com/putridia/de_putri-dia-lestari/assets/120665019/1af756ae-217e-4349-b103-371cbac94781)
