import instaloader 
ig = instaloader.Instaloader()
uname = input ("masukan username: ")
ig.download_profile (uname, profile_pic_only = True)