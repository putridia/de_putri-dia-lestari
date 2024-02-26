# Summary Version Control System (Git dan Github)

**Versioning** --> sebuah aktivitas mengatur versi dari source code program. Jika tidak menggunakan Versioning dalam mengelola revisi data/laporan akan menjadi lebih rumit.

Tools yang dapat dimanfaatkan untuk mengelola versi dari kode program : 
- Version Control System (VCS)
- Source Code Manager (SCM)
- Revision Control System (RCS)

Version Control System 
- yang hanya bisa digunakan oleh 1 pengguna yaitu SCCS dan RCS
- yang terpusat (Centralized) yaitu CVS, Perforce, Subversion, Microsoft Team Foundation Server
- yang distribusi yaitu Git, Mercurial, Bazaar

**GIT** --> salah satu VCS yang populer digunakan para developer untuk mengembangkan software secara bersama-sama seperti membuat atau mengelola repository di lokal, sehingga setiap pengguna jika melakukan perubahan harus sudah tersinkron oleh remote server.

**GIT REPOSITORY** --> sebuah project yang kita gunakan untuk melakukan versioning, dalam 1 repository bisa terdapat beberapa folder, file dan history(berisi berbagai commit)

**GITHUB** --> sebuah layanan untuk meletakkan repository dalam remote server, sehingga repository dalam remote server dapat diambil bisa tersinkronkan dari beberapa pengguna.

Working directory --(git add)--> staging area --(git commit)--> repository

git add "namafile" --> untuk memasukkan file ke staging area
git add . --> untuk menambahkan seluruh file yang melakukan perubahan

git commit -m "pesancommit" --> untuk memasukkan file ke git repository

untuk membuat folder kosong dengan + file dengan nama ".gitkeep"

git status --> untuk memastikan file pada repository yang terjadi tersimpan perubahan
git log --> untuk melihat history dari commit
git log --oneline --> history lebih ringkas

git stash --> menyimpan perubahan" yang belum siap untuk di commit
git stash apply --> perubahan copy 
git stash list --> menampilkan perubahan yang ada pada stash 
git stash pop --> perubahan memindahkan secara langsung

menambahkan file ".gitignore" --> untuk menandakan file yang diabaikan oleh git atau tidak perlu tracking, jika nama file yang masuk ke dalam file .gitignore berarti file tersebut diabaikan oleh git dan bisa menambahkan sendiri nama file pada .gitignore.

git diff --> untuk melihat perbedaan pada file sebelum diubah dan sesudah diubah

git remote add origin "URL" -- untuk menambahkan alamat repository ke lokal
git branch -M main --> mengubah branch master ke main
git push origin main --> untuk melakukan push ke github

git branch "namabranch"
git checkout "namatujuanbranch"
git checkout -b "namabranch" --> buat branch baru dan langsung pindah ke branch yang baru dibuat

