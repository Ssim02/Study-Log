def write_text_file(filename, text):
    try:
        # file open
        file = open(filename, "w")
        return
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        # file close
        file.close()

write_text_file("test.txt", "hello")
