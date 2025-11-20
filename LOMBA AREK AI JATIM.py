# ===============================================================
#    PROGRAM REKOMENDASI INVESTASI UNTUK PELAJAR DI INDONESIA
# ===============================================================

def garis():
    print("=" * 65)

def rekomendasi_investasi(sisa):
    """Memberikan rekomendasi berdasarkan sisa uang yang bisa diinvestasikan"""
    if sisa <= 10000:
        return (
            "⚠️ Nominal uangmu masih belum mencukupi untuk memulai investasi.\n"
            "Fokuskan uangmu untuk menambah tabungan dan dana darurat terlebih  dahulu."
        )
    elif 11000 <= sisa < 50000:
        return (
            "ℹ️ Sisa uang masih kecil untuk investasi.\n"
            "Mulailah dengan menabung terlebih dahulu sampai mencapai nominal minimal Rp 50.000."
        )
    elif 50000 <= sisa < 200000:
        return (
            "✅ Kamu sudah bisa mulai investasi kecil!\n"
            "- Pilihan terbaik: Reksa Dana Pasar Uang atau Tabungan Emas."
        )
    elif 200000 <= sisa < 500000:
        return (
            "👍 Kamu cocok untuk mulai investasi rutin.\n"
            "- Rekomendasi: RDPU, Reksadana Pendapatan Tetap, Tabungan Emas."
        )
    else:
        return (
            "🔥 Kamu sangat layak mulai investasi.\n"
            "- Rekomendasi: RDPU, RDPT, Emas, Deposito kecil, bahkan SBN ritel."
        )


def info_instrumen():
    instrumen = {
        "Reksa Dana Pasar Uang (RDPU)": {
            "Keuntungan": [
                "Risiko rendah, cocok untuk pemula.",
                "Bisa mulai dari Rp 10.000.",
                "Likuid (mudah dicairkan)."
            ],
            "Kerugian": [
                "Keuntungan tidak terlalu besar.",
                "Masih dapat terpengaruh kondisi pasar."
            ]
        },
        "Reksa Dana Pendapatan Tetap (RDPT)": {
            "Keuntungan": [
                "Potensi return lebih tinggi daripada RDPU.",
                "Risiko tetap lebih rendah dibanding saham.",
            ],
            "Kerugian": [
                "Nilai bisa turun jika pasar obligasi melemah.",
                "Tidak cocok untuk jangka sangat pendek."
            ]
        },
        "Deposito Bank": {
            "Keuntungan": [
                "Sangat aman karena dijamin LPS.",
                "Bunga stabil dan pasti.",
            ],
            "Kerugian": [
                "Tidak bisa dicairkan sebelum jatuh tempo.",
                "Minimal deposit biasanya cukup besar.",
            ]
        },
        "Emas (tabungan emas / emas fisik)": {
            "Keuntungan": [
                "Nilai stabil jangka panjang.",
                "Cocok untuk melawan inflasi.",
                "Bisa mulai kecil melalui tabungan emas."
            ],
            "Kerugian": [
                "Keuntungan tidak cepat.",
                "Emas fisik butuh tempat penyimpanan aman."
            ]
        }
    }

    garis()
    print("📘 INFORMASI PILIHAN INVESTASI ANDA")
    garis()

    for nama, data in instrumen.items():
        print(f"\n🔹 {nama}")
        print("   ➤ Keuntungan:")
        for k in data["Keuntungan"]:
            print(f"      - {k}")
        print("   ➤ Kerugian:")
        for r in data["Kerugian"]:
            print(f"      - {r}")


def main():

    # Input data
    garis()
    print("🧑‍🎓 PROGRAM REKOMENDASI INVESTASI PELAJAR INDONESIA 🧑‍🎓")
    garis()
    nama = input("Nama pelajar                : ")
    jenjang = input("Jenjang pendidikan (SMP/SMA/SMK) : ")

    # Input uang saku
    while True:
        try:
            uang_saku = int(input("Uang saku bulanan (Rp)      : "))
            break
        except ValueError:
            print("❗ Masukkan angka yang valid.")

    # Input budgeting
    garis()
    print("📌 Masukkan pengelolaan uang bulanan:")
    while True:
        try:
            sekolah = int(input("  Kebutuhan sekolah (Rp)    : "))
            transport = int(input("  Transportasi (Rp)         : "))
            jajan = int(input("  Jajan (Rp)                : "))
            tabungan = int(input("  Tabungan (Rp)             : "))
            break
        except ValueError:
            print("❗ Masukkan angka yang valid.")

    total_pengeluaran = sekolah + transport + jajan + tabungan
    sisa = uang_saku - total_pengeluaran

    # Output hasil
    garis()
    print("📄 PROFIL PELAJAR")
    garis()
    print(f"Nama pelajar      : {nama}")
    print(f"Jenjang pendidikan : {jenjang}")
    print(f"Uang saku bulanan : Rp {uang_saku:,}")

    garis()
    print("📊 RINCIAN BUDGETING:")
    garis()
    print(f"- Kebutuhan sekolah : Rp {sekolah:,}")
    print(f"- Transportasi      : Rp {transport:,}")
    print(f"- Jajan             : Rp {jajan:,}")
    print(f"- Tabungan          : Rp {tabungan:,}")
    print(f"- Total pengeluaran : Rp {total_pengeluaran:,}")
    garis()
    print(f"💰 Sisa uang untuk investasi : Rp {sisa:,}")

    garis()
    print("📌 HASIL ANALISIS PENGELOLAAN UANG BULANAN:")
    print(rekomendasi_investasi(sisa))

    info_instrumen()

    garis()
    print("🎯Start from a small amount, be consistent every month.")
    garis()


if __name__ == "__main__":
    main()
