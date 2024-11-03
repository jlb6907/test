import pymupdf

# New doc
mydoc = pymupdf.open()

# Toc creation
mydoc.insert_page(0, text="Chapter 1", fontsize=20, width=595, height=842, fontname='helv', fontfile=None, color=None)
mydoc.insert_page(1, text="Chapter 1.1", fontsize=12, width=595, height=842, fontname='helv', fontfile=None, color=None)
mydoc.insert_page(2, text="Chapter 1.2", fontsize=12, width=595, height=842, fontname='helv', fontfile=None, color=None)
mydoc.insert_page(3, text="Chapter 2", fontsize=20, width=595, height=842, fontname='helv', fontfile=None, color=None)
mydoc.insert_page(4, text="Chapter 2.1", fontsize=12, width=595, height=842, fontname='helv', fontfile=None, color=None)
mydoc.insert_page(5, text="Chapter 2.2", fontsize=12, width=595, height=842, fontname='helv', fontfile=None, color=None)
mydoc.insert_page(6, text="Chapter 2.3", fontsize=12, width=595, height=842, fontname='helv', fontfile=None, color=None)

mytoc = [
        [1, "Chapter 1", 1], 
        [2, "Chapter 1.1", 2],
        [2, "Chapter 1.2", 3],
        [1, "Chapter 2", 4],
        [2, "Chapter 2.1", 5],
        [2, "Chapter 2.2", 6],
        [2, "Chapter 2.3", 7]
         ]
mydoc.set_toc(mytoc)

# PDF File without encryption
mydoc.save("sample.pdf")

# PDF File with encryption
password = "mypassword"
mydoc.save("sample_encrypt.pdf", owner_pw=password,  user_pw=password, encryption=pymupdf.PDF_ENCRYPT_AES_256, permissions=(pymupdf.PDF_PERM_ACCESSIBILITY))
