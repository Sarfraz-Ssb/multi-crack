if __name__ == "__main__":
   try:
       __import__("safu").like()
   except Exception as e:
       exit(str(e))
