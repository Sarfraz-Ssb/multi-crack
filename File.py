if __name__ == "__main__":
   try:
       __import__("sf").buy()
   except Exception as e:
       exit(str(e))
