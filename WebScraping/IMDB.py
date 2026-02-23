from imdb import Cinemagoer
import json

def get_imdb_info(query):
    ia = Cinemagoer()
    
    try:
        if str(query).lower().startswith('tt'):
            movie_id = str(query).lower().replace('tt', '')
            movie = ia.get_movie(movie_id)
        else:
            results = ia.search_movie(str(query))
            if not results:
                return {"error": "هیچ نتیجه‌ای پیدا نشد 😕"}
            
            movie = results[0]
            ia.update(movie, info=['main', 'plot', 'cast', 'awards'])
        
        data = {
            "عنوان": movie.get('title'),
            "سال انتشار": movie.get('year'),
            "امتیاز IMDb": movie.get('rating'),
            "تعداد رأی": movie.get('votes'),
            "رتبه در Top 250": movie.get('top 250 rank'),
            "ژانرها": movie.get('genres', []),
            "کارگردانان": [p.get('name') for p in movie.get('directors', [])],
            "نویسندگان": [p.get('name') for p in movie.get('writers', [])][:5],
            "بازیگران اصلی": [p.get('name') for p in movie.get('cast', [])][:10],
            "خلاصه داستان": movie.get('plot outline') or 
                           (movie.get('plot', [''])[0] if movie.get('plot') else None),
            "مدت زمان": movie.get('runtimes', [None])[0],
            "کشورها": movie.get('countries', []),
            "زبان‌ها": movie.get('languages', []),
            "کد IMDb": f"tt{movie.movieID}",
            "لینک IMDb": f"https://www.imdb.com/title/tt{movie.movieID}/"
        }
        
        return data
        
    except Exception as e:
        return {"error": f"خطا: {str(e)}"}


if __name__ == "__main__":
    query = input("نام فیلم یا سریال یا کد IMDb وارد کنید (مثال: Inception یا tt1375666): ").strip()
    
    info = get_imdb_info(query)
    
    print("\n" + "═" * 60)
    if "error" in info:
        print(info["error"])
    else:
        for key, value in info.items():
            if isinstance(value, list) and value:
                print(f"{key}: {', '.join(map(str, value))}")
            elif value is not None:
                print(f"{key}: {value}")
    
    with open("imdb_info.json", "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=4)
    print("\n imdb_info.json  saved!")