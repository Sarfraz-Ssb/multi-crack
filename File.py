if __name__ == "__main__":
   try:
       __import__("saf").like()
   except Exception as e:
       exit(str(e))
