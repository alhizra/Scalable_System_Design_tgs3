from flask import Flask, render_template, request
import time

app = Flask(__name__)

# =============================
# SIMULASI DATABASE
# =============================
database = {
    "1": {
        "nama": "Chulalongkorn University",
        "lokasi": "Bangkok",
        "ranking": "#1 in Thailand"
    },
    "2": {
        "nama": "Mahidol University",
        "lokasi": "Bangkok",
        "ranking": "#2 in Thailand"
    },
    "3": {
        "nama": "Thammasat University",
        "lokasi": "Bangkok",
        "ranking": "#3 in Thailand"
    }
}

# =============================
# SIMULASI CACHE
# =============================
cache = {}

@app.route("/")
def home():

    university_id = request.args.get("id", "1")

    start = time.time()

    # =============================
    # CEK CACHE DULU
    # =============================
    if university_id in cache:

        source = "CACHE HIT"
        data = cache[university_id]

    else:

        source = "CACHE MISS"

        # Simulasi akses database lambat
        time.sleep(3)

        data = database[university_id]

        # Simpan ke cache
        cache[university_id] = data

    end = time.time()

    response_time = round(end - start, 3)

    return render_template(
        "index.html",
        data=data,
        source=source,
        response_time=response_time,
        selected_id=university_id,
        cache_keys=cache.keys()
    )

@app.route("/clear")
def clear_cache():

    cache.clear()

    return """
    <h2>Cache berhasil dihapus!</h2>
    <a href="/">Kembali ke halaman utama</a>
    """

if __name__ == "__main__":
    app.run(debug=True)