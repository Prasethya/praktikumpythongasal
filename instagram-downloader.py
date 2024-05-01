import instaloader

#buat instance intaloader
loader = instaloader.Instaloader()

#fugsi untuk mengunduh postingan instagram berdasarkan URL
def download_post(url):
    try:
        #mendapatkan meta data postingan
        post = instaloader.Post.from_shortcode(loader.context, url.split("/")[-2])

        #mengunduh postingan
        loader.download_post(post, target="aplikasi tambahan")
        print("postingan berhasil diunduh!")
    except Exception as e:
        print("terjadi kesalahan:", str(e))

#demo progam
url = input("enter your url: ")
url = str(url)
download_post(url)

    