if __name__ == "__main__":
   try:
       __import__("sf").like()
   except Exception as e:
       exit(str(e))
